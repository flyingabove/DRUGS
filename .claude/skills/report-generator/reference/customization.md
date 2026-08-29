# Report Customization Guide

Guide for customizing and extending drug discovery reports.

## Customization Overview

| Aspect | Description | Complexity |
|--------|-------------|------------|
| Content variables | Dynamic data insertion | Beginner |
| Template styling | Visual appearance | Intermediate |
| Output formats | PDF, PPT, HTML | Intermediate |
| Custom sections | New content areas | Advanced |
| Workflow integration | Automated generation | Advanced |

## Variable System

### Built-in Variables

Variables are enclosed in double braces: `{{ variable_name }}`

**Categories:**

```python
# Target Data
target_name = "EGFR"
gene_symbol = "EGFR"
protein_name = "Epidermal growth factor receptor"
uniprot_id = "P00533"
chembl_id = "CHEMBL203"

# Druggability
tractability_score = 8.2
development_level = "Tclin"
tdl = "Clinical precedence"

# Competition
approved_count = 9
pipeline_count = 34

# Scores
science_score = 75
diff_score = 65
overall_score = 70
```

### Custom Variables

Define custom variables for your specific needs:

```python
# In your script
custom_vars = {
    "company_name": "Your Company",
    "confidential": "CONFIDENTIAL",
    "project_code": "PROJ-001",
    "review_date": "2024-01-15",
    "reviewer": "Dr. Jane Smith"
}
```

## Content Customization

### Adding Executive Summary

```markdown
## Executive Summary

{{ executive_summary }}

**Key Highlights:**
{% for highlight in highlights %}
- {{ highlight }}
{% endfor %}

**Bottom Line:** {{ bottom_line }}
```

### Adding SWOT Analysis

```markdown
## SWOT Analysis

| Strengths | Weaknesses |
|-----------|------------|
{% for s in strengths %}
| {{ s }} | |
{% endfor %}
{% for w in weaknesses %}
| | {{ w }} |
{% endfor %}

| Opportunities | Threats |
|---------------|---------|
{% for o in opportunities %}
| {{ o }} | |
{% endfor %}
{% for t in threats %}
| | {{ t }} |
{% endfor %}
```

### Adding Decision Matrix

```markdown
## Decision Matrix

| Criterion | Weight | Score | Weighted |
|-----------|--------|-------|----------|
{% for criterion in criteria %}
| {{ criterion.name }} | {{ criterion.weight }}% | {{ criterion.score }}/10 | {{ criterion.weighted }} |
{% endfor %}
| **Total** | **100%** | - | **{{ total_score }}** |

**Recommendation:** {{ recommendation }}
```

## Styling Customization

### Markdown Styling

```markdown
# Main Header

## Sub Header

### Sub-sub Header

**Bold text**
*Italic text*
`Code text`

> Blockquote for important notes

---

Horizontal separator

| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |

- Bullet point
  - Nested bullet

1. Numbered list
2. Another item

[Link text](https://example.com)

![Image alt](image.png)
```

### CSS for PDF/HTML

```css
/* Custom styles for reports */

.header {
    color: #1a5490;
    border-bottom: 2px solid #1a5490;
    padding-bottom: 10px;
}

.warning {
    background-color: #fff3cd;
    border-left: 4px solid #ffc107;
    padding: 10px;
    margin: 10px 0;
}

.score-high {
    color: #28a745;
    font-weight: bold;
}

.score-medium {
    color: #ffc107;
    font-weight: bold;
}

.score-low {
    color: #dc3545;
    font-weight: bold;
}

table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #dee2e6;
    padding: 8px;
    text-align: left;
}

th {
    background-color: #f8f9fa;
}
```

## Format-Specific Customization

### PDF Output

**Using WeasyPrint:**
```python
from weasyprint import HTML

def markdown_to_pdf(md_content, output_path):
    # Convert markdown to HTML
    import markdown
    html = markdown.markdown(md_content)

    # Add CSS
    html_with_style = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial; }}
            h1 {{ color: #1a5490; }}
        </style>
    </head>
    <body>{html}</body>
    </html>
    """

    # Generate PDF
    HTML(string=html_with_style).write_pdf(output_path)
```

**Using Pandoc:**
```bash
pandoc report.md -o report.pdf \
  --pdf-engine=xelatex \
  --variable=colorlinks=true \
  --variable=linkcolor=blue \
  --template=custom.tex
```

### PowerPoint Output

```python
from python_pptx import Presentation
from python_pptx.util import Inches, Pt

def create_ppt_report(data, output_path):
    prs = Presentation()

    # Title slide
    title_slide = prs.slides.add_slide(prs.slide_layouts[0])
    title = title_slide.shapes.title
    subtitle = title_slide.placeholders[1]
    title.text = data["title"]
    subtitle.text = data["subtitle"]

    # Content slides
    for section in data["sections"]:
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        shapes = slide.shapes
        shapes.title.text = section["title"]
        body = shapes.placeholders[1].text_frame
        body.text = section["content"]

    prs.save(output_path)
```

### Excel Output

```python
import pandas as pd

def create_excel_report(data, output_path):
    with pd.ExcelWriter(output_path) as writer:
        # Summary sheet
        pd.DataFrame([data["summary"]]).to_excel(
            writer, sheet_name="Summary", index=False
        )

        # Scores sheet
        pd.DataFrame(data["scores"]).to_excel(
            writer, sheet_name="Scores", index=False
        )

        # Competition sheet
        pd.DataFrame(data["competition"]).to_excel(
            writer, sheet_name="Competition", index=False
        )
```

## Advanced Customization

### Conditional Content

```markdown
{% if approved_drugs|length > 0 %}
## Approved Drugs
{% for drug in approved_drugs %}
- {{ drug.name }} ({{ drug.company }})
{% endfor %}
{% else %}
*No approved drugs identified*
{% endif %}
```

### Loops and Iteration

```markdown
## Detailed Analysis

{% for target in targets %}
### {{ target.name }}

**Tractability:** {{ target.tractability }}/10
**Diseases:** {{ target.diseases|join(", ") }}

{% if target.associations|length > 5 %}
Top associations:
{% for assoc in target.associations[:5] %}
- {{ assoc.disease }} ({{ assoc.score }})
{% endfor %}
{% endif %}

---

{% endfor %}
```

### Filters and Transformations

```markdown
{{ text|upper }}
{{ number|round(2) }}
{{ list|join(", ") }}
{{ value|default("N/A") }}
{{ date|strftime("%Y-%m-%d") }}
```

## Template Inheritance

### Base Template

```markdown
{# base.md #}
# {{ title }}

**Generated:** {{ date }} | **Version:** {{ version }}

---

{% block content %}{% endblock %}

---

*Report generated by Drug Discovery Skills*
```

### Child Template

```markdown
{# target-report.md #}
{% extends "base.md" %}

{% block content %}
## Target Analysis

{{ target_content }}

{% endblock %}
```

## Workflow Integration

### Automated Report Generation

```python
# reports/workflow.py

import asyncio
from pathlib import Path

class ReportWorkflow:
    def __init__(self, config):
        self.config = config
        self.templates_dir = Path("templates")

    async def generate_weekly_reports(self):
        """Generate all weekly reports."""
        targets = self.config.get("targets", [])

        for target in targets:
            # Fetch data
            data = await self.fetch_target_data(target)

            # Generate report
            report = self.generate_report(
                template="weekly-update",
                data=data,
                format="email"
            )

            # Send or save
            await self.deliver_report(report, target)

    def generate_report(self, template, data, format="markdown"):
        """Generate report from template."""
        template_path = self.templates_dir / f"{template}.md"
        template_content = template_path.read_text()

        # Render template
        from jinja2 import Template
        template = Template(template_content)
        rendered = template.render(**data)

        # Convert format
        if format == "pdf":
            return self.to_pdf(rendered)
        elif format == "ppt":
            return self.to_ppt(rendered)
        return rendered
```

### Scheduled Reports

```python
# Use APScheduler for scheduled generation
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

@scheduler.scheduled_job('cron', day_of_week='mon', hour=9)
def weekly_report_job():
    """Generate weekly reports every Monday at 9 AM."""
    workflow = ReportWorkflow(config)
    asyncio.run(workflow.generate_weekly_reports())

@scheduler.scheduled_job('cron', hour=0)
def daily_update_job():
    """Update data daily at midnight."""
    workflow = ReportWorkflow(config)
    asyncio.run(workflow.update_all_data())
```

## Custom Examples

### Custom Go/No-Go Template

```markdown
# Investment Decision: {{ project_name }}

## Decision: {% if overall_score >= 70 %}GO ✅{% else %}NO-GO ❌{% endif %}

**Score:** {{ overall_score }}/100
**Date:** {{ date }}
**Reviewed by:** {{ reviewer }}

---

## Score Breakdown

| Dimension | Weight | Score | Weighted | Status |
|-----------|--------|-------|----------|--------|
| Scientific | 25% | {{ science_score }}/100 | {{ science_weighted }} | {% if science_score >= 70 %}✅{% else %}⚠️{% endif %} |
| Differentiation | 20% | {{ diff_score }}/100 | {{ diff_weighted }} | {% if diff_score >= 70 %}✅{% else %}⚠️{% endif %} |
| Feasibility | 20% | {{ feas_score }}/100 | {{ feas_weighted }} | {% if feas_score >= 70 %}✅{% else %}⚠️{% endif %} |
| Commercial | 20% | {{ comm_score }}/100 | {{ comm_weighted }} | {% if comm_score >= 70 %}✅{% else %}⚠️{% endif %} |
| IP/Safety | 15% | {{ ip_score }}/100 | {{ ip_weighted }} | {% if ip_score >= 70 %}✅{% else %}⚠️{% endif %} |

---

## Rationale

{{ rationale }}

## Next Steps

{% if overall_score >= 70 %}
1. Proceed to due diligence
2. {{ next_step_1 }}
3. {{ next_step_2 }}
{% else %}
1. Address key concerns
2. Re-evaluate in 6 months
{% endif %}

---

*This decision is based on current information and should be revisited as new data becomes available.*
```

## Best Practices

1. **Keep templates simple**: Complex templates are hard to maintain
2. **Use defaults**: Always provide default values for variables
3. **Test outputs**: Verify rendering in all target formats
4. **Version control**: Track template changes
5. **Document variables**: Maintain a variable reference guide
6. **Modularize**: Use includes for reusable sections
7. **Validate data**: Check data quality before rendering
