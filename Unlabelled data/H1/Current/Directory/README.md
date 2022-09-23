# Dataset Card for CVD Policy Documents, Unlabelled data, H1, Current, Directory

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

This dataset provides the current directory information for bug bounty programmes that use HackerOne.

### Supported Tasks and Leaderboards

There are currently no supported tasks for this dataset. 

### Languages

Underlying text is predomnantly in English, but may contain passages of text in other languages. 

## Dataset Structure

### Data Instances

There are 526 directory entries.

### Data Fields

The fields are as follows (note that some columns are duplicate):

| Field      | Data type | Description |
| ----------- | ----------- | ----------- |
| Name | String | Name of the operating organisation |
| URL | String | URL of the programme page |
| Badges | List of strings | Badges used to describe the programme |
| Launch | Date (YYYY-MM-DD) | Date of programme launch |
| Reports | Integer | Number of reports resolved |
| MinBounty | List of integers | Minimum bounty, or bounty range, offered for valid reports |
| AvgBounty | List of integers | Average bounty, or bounty range, offered for valid reports  |
| Type | String | Either bug bounty or responsible disclosure |
| Updates | Integer | Number of updates published by the programme operators |
| RewardURL | String | URL for the rewards page |
| PolicyURL | String | URL for the policy page |
| ScopeURL | String | URL for the scope page |
| FirstResponseTime | String | Average time to first response |
| TriageTime | String | Average time to triage |
| BountyTime | String | Average time to bounty |
| ResolutionTime | String | Average time to resolution |
| MeetStandards | String | Percent of responses that meet HackerOne's standards |
| BountyMin | List of integers | Minimum bounty, or bounty range, offered for valid reports |
| BountyTotal | List of integers | Total bounty, or estimated total, offered for all reports |
| BountyAverage | List of integers | Average bounty, or bounty range, offered for valid reports |
| BountyTop | List of integers | Top bounties, or bounty range, offered for valid reports |
| Bounty90Days | List of integers | Total bounty, or estimated total, offered in the last 90 days |
| Reports90Days | Integer | Number of reports resolved in the last 90 days |
| ReportsLast | String | Last report resolved |
| ReportsTotal | Integer | Total number of reports resolved |
| HackersThanked | Integer | Number of hackers thanked |
| RewardUpdatedURL | String | URL for the rewards page |
| ScopeUpdatedURL | String | URL for the policy page |


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
2. Directory informatio is only applicable for the time of collection.

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
