# Report Templates Reference

Reference guide for all report templates in the drug discovery skills.

## Template Overview

| Template | File | Purpose | Output Format |
|----------|------|---------|--------------|
| Target Dossier | target-dossier.md | Target validation report | PDF/Markdown |
| Competitor Brief | competitor-brief.md | Competitive intelligence | PPT/Markdown |
| Go/No-Go | go-no-go.md | Investment decision | PDF/Markdown |
| Weekly Update | weekly-update.md | Team intelligence | Email/Markdown |

## Template Variables

### Common Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{ date }}` | Report generation date | 2024-01-15 |
| `{{ query }}` | Search query/topic | EGFR |
| `{{ target_name }}` | Target gene symbol | EGFR |
| `{{ topic }}` | Report topic | EGFR inhibitors |
| `{{ project_name }}` | Project identifier | KRAS-G12C-001 |
| `{{ version }}` | Report version | 1.0.0 |

### Target Dossier Variables

| Category | Variables |
|----------|-----------|
| **Overview** | `gene_symbol`, `protein_name`, `uniprot_id`, `class`, `location` |
| **Druggability** | `tractability_score`, `development_level`, `summary` |
| **Diseases** | `disease_name`, `association_score`, `evidence` |
| **Pathways** | `primary_pathway`, `pathway_id`, `upstream`, `downstream` |
| **Competition** | `approved_drugs_count`, `pipeline_count`, `leading_companies` |
| **Safety** | `safety_tier`, `known_toxicities` |

### Competitor Brief Variables

| Category | Variables |
|----------|-----------|
| **Market** | `approved_count`, `pipeline_count`, `market_size`, `growth_rate` |
| **Products** | `product_name`, `company`, `year`, `type`, `status` |
| **Pipeline** | `phase_i_count`, `phase_ii_count`, `phase_iii_count` |
| **Companies** | `company_name`, `portfolio_strength`, `strategy` |
| **Opportunities** | `opportunity_name`, `rationale`, `stage` |

### Go/No-Go Variables

| Category | Variables |
|----------|-----------|
| **Scores** | `science_score`, `diff_score`, `feasibility_score`, `commercial_score`, `ip_safety_score` |
| **Status** | `science_status`, `diff_status`, `overall_score`, `recommendation` |
| **Details** | `strengths`, `concerns`, `evidence_summary`, `conditions` |
| **Decision** | `recommendation_uppercase`, `recommendation_detail`, `rationale` |

### Weekly Update Variables

| Category | Variables |
|----------|-----------|
| **Header** | `week_start`, `week_end`, `generated` |
| **Stats** | `clinical_deals_count`, `lit_count`, `deal_count` |
| **Highlights** | `highlight_title`, `highlight_summary`, `highlight_impact` |
| **Trials** | `nct`, `sponsor`, `phase`, `indication`, `notes` |
| **Alerts** | `alert_type`, `alert_message`, `alert_due` |

## Template Structure

### Target Dossier Structure

```markdown
# {{ target_name }} Target Dossier

## Executive Summary
{{ executive_summary }}

## Quick Stats
| Metric | Value |
|--------|-------|
| Gene | {{ gene_symbol }} |
| Tractability | {{ tractability_score }}/10 |
...

## 1. Target Overview
[Basic target information]

## 2. Druggability Assessment
[Tractability analysis]

## 3. Disease Associations
[Associated diseases with scores]

## 4. Pathway Context
[Pathway information]

## 5. Competitive Landscape
[Approved drugs and pipeline]

## 6. Safety Considerations
[Safety assessment]

## 7. Opportunities
[Key opportunities]

## 8. Risks
[Key risks]

## 9. Recommendations
[Actionable recommendations]
```

### Competitor Brief Structure

```markdown
# {{ topic }} - Competitive Intelligence Brief

## Executive Summary
{{ executive_summary }}

## Market Overview
[Market size, growth, key players]

## Approved Products
[Product comparison table]

## Pipeline Analysis
[Phase-by-phase breakdown]

## Company Landscape
[Key company profiles]

## Mechanism Analysis
[MOA classification]

## White Space Opportunities
[Unaddressed areas]

## Key Developments
[Recent events]

## Outlook
[Forward-looking analysis]
```

### Go/No-Go Structure

```markdown
# Go/No-Go Analysis: {{ project_name }}

## Overall Score: {{ overall_score }}/100

## Scorecard
[Dimension-by-dimension scores]

## Dimension Assessments
### 1. Scientific Rationale ({{ science_score }}/100)
[Detailed analysis]

### 2. Differentiation ({{ diff_score }}/100)
[Competitive positioning]

### 3. Feasibility ({{ feasibility_score }}/100)
[Technical assessment]

### 4. Commercial ({{ commercial_score }}/100)
[Market analysis]

### 5. IP/Safety ({{ ip_safety_score }}/100)
[IP and safety assessment]

## Conditions to Proceed
[Required conditions]

## Recommendation
[Go/No-Go decision with rationale]
```

### Weekly Update Structure

```markdown
# Weekly Intelligence Update

## This Week at a Glance
{{ weekly_summary }}

## Key Developments
[Clinical updates, literature, deals]

## Clinical Trials
[New and updated trials]

## Literature Highlights
[Key papers]

## Deals & Transactions
[Recent deals]

## Regulatory Updates
[Regulatory news]

## Alerts & Reminders
[Action items]
```

## Customization Guide

### Adding Custom Sections

1. **Define variable** in data fetching
2. **Add placeholder** in template: `{{ custom_variable }}`
3. **Populate** in script or Claude response

### Conditional Content

```markdown
{% if condition %}
This section appears when condition is true
{% endif %}
```

### Loops

```markdown
{% for item in items %}
- {{ item.name }}: {{ item.value }}
{% endfor %}
```

## Output Conversion

### Markdown to PDF

```bash
# Using weasyprint
weasyprint input.md output.pdf

# Using pandoc
pandoc input.md -o output.pdf
```

### Markdown to PPT

```python
from python_pptx import Presentation

def markdown_to_ppt(md_file, ppt_file):
    # Parse markdown and create slides
    # Implementation depends on structure
    pass
```

### Markdown to Email

```python
import markdown

def markdown_to_email(md_content):
    html = markdown.markdown(md_content)
    # Send as HTML email
    return html
```

## Template Best Practices

1. **Keep sections focused**: One topic per section
2. **Use tables for comparison**: Easy to scan
3. **Include executive summary**: Key insights upfront
4. **Add visual hierarchy**: Headers, bullets, bold text
5. **Limit length**: Target 2-3 pages max for briefs
6. **Include action items**: What should reader do?

## Template Maintenance

### Version Control
- Track template versions
- Document changes
- Archive old versions

### Update Schedule
| Template | Review Frequency | Update Trigger |
|----------|------------------|----------------|
| Target Dossier | Quarterly | New data sources |
| Competitor Brief | Monthly | Market changes |
| Go/No-Go | Annually | Framework updates |
| Weekly Update | As needed | Format changes |

### Quality Checks
- [ ] All variables have default values
- [ ] Tables render correctly
- [ ] Links are valid
- [ ] Formatting is consistent
- [ ] Examples are current

## Advanced Customization

### Custom Styles

```markdown
<style>
    .header { color: #003366; }
    .warning { color: #CC0000; }
    .success { color: #006600; }
</style>

# <div class="header">Custom Header</div>
```

### Dynamic Content

```python
# In Python script
from jinja2 import Template

template = Template(open('template.md').read())
rendered = template.render(
    target_name="EGFR",
    # ... other variables
)
```

### Conditional Formatting

```markdown
{% if score >= 80 %}
✅ **Strong Go** - Proceed with confidence
{% elif score >= 60 %}
⚠️ **Go with Conditions** - Address concerns
{% elif score >= 40 %}
⚠️ **Caution** - Re-evaluate
{% else %}
❌ **No-Go** - Do not proceed
{% endif %}
```
