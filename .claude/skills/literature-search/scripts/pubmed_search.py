#!/usr/bin/env python3
"""
Search and analyze scientific literature from PubMed.

Usage:
    python pubmed_search.py "EGFR resistance" --output results.json
    python pubmed_search.py "KRAS G12C" --start 2023-01-01 --end 2024-12-31
    python pubmed_search.py PROTAC --trend --years 5
"""

import argparse
import json
import sys
from datetime import datetime
from typing import Optional, Dict, Any, List
import requests
import time


class PubMedSearcher:
    """Search and analyze PubMed literature."""

    def __init__(self, query: str):
        self.query = query
        self.base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
        self.results = {
            "query": query,
            "data": {},
            "timestamp": datetime.now().isoformat()
        }
        self.api_key = None  # Optional: Set your NCBI API key for higher rate limits

    def _esearch(self, term: str, **params) -> Dict[str, Any]:
        """Execute ESearch query."""
        url = f"{self.base_url}/esearch.fcgi"
        default_params = {
            "db": "pubmed",
            "term": term,
            "retmode": "json",
            "retmax": params.get("retmax", 500)
        }
        default_params.update(params)

        response = requests.get(url, params=default_params, timeout=30)
        response.raise_for_status()
        return response.json()

    def _esummary(self, pmids: List[str]) -> Dict[str, Any]:
        """Execute ESummary query."""
        url = f"{self.base_url}/esummary.fcgi"
        params = {
            "db": "pubmed",
            "id": ",".join(pmids),
            "retmode": "json"
        }

        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()

    def _efetch(self, pmids: List[str]) -> Dict[str, Any]:
        """Execute EFetch query for detailed records."""
        url = f"{self.base_url}/efetch.fcgi"
        params = {
            "db": "pubmed",
            "id": ",".join(pmids),
            "retmode": "xml",
            "rettype": "abstract"
        }

        response = requests.get(url, params=params, timeout=60)
        response.raise_for_status()
        return response.text

    def search(self, start_date: Optional[str] = None, end_date: Optional[str] = None,
               max_results: int = 100) -> List[Dict[str, Any]]:
        """Search PubMed and return paper details."""
        try:
            # Build query with date filters
            query = self.query
            if start_date or end_date:
                date_parts = []
                if start_date:
                    date_parts.append(f"{start_date}[Date - Publication] : 3000[Date - Publication]")
                if end_date:
                    date_parts.append(f"1900[Date - Publication] : {end_date}[Date - Publication]")
                if date_parts:
                    query = f"({self.query}) AND ({' AND '.join(date_parts)})"

            # Search for PMIDs
            search_result = self._esearch(query, retmax=max_results)
            pmids = search_result.get("esearchresult", {}).get("idlist", [])

            if not pmids:
                print(f"No results found for query: {self.query}")
                return []

            print(f"Found {len(pmids)} papers")

            # Get summaries
            time.sleep(0.5)  # Rate limiting
            summary_result = self._esummary(pmids)

            papers = []
            for pmid, paper_data in summary_result.get("result", {}).items():
                if pmid == "uids":
                    continue

                # Extract citation counts (requires additional call)
                citations = self._get_citation_count(pmid)

                paper = {
                    "pmid": pmid,
                    "title": paper_data.get("title", ""),
                    "authors": [a.get("name", "") for a in paper_data.get("authors", [])[:10]],
                    "journal": paper_data.get("source", ""),
                    "pubdate": paper_data.get("pubdate", ""),
                    "citation_count": citations,
                    "doi": paper_data.get("els", [""])[0] if paper_data.get("els") else ""
                }
                papers.append(paper)

            # Sort by citation count (desc)
            papers.sort(key=lambda x: x.get("citation_count", 0), reverse=True)

            self.results["data"]["papers"] = papers
            self.results["data"]["total_count"] = len(pmids)
            print(f"✓ Retrieved {len(papers)} paper summaries")
            return papers

        except Exception as e:
            print(f"✗ PubMed search error: {e}")
            return []

    def _get_citation_count(self, pmid: str) -> int:
        """Get citation count for a paper (using PubMed Central if available)."""
        try:
            # This is a simplified approach - for real use, consider using
            # Europe PMC API or other citation databases
            url = f"https://www.ncbi.nlm.nih.gov/pmc/utils/ctxp/PMCID:{pmid}"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                # Parse citation count from response
                data = response.json()
                return data.get("record", {}).get("citationcount", 0)
        except:
            pass
        return 0

    def analyze_trends(self, years: int = 5) -> Dict[str, Any]:
        """Analyze publication trends over time."""
        try:
            current_year = datetime.now().year
            yearly_counts = {}

            for year in range(current_year - years, current_year + 1):
                date_query = f"{self.query} AND {year}[Date - Publication] : {year}[Date - Publication]"
                search_result = self._esearch(date_query, retmax=1)
                count = int(search_result.get("esearchresult", {}).get("count", 0))
                yearly_counts[year] = count
                time.sleep(0.34)  # Rate limiting (3 requests per second)

            # Calculate growth rate
            years_list = sorted(yearly_counts.keys())
            if len(years_list) >= 2:
                first_year_count = yearly_counts[years_list[0]]
                last_year_count = yearly_counts[years_list[-1]]
                growth_rate = ((last_year_count - first_year_count) / first_year_count * 100) if first_year_count > 0 else 0
            else:
                growth_rate = 0

            trend_data = {
                "yearly_counts": yearly_counts,
                "total_papers": sum(yearly_counts.values()),
                "average_per_year": sum(yearly_counts.values()) / len(yearly_counts) if yearly_counts else 0,
                "growth_rate_percent": round(growth_rate, 1),
                "trend": "increasing" if growth_rate > 10 else "stable" if growth_rate > -10 else "decreasing"
            }

            self.results["data"]["trends"] = trend_data
            print(f"✓ Analyzed trends over {years} years")
            return trend_data

        except Exception as e:
            print(f"✗ Trend analysis error: {e}")
            return {}

    def get_top_papers(self, n: int = 20) -> List[Dict[str, Any]]:
        """Get top N papers by citation count."""
        papers = self.results.get("data", {}).get("papers", [])
        return papers[:n]

    def extract_keywords(self) -> List[str]:
        """Extract frequently occurring keywords from titles."""
        papers = self.results.get("data", {}).get("papers", [])

        word_freq = {}
        stop_words = {"and", "or", "the", "of", "in", "for", "with", "a", "an", "to", "from"}

        for paper in papers:
            title = paper.get("title", "").lower()
            words = title.split()
            for word in words:
                word = word.strip(".,;:!?-()")
                if len(word) > 3 and word not in stop_words:
                    word_freq[word] = word_freq.get(word, 0) + 1

        # Sort by frequency
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return [word for word, count in sorted_words[:30]]

    def fetch_all(self, start_date: Optional[str] = None, end_date: Optional[str] = None,
                  max_results: int = 100, analyze_trends: bool = False,
                  trend_years: int = 5) -> Dict[str, Any]:
        """Perform complete search and analysis."""
        print(f"\nSearching PubMed for: {self.query}\n")

        self.search(start_date=start_date, end_date=end_date, max_results=max_results)

        if analyze_trends:
            self.analyze_trends(years=trend_years)

        # Extract keywords
        if self.results.get("data", {}).get("papers"):
            keywords = self.extract_keywords()
            self.results["data"]["top_keywords"] = keywords

        return self.results

    def save(self, output: str):
        """Save results to file."""
        with open(output, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"\n✓ Results saved to {output}")


def main():
    parser = argparse.ArgumentParser(description="Search PubMed literature")
    parser.add_argument("query", help="Search query (e.g., 'EGFR resistance', 'KRAS G12C')")
    parser.add_argument("-o", "--output", default="pubmed_results.json", help="Output file path")
    parser.add_argument("--start", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", help="End date (YYYY-MM-DD)")
    parser.add_argument("--max", type=int, default=100, help="Maximum results")
    parser.add_argument("--trend", action="store_true", help="Analyze trends")
    parser.add_argument("--years", type=int, default=5, help="Years for trend analysis")
    parser.add_argument("--full-text", action="store_true", help="Include full-text abstracts")
    parser.add_argument("--format", choices=["json", "summary"], default="json", help="Output format")

    args = parser.parse_args()

    searcher = PubMedSearcher(args.query)

    searcher.fetch_all(
        start_date=args.start,
        end_date=args.end,
        max_results=args.max,
        analyze_trends=args.trend,
        trend_years=args.years
    )

    if args.format == "summary":
        print_summary(searcher.results)
    else:
        searcher.save(args.output)


def print_summary(data: Dict[str, Any]):
    """Print a summary of search results."""
    print("\n" + "="*70)
    print(f"LITERATURE SEARCH: {data['query'].upper()}")
    print("="*70 + "\n")

    # Basic stats
    total_count = data.get("data", {}).get("total_count", 0)
    print(f"Total Papers: {total_count}\n")

    # Trends
    if "trends" in data.get("data", {}):
        trends = data["data"]["trends"]
        print(f"Publication Trends ({len(trends.get('yearly_counts', {}))} years):")
        print(f"  Total: {trends.get('total_papers', 0)} papers")
        print(f"  Average: {trends.get('average_per_year', 0):.0f} papers/year")
        print(f"  Growth Rate: {trends.get('growth_rate_percent', 0)}%")
        print(f"  Trend: {trends.get('trend', 'unknown').title()}\n")

        yearly = trends.get("yearly_counts", {})
        if yearly:
            print(f"  Yearly Breakdown:")
            for year, count in sorted(yearly.items()):
                print(f"    {year}: {count} papers")
        print()

    # Top papers
    papers = data.get("data", {}).get("papers", [])
    if papers:
        print(f"Top {min(10, len(papers))} Papers by Citations:\n")
        for i, paper in enumerate(papers[:10], 1):
            print(f"  {i}. {paper.get('title', 'N/A')[:70]}...")
            print(f"     {paper.get('journal', 'N/A')} | {paper.get('pubdate', 'N/A')} | "
                  f"Citations: {paper.get('citation_count', 0)}")
            print()

    # Keywords
    keywords = data.get("data", {}).get("top_keywords", [])
    if keywords:
        print(f"Top Keywords:")
        print(f"  {', '.join(keywords[:15])}\n")

    print("="*70 + "\n")


if __name__ == "__main__":
    main()
