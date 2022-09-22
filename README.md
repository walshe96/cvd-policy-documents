# Purpose
This repository contains the datasets and models published alongside the paper "Towards a greater understanding of Coordinated Vulnerability Disclosure policy documents" (currently under review). It is hoped that by publishing the associated files, replicability of the findings can be achieved. 

Much of the data in the repository remains un-analysed, as it falls outside of the immediate scope of the paper. Further investigation may allow researchers to gain a greater understanding of the current state of CVD programmes (data collected in April 2022).


# Organisation
The repository is organised as follows:

1. Annotated data - Annotated entity spans and multi-class categories used for model creation and evaluation (contains dataset cards). 
2. Unlabelled data - A collection of all data obtained during the web scraping of bug bounty platforms and CVD programme pages.
3. Models - A spaCy Named Entity Recognition (NER) model and a spaCy multi-class classification model (contains model cards).
4. Utils - Scripts predominantly used for training and evaluation.
5. requirements.txt - Python environment requirements file.

## Annotated data
```
Annotated data
│
│   
└───Classification
│   │   README.md
│   │
│   
│
└───NER
    │   README.md
    │
```


## Unlabelled data
```
Unlabelled data
│   
│       
└───External programs/Policies
│   │   README.md
│
│  
└───H1
│   │
│   │
│   └─── Current
│   │    │
│   │    │
│   │    └─── Bounties
│   │    │    │   README.md
│   │    │    │
│   │    │
│   │    │
│   │    └─── Directory
│   │    │    │   README.md
│   │    │    │
│   │    │
│   │    │
│   │    └─── Policies
│   │    │    │   README.md
│   │    │    │
│   │    │
│   │    │
│   │    └─── Scopes
│   │         │   README.md
│   │         │
│   │
│   │
│   └─── Version changes
│        │
│        │
│        └─── Bounties
│        │    │   README.md
│        │    │
│        │
│        │
│        └─── Policies
│        │    │   README.md
│        │    │
│        │
│        │
│        └─── Scopes
│        │    │   README.md
│        │    │
│        │
│        │
│        └─── Updates
│             │   README.md
│             │
│
│
└───Other platforms/Policies
```


## Models
```
Models
│ 
│   
└───Classification
│   │   README.md
│   │
│   
│
└───NER
    │   README.md
    │
```


## Utils
```
Utils
│ 
│   
│   README.md
```

