# Modern Data Stack Portfolio Project

A production-grade data platform built with Snowflake, dbt, and GitHub Actions — 
demonstrating the architecture and engineering practices used in real-world 
data platform deployments.

## Architecture
```
FRED API → Snowflake (RAW) → dbt Staging → dbt Marts → Analytics
```

## Tech Stack

- **Snowflake** — Cloud data warehouse with DEV, TEST, and PROD environments
- **dbt Core** — Data transformation with staging and mart layers
- **GitHub Actions** — Automated CI/CD pipeline for dbt runs and tests
- **Python** — Data ingestion from FRED (Federal Reserve Economic Data) API

## Project Structure
```
├── .github/workflows/     # GitHub Actions CI/CD pipeline
├── dbt/portfolio_project/
│   └── models/
│       ├── staging/       # Raw to clean transformations
│       └── marts/         # Business-ready analytical models
├── ingestion/             # Python data ingestion scripts
└── README.md
```

## Data Models

### Staging Layer
- `stg_gdp` — US GDP quarterly data
- `stg_unemployment` — US Unemployment rate monthly data  
- `stg_inflation` — US CPI inflation monthly data

### Mart Layer
- `mart_economic_indicators` — Joined analytical table combining 
GDP, unemployment, and inflation for trend analysis

## CI/CD Pipeline

Every push to main triggers GitHub Actions to:
1. Install dbt
2. Connect to Snowflake
3. Run all dbt models
4. Run all dbt tests
5. Report results

## Environment Strategy

| Environment | Purpose | Schema |
|-------------|---------|--------|
| DEV | Active development | dbt_dev |
| TEST | QA and validation | dbt_test |
| PROD | Production data | dbt_prod |

## About

Built as a portfolio project to demonstrate modern data engineering practices
including version-controlled transformations, automated deployments, and 
environment promotion strategies.