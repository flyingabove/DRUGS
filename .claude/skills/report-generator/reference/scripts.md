# Report Generation Scripts Reference

Reference for report generation utility scripts.

## Script Overview

| Script | Purpose | Input | Output |
|--------|---------|-------|--------|
| generate_report.py | Main report generator | Report type, query | Formatted report |
| fetch_data.py | Data aggregation | Target/drug name | JSON data |
| format_converter.py | Format conversion | Markdown | PDF/PPT/HTML |

## Main Script: generate_report.py

### Usage

```bash
# Basic usage
python generate_report.py dossier EGFR

# With output file
python generate_report.py dossier EGFR -o reports/EGFR.pdf

# With format
python generate_report.py brief "EGFR inhibitors" --format ppt

# Go/No-Go analysis
python generate_report.py gng project-KRAS --format pdf

# Weekly report
python generate_report.py weekly --targets EGFR,KRAS,HER2
```

### Arguments

| Argument | Short | Required | Description |
|----------|-------|----------|-------------|
| report_type | - | Yes | dossier, brief, gng, weekly |
| query | - | Yes | Target name, drug, or topic |
| --output | -o | No | Output file path |
| --template | -t | No | Custom template name |
| --format | -f | No | markdown, pdf, ppt, html |
| --no-fetch | - | No | Skip data fetching |

### Examples

```bash
# Target dossier
python generate_report.py dossier EGFR \
  --format pdf \
  --output reports/EGFR-dossier.pdf

# Competitor brief
python generate_report.py brief "EGFR TKIs" \
  --format ppt \
  --template custom-competitor-brief

# Go/No-Go with custom scoring
python generate_report.py gng KRAS-G12C-001 \
  --format pdf \
  --weights science=30,commercial=25

# Weekly update
python generate_report.py weekly \
  --targets EGFR,KRAS,BRAF,ALK,ROS1 \
  --format email \
  --output weekly-update.html
```

## Python API

### ReportGenerator Class

```python
from report_generator.scripts.generate_report import ReportGenerator

# Initialize
generator = ReportGenerator(
    report_type="dossier",
    query="EGFR"
)

# Generate report
output = generator.generate(
    output_path="reports/EGFR.pdf",
    format="pdf"
)
print(f"Report saved to: {output}")
```

### Custom Report Generation

```python
from report_generator.scripts.generate_report import ReportGenerator
import json

# Custom data
custom_data = {
    "target": "EGFR",
    "scores": {
        "scientific": 85,
        "commercial": 78,
        "overall": 81
    },
    "recommendations": [
        "Proceed to Phase II",
        "Expand to NSCLC",
        "Explore combinations"
    ]
}

# Generate with custom data
generator = ReportGenerator("gng", "EGFR-project")
generator.results["data"] = custom_data

# Use custom template
output = generator.generate(
    template="custom-gng",
    output_path="custom-report.pdf"
)
```

### Batch Report Generation

```python
from report_generator.scripts.generate_report import ReportGenerator

targets = ["EGFR", "HER2", "HER3", "ALK", "ROS1"]

for target in targets:
    generator = ReportGenerator("dossier", target)
    output_path = f"reports/{target}-dossier.md"
    generator.generate(output_path=output_path)
    print(f"Generated: {output_path}")
```

## Data Fetching

### fetch_data.py

```python
from report_generator.scripts.fetch_data import fetch_all_data

# Fetch data for target
data = fetch_all_data(
    target="EGFR",
    sources=["opentargets", "uniprot", "chembl"],
    include_clinical=True
)

# Fetch competitor data
comp_data = fetch_competitor_data(
    query="EGFR inhibitors",
    include_pipeline=True,
    include_clinical_trials=True
)
```

## Format Conversion

### Markdown to PDF

```python
from report_generator.scripts.format_converter import MarkdownToPDF

converter = MarkdownToPDF()
converter.convert(
    input_path="report.md",
    output_path="report.pdf",
    css="styles/report.css"
)
```

### Markdown to PowerPoint

```python
from report_generator.scripts.format_converter import MarkdownToPPT

converter = MarkdownToPPT()
converter.convert(
    input_path="brief.md",
    output_path="brief.pptx",
    template="templates/brief-pptx.json"
)
```

## Template Variables Reference

### Target Dossier Variables

```python
{
    "target_name": "EGFR",
    "gene_symbol": "EGFR",
    "protein_name": "Epidermal growth factor receptor",
    "uniprot_id": "P00533",
    "chembl_id": "CHEMBL203",
    "length": 1210,
    "mass_kda": 134.3,
    "class": "Receptor tyrosine kinase",
    "location": "Cell membrane",
    "tractability_score": 8.2,
    "development_level": "Tclin",
    "disease_count": 142,
    "approved_drugs_count": 9,
    "pipeline_count": 34,
    "safety_tier": 2
}
```

### Go/No-Go Variables

```python
{
    "project_name": "KRAS-G12C-001",
    "overall_score": 72,
    "recommendation": "Go with Conditions",
    "science_score": 85,
    "science_weighted": 21.25,
    "science_status": "✅ Strong",
    "diff_score": 65,
    "feasibility_score": 75,
    "commercial_score": 80,
    "ip_safety_score": 50,
    "conditions": [
        "Conduct FTO analysis",
        "Early toxicity profiling",
        "Explore combination strategies"
    ]
}
```

## Error Handling

### Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `TemplateNotFound` | Template file missing | Check template path |
| `DataFetchError` | API failure | Check network, try alternative source |
| `RenderError` | Invalid template syntax | Validate template |
| `FormatError` | Conversion failed | Check format dependencies |

### Error Handling Example

```python
from report_generator.scripts.generate_report import ReportGenerator, ReportError

try:
    generator = ReportGenerator("dossier", "INVALID_TARGET")
    output = generator.generate()
except ReportError as e:
    print(f"Report generation failed: {e}")
    # Log error and notify
except Exception as e:
    print(f"Unexpected error: {e}")
    # Handle unexpected errors
```

## Configuration

### config.yaml

```yaml
# Report generation configuration

reports:
  output_dir: "./reports"
  default_format: "markdown"
  template_dir: "./templates"

data_sources:
  opentargets:
    enabled: true
    timeout: 30
  chembl:
    enabled: true
    timeout: 30
  pubmed:
    enabled: true
    timeout: 30
    api_key: null

formats:
  pdf:
    engine: "weasyprint"
    css: "styles/report.css"
  ppt:
    template: "templates/ppt-template.json"
  html:
    css: "styles/report.css"

logging:
  level: "INFO"
  file: "reports/generation.log"
```

### Loading Configuration

```python
import yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

generator = ReportGenerator("dossier", "EGFR", config=config)
```

## Advanced Features

### Custom Scoring Weights

```python
# Custom Go/No-Go weights
weights = {
    "scientific": 30,      # Default 25%
    "differentiation": 25,  # Default 20%
    "feasibility": 15,      # Default 20%
    "commercial": 20,       # Default 20%
    "ip_safety": 10         # Default 15%
}

generator = ReportGenerator("gng", "project-name")
generator.set_weights(weights)
output = generator.generate()
```

### Conditional Sections

```python
# Add sections based on data
if data.get("approved_drugs_count", 0) > 0:
    generator.add_section("competition")
    generator.add_section("differentiation")

if data.get("clinical_trials", 0) > 10:
    generator.add_section("trial_analysis")
```

### Report Comparison

```python
# Compare two reports
from report_generator.scripts.compare import compare_reports

diff = compare_reports(
    "reports/EGFR-v1.pdf",
    "reports/EGFR-v2.pdf"
)

print(f"Changes: {diff['summary']}")
```

## Best Practices

1. **Validate inputs**: Check target names, drug names
2. **Handle errors gracefully**: Provide fallbacks
3. **Log operations**: Track report generation
4. **Cache data**: Avoid repeated API calls
5. **Version reports**: Track report versions
6. **Test templates**: Verify with sample data
7. **Document customizations**: Keep notes on changes

## Troubleshooting

### Debug Mode

```bash
# Enable debug output
python generate_report.py dossier EGFR --debug
```

### Template Validation

```python
from report_generator.scripts.validate import validate_template

errors = validate_template("templates/custom.md")
if errors:
    print("Template errors:")
    for error in errors:
        print(f"  - {error}")
```

### Data Inspection

```python
# Inspect fetched data
from report_generator.scripts.fetch_data import fetch_all_data
import json

data = fetch_all_data("EGFR")
print(json.dumps(data, indent=2))
```
