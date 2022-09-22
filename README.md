# Purpose
This repository contains the datasets and models published alongside the paper "Towards a greater understanding of Coordinated Vulnerability Disclosure policy documents" (currently under review). It is hoped that by publishing the associated files, replicability of the findings can be achieved. 

Much of the data in the repository remains un-analysed, as it falls outside of the immediate scope of the paper. Further investigation may allow researchers to gain a greater understanding of the current state of CVD programmes (data collected in April 2022).


# Organisation
The repository is organised as follows:

1. Annotated data - Annotated entity spans and multi-class categories used for model creation and evaluation (contains dataset cards). 
2. Unlabelled data - A collection of all data obtained during the web scraping of bug bounty platforms and CVD programme pages (contains dataset cards).
3. Models - A spaCy Named Entity Recognition (NER) model and a spaCy multi-class classification model (contains model cards).
4. Utils - Scripts predominantly used for training and evaluation.
5. requirements.txt - Python environment requirements file.

## Annotated data
```
Annotated data
│
│   
└───Classification
│   │   README.md   (dataset card)
│   │
│   
│
└───NER
    │   README.md   (dataset card)
    │
```


## Unlabelled data
```
Unlabelled data
│   
│       
└───External programs/Policies
│   │   README.md   (dataset card)
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
│   │    │    │
│   │    │
│   │    │
│   │    └─── Directory
│   │    │    │   README.md   (dataset card)
│   │    │    │
│   │    │
│   │    │
│   │    └─── Policies
│   │    │    │   README.md   (dataset card)
│   │    │    │
│   │    │
│   │    │
│   │    └─── Scopes
│   │         │   README.md   (dataset card)
│   │         │
│   │
│   │
│   └─── Version changes
│        │
│        │
│        └─── Bounties
│        │    │   README.md   (dataset card)
│        │    │
│        │
│        │
│        └─── Policies
│        │    │   README.md   (dataset card)
│        │    │
│        │
│        │
│        └─── Scopes
│        │    │   README.md   (dataset card)
│        │    │
│        │
│        │
│        └─── Updates
│             │   README.md   (dataset card)
│             │
│
│
└───Other platforms/Policies
    │   README.md   (dataset card)
```


## Models
```
Models
│ 
│   
└───Classification
│   │   README.md   (model card)
│   │
│   
│
└───NER
    │   README.md   (model card)
    │
```


## Utils
```
Utils
│ 
│   
│   README.md
```







Note 1: All dataset cards use the [Hugging Face dataset card](https://raw.githubusercontent.com/huggingface/datasets/main/templates/README.md) as a template 

Note 2: All model cards use the [Hugging Face model card](https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1) as a template
