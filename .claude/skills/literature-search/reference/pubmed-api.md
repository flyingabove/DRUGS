# PubMed E-utilities API Reference

NCBI E-utilities for programmatic access to PubMed database.

## Base URL

```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils
```

## API Rate Limits

- **Without API Key**: 3 requests per second
- **With API Key**: 10 requests per second
- **Get API Key**: https://www.ncbi.nlm.nih.gov/account/

## Key E-utilities

### 1. ESearch - Search PubMed

Search for papers matching a query.

```
GET esearch.fcgi?db=pubmed&term={query}&retmax={count}
```

**Parameters:**
| Parameter | Required | Description |
|-----------|----------|-------------|
| `db` | Yes | Database name (pubmed) |
| `term` | Yes | Search query |
| `retmax` | No | Max results (default: 20) |
| `retmode` | No | Return mode (json) |
| `datetype` | No | Date type (pubdate) |
| `reldate` | No | Relative days (e.g., 365) |
| `mindate` | No | Minimum date (YYYY/MM/DD) |
| `maxdate` | No | Maximum date (YYYY/MM/DD) |

**Example:**
```bash
# Basic search
curl "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=EGFR+resistance&retmax=100&retmode=json"

# Date range search
curl "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=KRAS+G12C&mindate=2023/01/01&maxdate=2024/12/31&retmode=json"
```

**Response:**
```json
{
  "esearchresult": {
    "count": "847",
    "retmax": "100",
    "retstart": "0",
    "idlist": [
      "38123456",
      "38123455",
      ...
    ]
  }
}
```

### 2. ESummary - Get Article Summaries

Get summary information for PMIDs.

```
GET esummary.fcgi?db=pubmed&id={pmids}
```

**Parameters:**
| Parameter | Required | Description |
|-----------|----------|-------------|
| `db` | Yes | Database name (pubmed) |
| `id` | Yes | Comma-separated PMIDs |
| `retmode` | No | Return mode (json) |

**Example:**
```bash
curl "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=38123456,38123455&retmode=json"
```

**Response:**
```json
{
  "result": {
    "38123456": {
      "uid": "38123456",
      "title": "Osimertinib resistance mechanisms in NSCLC",
      "authors": [
        {"name": "Smith J"},
        {"name": "Johnson A"}
      ],
      "source": "Nat Med",
      "pubdate": "2023 Jun",
      "volume": "29",
      "issue": "6",
      "pages": "1234-45",
      "elocationid": "doi:10.1038/s41591-023-01234-5",
      "sorttitle": "osimertinib resistance",
      "lang": ["English"]
    }
  }
}
```

### 3. EFetch - Get Full Records

Get complete article data including abstracts.

```
GET efetch.fcgi?db=pubmed&id={pmids}&rettype=abstract
```

**Parameters:**
| Parameter | Required | Description |
|-----------|----------|-------------|
| `db` | Yes | Database name (pubmed) |
| `id` | Yes | Comma-separated PMIDs |
| `rettype` | No | Return type (abstract, medline) |
| `retmode` | No | Return mode (xml, text) |

**Example:**
```bash
curl "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=38123456&rettype=abstract&retmode=xml"
```

### 4. ELink - Find Related Articles

Find articles similar to a given article.

```
GET elink.fcgi?dbfrom=pubmed&db=pubmed&id={pmid}&cmd=neighbor_score
```

**Example:**
```bash
curl "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&db=pubmed&id=38123456&cmd=neighbor_score&retmode=json"
```

## Search Field Tags

| Tag | Field | Example |
|-----|-------|---------|
| `[Title]` | Title only | `cancer[Title]` |
| `[Abstract]` | Abstract only | `resistance[Abstract]` |
| `[MeSH]` | MeSH terms | `Carcinoma[MeSH]` |
| `[Author]` | Author name | `Smith J[Author]` |
| `[Journal]` | Journal name | `Nature[Journal]` |
| `[Date]` | Publication date | `2023[Date]` |
| `[PDAT]` | Publication date | `2023/01/01:2024/12/31[PDAT]` |

## Boolean Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `AND` | Both terms | `EGFR AND resistance` |
| `OR` | Either term | `TKI OR antibody` |
| `NOT` | Exclude term | `cancer NOT lung` |
| `*` | Wildcard | `resist*` |

## Date Queries

| Format | Description | Example |
|--------|-------------|---------|
| `YYYY[Date]` | Single year | `2023[Date]` |
| `YYYY/MM[Date]` | Single month | `2023/06[Date]` |
| `YYYY/MM/DD:YYYY/MM/DD[PDAT]` | Date range | `2023/01/01:2024/12/31[PDAT]` |
| `Nd[YEAR]` | Last N days | `365d[YEAR]` |

## Python Example

```python
import requests
import time

class PubMedClient:
    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
    API_KEY = None  # Set your NCBI API key here

    def __init__(self, api_key=None):
        self.api_key = api_key
        self.last_request_time = 0

    def _rate_limit(self):
        """Enforce rate limiting."""
        min_interval = 0.34 if self.api_key else 0.34  # 3 requests/sec
        elapsed = time.time() - self.last_request_time
        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)
        self.last_request_time = time.time()

    def search(self, query, max_results=100, date_range=None):
        """Search PubMed and return PMIDs."""
        url = f"{self.BASE_URL}/esearch.fcgi"
        params = {
            "db": "pubmed",
            "term": query,
            "retmax": max_results,
            "retmode": "json"
        }

        if date_range:
            params["datetype"] = "pubdate"
            params["mindate"] = date_range[0].replace("-", "/")
            params["maxdate"] = date_range[1].replace("-", "/")

        self._rate_limit()
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        return data["esearchresult"]["idlist"]

    def get_summaries(self, pmids):
        """Get article summaries."""
        url = f"{self.BASE_URL}/esummary.fcgi"
        params = {
            "db": "pubmed",
            "id": ",".join(pmids),
            "retmode": "json"
        }

        self._rate_limit()
        response = requests.get(url, params=params)
        response.raise_for_status()

        return response.json()

    def get_abstracts(self, pmids):
        """Get full abstracts."""
        url = f"{self.BASE_URL}/efetch.fcgi"
        params = {
            "db": "pubmed",
            "id": ",".join(pmids),
            "rettype": "abstract",
            "retmode": "xml"
        }

        self._rate_limit()
        response = requests.get(url, params=params)
        response.raise_for_status()

        return response.text

# Usage
client = PubMedClient()

# Search
pmids = client.search("EGFR resistance", max_results=50)
print(f"Found {len(pmids)} papers")

# Get summaries
summaries = client.get_summaries(pmids[:20])
for pmid, data in summaries["result"].items():
    if pmid != "uids":
        print(f"{pmid}: {data.get('title', 'N/A')}")
```

## Common Search Queries

| Goal | Query |
|------|-------|
| Drug resistance | `drug name AND resistance[Title/Abstract]` |
| Clinical trials | `disease AND clinical trial[Publication Type]` |
| Reviews only | `topic AND review[Publication Type]` |
| Recent papers | `topic AND 2023[PDAT]:3000[PDAT]` |
| Specific journal | `topic AND journal name[Journal]` |

## Best Practices

1. **Use specific terms**: Add MeSH terms for precision
2. **Limit results**: Use retmax to avoid large responses
3. **Rate limiting**: Always implement rate limiting
4. **Cache results**: PubMed data doesn't change frequently
5. **Use API key**: Register for higher rate limits
6. **Handle errors**: Check response status and handle failures

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| 429 | Rate limit exceeded | Slow down requests |
| 400 | Invalid parameters | Check query syntax |
| 500 | Server error | Retry with backoff |
| 404 | No results | Verify query terms |
