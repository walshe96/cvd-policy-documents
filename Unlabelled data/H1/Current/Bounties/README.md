# Dataset Card for CVD Policy Documents, Unlabelled data, H1, Bounties

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

This dataset provides the current bounty offerings for bug bounty programmes the use HackerOne.

### Supported Tasks and Leaderboards

There are currently no supported tasks for this dataset. 

### Languages

Underlying text is predomnantly in English, but may contain passages of text in other languages. 

## Dataset Structure

### Data Instances

There are 379 entries containing information or comments on the bounties offered by programmes.

### Data Fields

The fields are as follows:

| Field      | Data type | Description |
| ----------- | ----------- | ----------- |
| Name | String | Name of the operating organisation |
| Timestamp | Timestamp | Date and time of issue |
| Domain | String | Either empty or comment |
| Low | String | Monetary value of low severity bounties |
| Medium | String | Monetary value of medium severity bounties |
| High | String | Monetary value of high severity bounties |
| Critical | String | Monetary value of critical severity bounties |
| Content | String | Any comments that may be present in the bounty tables |


## Dataset Creation

### Curation Rationale
Although not directly used in the study, it is hoped that the data will be of use to researchers in the future.

### Source Data

#### Initial Data Collection and Normalization

The bounty data was collected from during April 2022.

### Social Impact of Dataset
As the dataset contains no annotations, the usability outside of the current task may be limited. 


### Discussion of Biases

The biases for the dataset are as follows:

1. The content is applicable only to HackerOne.
2. Bounty values are applicable only for the time of collection.

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
