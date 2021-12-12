# Analyze Firms’ ESG Commitment from Texts

The project performs Environmental, Social, and Governance (ESG) commitment analysis based on texts extracted from companies' 10-K/10-Q filings

## Environment Setup

Navigate to the project root folder and run the following command:
```bash
pip install -r requirements.txt
```

## Content Description
Directory Structure
```
esg_nlp
│   README.md
│   requirements.txt
│   notebook.ipynb                  # Title of the notebook indicates its content
│   ...
│
└───data
│   │   esg_score.xlsx              # Contain ESG scores for each ticker
│   │   sp500_component_stocks.csv  # S&P 500 Company to ticker pair
│   │   stock_info.csv              # Detailed info of each stock
│   │
│   └───goodvbad                    # Contain dictionaries using good versus bad approach
│   │   │   file1.csv
│   │   │   file2.csv
│   │   │   ...
│   │
│   └───regression                  # Contain dictionaries using regression approach
│       │   file1.csv
│       │   file2.csv
│       │   ...
│   
└───utils
    │   file.py                     # Contain util functions for crawler, preprocessing, validation, etc.
    │   ...
```

## Acknowledgments
Coworked with Mohammed Al Harmoudi and Siddharth Kantamneni on the project. Supervised by Dr. Stoikov at Cornell and sponsored by Rebellion Research.