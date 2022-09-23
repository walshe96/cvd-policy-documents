# Dataset Card for CVD Policy Documents, Annotated data, Classification

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

This dataset provides over 3,000 annotated paragraphs using 12 CVD specific categories that consider the formal and informal constraints imposed upon participants (hackers).

### Supported Tasks and Leaderboards

This dataset is only suitable for multi-class classification. 

### Languages

Underlying text is predomnantly in English, but may contain passages of text in other languages. 

## Dataset Structure

### Data Instances

There are 3,003 paragraphs within the dataset, of which 955 belong to none of the pre-defined categories. The distribution of tags is as follows:

| Class      | Count |
| ----------- | ----------- |
| COMPANY-STATEMENT | 622 | 
| REWARD-EVALUATION | 466 | 
| SCOPE-IN | 284 | 
| VULN-ELIGIBLE | 219 | 
| VULN-INELIGIBLE | 211 | 
| PROHIBITED-ACTIONS | 182 | 
| GUIDELINES-SUBMISSIONS | 174 | 
| SCOPE-OUT | 155 | 
| ENGAGEMENT | 119 | 
| GUIDELINES-DISCLOSURE | 77 | 
| LEGAL | 71 | 
| PARTICIPANT-RESTRICTIONS | 38 | 


### Data Fields

The dataset is provided a serialised [spaCy DocBin](https://spacy.io/api/docbin), this can either be read using the functions provided in [Utils](https://github.com/walshe96/cvd-policy-documents/tree/main/Utils) or the built in spaCy functions.

### Data Splits

The presented dataset is unified, additional scripts in [Utils](https://github.com/walshe96/cvd-policy-documents/tree/main/Utils) are provided to split the data.

## Dataset Creation

### Curation Rationale

In order to investigate the contents of CVD policy documents, it was neccessary to understand the information conveyed throughout the document in relation to the policy element taxonomy proposed by [Laszka et al.](https://link.springer.com/chapter/10.1007/978-3-662-58387-6_8)

### Source Data

#### Initial Data Collection and Normalization

Data was collected from bug bounty platforms and stand-alone CVD programmes during April 2022, a full list of sources can be obtained from the paper. From the collected content, a random sample of paragraphs (split documents) was selected for annotation. 

### Annotations

#### Annotation process

A research license of Explosion.ai's [Prodigy](https://prodi.gy) annotation tool was obtained. The tool was subsequently used to perform manual text multi-classification. 

#### Who are the annotators?

The lead author of the paper performed all annotation. 

### Personal and Sensitive Information

To the knowledge of the authors, there is no personal or sentive information contained within the dataset.

## Considerations for Using the Data

### Social Impact of Dataset

As the purpose of the dataset is to allow for greater insights into the content of CVD policies, the social impact may be limited as it is not expected that the data will be used within any decision making system. 


### Discussion of Biases

The biases for the dataset are as follows:

1. Content is almost entirely in the English language.
2. There is a geographic bias towards U.S. based organisations, and somewhat of a bias towards European organisations. Data from a limited number of non-Western organisations is present.
3. As data for annotation was randomly selected over the corpus, it may not cover all possible sources of data (e.g., platform).

### Other Known Limitations

The limitations for the dataset are as follows:

1. The underlying data was collected in April 2022 and may not reflect the current state of CVD programmes.
2. The employment of a single annotator may introduce biases may be hard to identify as inter-coder agreement is not possible to measure.


## Additional Information

### Dataset Curators

To be updated in the future.

### Licensing Information

To be updated in the future.

### Citation Information

To be updated in the future.
