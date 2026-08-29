# FDA Resources for Clinical Intelligence

FDA databases and resources for clinical trial and drug development intelligence.

## Key FDA Resources

### Drugs@FDA

**URL**: https://www.accessdata.fda.gov/scripts/cder/daf/

Database of FDA-approved drug and biologic products.

**Data includes**:
- Product information (brand/generic names)
- Approval date and expedited review status
- Therapeutic equivalence evaluations
- Drug substance and firm information

**API access**: No public API, use FDA Data Dashboard

### FDA Adverse Event Reporting System (FAERS)

**URL**: https://fis.fda.gov/sense/app/d10be6bb-754d-4781-a0f4-1c96edd24917/

Public dashboard for adverse event data.

**Quarterly data files**: https://www.fda.gov/drugs/questions-and-answers-fdas-adverse-event-reporting-system-faers

**Fields**:
- Patient demographics
- Adverse event descriptions
- Drug information
- Reporter information
- Outcome data

### Purple Book

**URL**: https://purplebooksearch.fda.gov/purplebooksearch/

Database of licensed biological products.

**Data includes**:
- BLA submissions
- Biosimilar and interchangeability evaluations
- Reference product exclusivity

### Orange Book

**URL**: https://www.accessdata.fda.gov/scripts/cder/ob/

Approved drug products with therapeutic equivalence evaluations.

**Key fields**:
- Active ingredients
- Dosage form/route
- Patent/exclusivity information
- Therapeutic equivalence codes

### ClinicalTrials.gov (FDA-sponsored)

**URL**: https://clinicaltrials.gov/

Registry of clinical trials (not FDA-specific but includes FDA-regulated trials).

**FDA-specific filters**:
- `src=FDA` - FDA-sponsored trials
- Filter by FDA oversight

## FDA Breakthrough Therapy Designations

### Designation Types

| Designation | Criteria | Benefits |
|-------------|----------|----------|
| Fast Track | Serious condition + nonclinical/clinical data showing potential | Rolling review, frequent meetings |
| Breakthrough Therapy | Serious condition + preliminary clinical evidence showing substantial improvement | Intensive guidance, FDA involvement |
| Accelerated Approval | Serious condition + surrogate endpoint | Approval based on surrogate endpoint |
| Priority Review | Significant improvement vs standard | 6-month review vs 10-month standard |
| Orphan Drug | Rare disease (<200k US prevalence) | 7-year exclusivity, tax credits |

### Recent Breakthrough Therapy Designations (Oncology)

| Drug | Target | Indication | Designation Date |
|------|--------|------------|------------------|
| Osimertinib | EGFR T790M | NSCLC | 2015 |
| Sotorasib | KRAS G12C | NSCLC | 2021 |
| Adagrasib | KRAS G12C | NSCLC | 2022 |
| Amivantamab | EGFR/MET | NSCLC | 2021 |

## FDA Divisions

### Oncology Center of Excellence (OCE)

**Division of Oncology 1** - Solid tumors (lung, breast, GI)
**Division of Oncology 2** - Hematologic malignancies
**Division of Oncology 3** - Rare cancers, pediatric

### Project Orbis

**Description**: International collaboration for concurrent review
**Participating countries**: Australia, Brazil, Canada, Singapore, Switzerland, UK

**Benefits**:
- Simultaneous submissions
- Common review timelines
- Information sharing

## FDA Databases Access

### openFDA

**Base URL**: https://api.fda.gov/

**Endpoints**:

1. **Drug Product Labeling**
   ```
   https://api.fda.gov/drug/label.json?search=osimertinib
   ```

2. **Drug Adverse Events**
   ```
   https://api.fda.gov/drug/event.json?search=patient.drug.medicinalproduct:"osimertinib"
   ```

3. **Drug Enforcement Reports**
   ```
   https://api.fda.gov/drug/enforcement.json?search=report_date:[20200101 TO 20201231]
   ```

4. **Device Adverse Events**
   ```
   https://api.fda.gov/device/event.json?search=date_received:[20240101+TO+20241231]
   ```

### openFDA Query Syntax

#### Field Search
```
search=patient.drug.medicinalproduct:"tylenol"
```

#### Date Range
```
search=receive_date:[20200101+TO+20201231]
```

#### Count Aggregation
```
count=patient.reaction.reactionmeddrapt.exact
```

#### Exact Match
```
search=patient.drug.openfda.pharm_class_epc:"nonsteroidal+anti-inflammatory+drug"
```

## FDA Review Milestones

### Standard Review Timeline

| Milestone | Timeline (Days) |
|-----------|-----------------|
| Submission | Day 0 |
| 30-Day Meeting | Day 30 |
| File Acceptance | Day 60 |
| Mid-Cycle Meeting | Day 180 (standard), Day 90 (priority) |
| Action Letter | Day 180 (priority), Day 300 (standard) |

### Accelerated Approval Pathway

**Submit**: Initial NDA/BLA
**Submit**: Accelerated approval request
**Meeting**: Pre-submission (Day -60)
**Submit**: NDA/BLA with surrogate endpoint
**Review**: 6-month priority review
**Approval**: Based on surrogate endpoint
**Post-Marketing**: Confirmatory trials required

## Integration with Clinical Trial Analysis

### FDA Approval → Clinical Trial Mapping

```python
# For a given drug, find pivotal trials
1. Search Drugs@FDA for NDA/BLA number
2. Extract review documents
3. Find referenced clinical trials
4. Map to ClinicalTrials.gov NCT IDs
5. Extract trial design and outcomes
```

### Clinical Trial → FDA Approval Prediction

**Signals for likely approval**:
- Fast Track/Breakthrough designation
- Positive Phase 3 results
- Advisory committee recommendation
- FDA safety review completion

**Red flags**:
- Complete Response Letter (CRL)
- Safety concerns raised
- Advisory committee negative vote
- Competitor approval first

## Additional Resources

| Resource | URL | Coverage |
|----------|-----|----------|
| FDA Drug Databases | https://www.fda.gov/drugs/drug-approvals-and-databases | All drug approvals |
| FDA News Feed | https://www.fda.gov/about-fda/contact-fda | Press releases |
| FDA Advisory Committees | https://www.fda.gov/about-fda/advisory-committee | Meeting materials |
| FDA Drug Shortages | https://www.fda.gov/drugs/drug-safety-and-availability/drug-shortages | Supply status |
| FDA Orange Book | https://www.accessdata.fda.gov/scripts/cder/ob/ | Patent/expiry |
