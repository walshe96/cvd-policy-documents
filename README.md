# Purpose
This repository contains the datasets and models published alongside the paper "Towards a greater understanding of Coordinated Vulnerability Disclosure policy documents" (currently under review). It is hoped that by publishing the associated files, replicability of the findings can be achieved. 

Much of the data in the repository remains un-analysed, as it falls outside of the immediate scope of the paper. Further investigation may allow researchers to gain a greater understanding of the current state of CVD programmes (data collected in April 2022).


# Organisation
The repository is organised as follows:

1. Annotated data - Annotated entity spans and multi-class categories used for model creation and evaluation (contains dataset cards). 
2. Unlabelled data - A collection of all data obtained during the web scraping of bug bounty platforms and CVD programme pages (contains dataset cards).
3. Models - A spaCy Named Entity Recognition (NER) model and a spaCy multi-class classification model (contains model cards).
4. Utils - Scripts predominantly used for training and evaluation.
5. requirements.txt - Python environment requirements file (Python 3.8.13).

## Annotated data
Hand-labelled datasets are available for *NER* and *multi-class classification* downstream tasks. For the NER, over 12,000 unique sentences (representing 9.7% of the 123,440 sentence corpus) are annotated for 15 entity types (for further details see the dataset card). For the text classification, over 3,000 paragraphs (representing 7.6% of the 39,748 paragraph corpus) are annotated for 12 classes (for further details see the dataset card).

```
Annotated data
│
│   
└───Classification
│   │   README.md   (dataset card)
│   │   annotated_classification_dataset.spacy
│   
│
└───NER
    │   README.md   (dataset card)
    │   annotated_ner_dataset.spacy
```


## Unlabelled data
A broad corpus of unlabelled data is made available in order to encourage researchers to further explore CVD. Aside from raw text, tables of statistics and metrics for many bug bounty programmes are included. 

```
Unlabelled data
│   
│       
└───External programs/Policies
│   │   README.md   (dataset card)
│   │   standalone_programme_policy.pkl
│
│  
└───H1
│   │
│   │
│   └─── Current
│   │    │
│   │    │
│   │    └─── Bounties
│   │    │    │   README.md   (dataset card)
│   │    │    │   hackerone_current_programme_bounty.pkl
│   │    │
│   │    │
│   │    └─── Directory
│   │    │    │   README.md   (dataset card)
│   │    │    │   hackerone_current_directory.pkl
│   │    │
│   │    │
│   │    └─── Policies
│   │    │    │   README.md   (dataset card)
│   │    │    │   hackerone_current_programme_policy.pkl
│   │    │
│   │    │
│   │    └─── Scopes
│   │         │   README.md   (dataset card)
│   │         │   hackerone_current_programme_scope.pkl
│   │
│   │
│   └─── Version changes
│        │
│        │
│        └─── Bounties
│        │    │   README.md   (dataset card)
│        │    │   hackerone_version_changes_bounty.pkl
│        │
│        │
│        └─── Policies
│        │    │   README.md   (dataset card)
│        │    │   hackerone_version_changes_policy.pkl
│        │
│        │
│        └─── Scopes
│        │    │   README.md   (dataset card)
│        │    │   hackerone_version_changes_scope.pkl
│        │
│        │
│        └─── Updates
│             │   README.md   (dataset card)
│             │   hackerone_programme_updates.pkl
│
│
└───Other platforms/Policies
    │   README.md   (dataset card)
    │   platforms_other_programme_policy.pkl
```


## Models
Fine-tuned *NER* and *multi-class classification* downstream models are provided to allow for the direct replication of results, and for use in further analysis. Both models make use of the spaCy NLP library, please see the model cards for more details.

```
Models
│ 
│   
└───Classification
│   │   README.md   (model card)
│   │   model-classification
│   
│
└───NER
    │   README.md   (model card)
    │   model-ner
```


## Utils
A collection of Python functions and scripts are provided for convienience. 

```
Utils
│ 
│   
│   README.md
│   document_splitter.py
│   perform_inference.py
│   spacy_cross_validation.py
│   train.txt
```



Note 1: All dataset cards use the [Hugging Face dataset card](https://raw.githubusercontent.com/huggingface/datasets/main/templates/README.md) as a template 

Note 2: All model cards use the [Hugging Face model card](https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1) as a template
