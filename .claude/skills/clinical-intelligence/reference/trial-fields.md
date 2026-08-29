# ClinicalTrials.gov Field Reference

Detailed field reference for ClinicalTrials.gov API responses.

## Study Identification

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| NCTId | string | ClinicalTrials.gov identifier | NCT03704547 |
| BriefTitle | string | Brief study title | "A Study of Osimertinib in EGFR Mutated NSCLC" |
| OfficialTitle | string | Official full title | Full protocol title |
| Acronym | string | Study acronym (optional) | "FLAURA" |

## Status Module

| Field | Type | Description |
|-------|------|-------------|
| OverallStatus | string | Study status (Recruiting, Active, Completed, etc.) |
| StartDateStruct | object | Start date with date type |
| PrimaryCompletionDateStruct | object | Primary completion date |
| CompletionDateStruct | object | Study completion date |
| LastUpdatePostDate | string | Last posted date |
| StudyFirstSubmitDate | string | First submission date |

### Status Values

- **Recruiting** - Currently enrolling participants
- **Not yet recruiting** - Not open for participant recruitment
- **Active, not recruiting** - Ongoing but not enrolling
- **Completed** - Study concluded
- **Suspended** - Study halted temporarily
- **Terminated** - Study stopped prematurely
- **Withdrawn** - Study withdrawn before enrollment
- **Available** - Expanded access available
- **No longer available** - Expanded access no longer available
- **Approved for marketing** - Drug approved
- **Enrolling by invitation** - Enrollment by invitation only

## Design Module

| Field | Type | Description |
|-------|------|-------------|
| StudyType | string | Interventional, Observational, etc. |
| PhaseList | array | Study phases (PHASE1, PHASE2, PHASE3, PHASE4, N/A) |
| DesignInfo | object | Study design details |
| PrimaryPurpose | string | Treatment, Prevention, Diagnostic, etc. |
| InterventionList | array | Study interventions |
| ArmGroupList | array | Study arms/groups |

### Study Types

- **Interventional** - Clinical trials with assigned interventions
- **Observational** - Observational studies without intervention assignment
- **Patient Registry** - Patient registry studies
- **Patient Prospective** - Prospective observational studies

### Phases

| Phase | Description |
|-------|-------------|
| PHASE1 | Safety and dosage determination |
| PHASE2 | Efficacy and side effects |
| PHASE3 | Large-scale efficacy comparison |
| PHASE4 | Post-marketing studies |

## Interventions Module

### Intervention Structure

```json
{
  "InterventionType": "Drug",
  "InterventionName": "Osimertinib",
  "Description": "80 mg tablet orally once daily",
  "ArmGroupLabels": ["Experimental"],
  "DosageText": "80 mg QD",
  "Synonyms": ["Tagrisso", "AZD9291"]
}
```

### Intervention Types

- **Drug** - Pharmaceutical intervention
- **Biological** - Biological product
- **Device** - Medical device
- **Procedure** - Surgical/procedural intervention
- **Radiation** - Radiation therapy
- **Behavioral** - Behavioral intervention
- **Dietary Supplement** - Dietary supplement
- **Diagnostic Test** - Diagnostic test
- **Other** - Other intervention type

## Conditions Module

| Field | Type | Description |
|-------|------|-------------|
| Condition | string | Primary condition/disease |
| ConditionList | array | All conditions studied |

## Eligibility Module

| Field | Type | Description |
|-------|------|-------------|
| EligibilityModule.Population | string | Study population |
| Gender | string | All, Male, Female |
| MinimumAge | string | Minimum eligible age |
| MaximumAge | string | Maximum eligible age |
| HealthyVolunteers | string | Accepts healthy volunteers |
| InclusionCriteria | string | Inclusion criteria text |
| ExclusionCriteria | string | Exclusion criteria text |
| StudyPopulation | string | Study population description |

## Locations Module

| Field | Type | Description |
|-------|------|-------------|
| LocationFacility | string | Facility name |
| LocationCity | string | City |
| LocationState | string | State/province |
| LocationCountry | string | Country |
| LocationStatus | string | Recruitment status at location |
| CentralContact | object | Contact information |

## Outcomes Module

### Primary Outcome

```json
{
  "Measure": "Progression Free Survival",
  "TimeFrame": "From randomization to documented disease progression or death",
  "Description": "Assessed by RECIST 1.1 criteria"
}
```

### Secondary Outcome

```json
{
  "Measure": "Overall Survival",
  "TimeFrame": "From randomization to death from any cause",
  "Description": "Kaplan-Meier estimate"
}
```

## Results Module

| Module | Description |
|--------|-------------|
| ParticipantFlowModule | Participant flow/attrition |
| BaselineCharacteristicsModule | Baseline demographics |
| OutcomeMeasurementsModule | Primary/secondary endpoint results |
| AdverseEventsModule | Adverse event data |
| SeriousAdverseEventsModule | Serious adverse events |

## Sponsor/Collaborators

| Field | Type | Description |
|-------|------|-------------|
| LeadSponsor | object | Lead sponsor organization |
| Collaborator | array | Collaborating organizations |

### Sponsor Types

- **NIH** - National Institutes of Health
- **Other U.S. Federal Agency** - Other US government
- **Industry** - Pharmaceutical/biotech company
- **Individual** | Individual investigator
- **Other** - Academic, nonprofit, or other

## Contacts Module

| Field | Type | Description |
|-------|------|-------------|
| CentralContactName | string | Contact name |
| CentralContactPhone | string | Contact phone |
| CentralContactEmail | string | Contact email |
| CentralContactOrganization | string | Contact organization |

## API Query Examples

### Search by Condition

```
https://clinicaltrials.gov/api/query/study_fields?
expr="lung cancer"[Condition]&
fields=NCTId,BriefTitle,OverallStatus,Phase&
min_rnk=1&max_rnk=50&fmt=json
```

### Search by Intervention

```
https://clinicaltrials.gov/api/query/study_fields?
expr="osimertinib"[Intervention]&
fields=NCTId,BriefTitle,Phase,Status&
fmt=json
```

### Get Full Study

```
https://clinicaltrials.gov/api/query/full_studies?
expr=NCT03704547[NCTId]&
min_rnk=1&max_rnk=1&
fmt=json
```

## Best Practices

1. **Use study_fields for searches** - Faster than full_studies
2. **Request only needed fields** - Reduces response size
3. **Handle missing data** - Not all fields populated
4. **Parse dates carefully** - Date structures can be complex
5. **Check status values** - Multiple status-related fields exist
