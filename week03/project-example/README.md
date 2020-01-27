
# Data Ingestion Example

[[DESCRIPTION OF PROJECT]]

## Usage Instructions

* Description of targets and using `run.py`

## Description of Contents

The project consists of these portions:
```
PROJECT
├── .env
├── .gitignore
├── README.md
├── config
│   ├── data-params.json
│   └── test-params.json
├── data
│   ├── log
│   ├── out
│   ├── raw
│   └── temp
├── lib
├── notebooks
│   └── .gitkeep
├── references
│   └── .gitkeep
├── requirements.txt
├── run.py
└── src
    └── etl.py
```

### `src`

* `etl.py`: Library code that executes tasks useful for getting data.

### `config`

* `data-params.json`: Common parameters for getting data, serving as
  inputs to library code.
  
* `test-params.json`: parameters for running small process on small
  test data.

### `references`

* Data Dictionaries, references to external sources

### `notebooks`

* Jupyter notebooks for *analyses*
  - notebooks are not for data processing; they should import code
    from `src`.
