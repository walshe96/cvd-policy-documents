# Dataset Card for CVD Policy Documents, Unlabelled data, External programs, Policies

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage: N/A**
- **Repository: [cvd-policy-documents](https://github.com/walshe96/cvd-policy-documents)**
- **Paper: Towards a greater understanding of Coordinated Vulnerability Disclosure policy documents (under review)**
- **Leaderboard: N/A**
- **Point of Contact: Raise issue in repo**

### Dataset Summary

This dataset provides 3,390 CVD policies for organisations that operate a stand-alone CVD programme (note that some are blank)

### Supported Tasks and Leaderboards

There are currently no supported tasks for this dataset. 

### Languages

Underlying text is predomnantly in English, but may contain passages of text in other languages. 

## Dataset Structure

### Data Instances

There are 3,390 policies, of which 81 are empty.

### Data Fields

The fields are as follows:

| Field      | Data type | Description |
| ----------- | ----------- | ----------- |
| Name | String | Name of the operating organisation |
| URL | String | Link to the source of the policy |
| Concept | String | Policy text |

## Dataset Creation

### Curation Rationale

In order to investigate the contents of CVD policy documents, it was neccessary to understand the information conveyed by stand-alone programmes.

### Source Data

#### Initial Data Collection and Normalization

The stand-alone policy data was collected from HackerOne's repository of external programes during April 2022.

### Social Impact of Dataset
As the dataset contains no annotations, the usability outside of the current task may be limited. 


### Discussion of Biases

The biases for the dataset are as follows:

1. Content is almost entirely in the English language.
2. There is a geographic bias towards U.S. based organisations, and somewhat of a bias towards European organisations. Data from a limited number of non-Western organisations is present.
3. HackerOne's repository of external programmes is used as the source of stand-alone programmes. There may be stand-alone programmes that exist, but are not included on the list.

### Other Known Limitations

The limitations for the dataset are as follows:

1. The underlying data was collected in April 2022 and may not reflect the current state of CVD programmes.

## Additional Information

### Dataset Curators

To be updated in the future.

### Licensing Information

To be updated in the future.

### Citation Information

To be updated in the future.
