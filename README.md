# Crimes committed in London Boroughs - 2022 and 2023

## Project Overview
This project is focused on building a data pipeline for extracting, staging, ingesting, and transforming data from an API source into Google BigQuery for further analysis and reporting. The pipeline is orchestrated using Mage with additional infrastructure setup managed by Terraform. Transformation and modeling of data are conducted using dbt Cloud, with reporting facilitated through Google Looker.

## Looker Dashboard
Please find the link to Looker dashboard here - [Crimes in London Boroughs](https://lookerstudio.google.com/s/nSxsOSAXNk8)

## Technologies Used
- Mage: Orchestration tool for data pipelines.
- Google Cloud Platform (GCP):
    -  Google Cloud Storage (GCS): Used as staging area for data.
    -  Google BigQuery: Data warehousing solution for ingesting and analyzing structured data.
- Terraform: Infrastructure as code tool for provisioning GCS bucket and BigQuery dataset.
- Python: Data manipulation and transformation within Mage.
- dbt Cloud: Data modeling and transformation tool.
- Google Looker: Business intelligence and data visualization platform.

## Workflow
1. Data Extraction: Mage is utilized to extract data from the API source and store it in CSV format.
2. Infrastructure Setup: Terraform provisions necessary infrastructure components such as GCS bucket and BigQuery dataset.
3. Staging Data: Extracted data is staged in Google Cloud Storage.
4. Ingestion: Staged data is ingested into BigQuery.
5. Transformation: Data transformation is conducted using dbt Cloud with three layers: source layer, staging layer, and reporting layer. 
6. Dashboarding: Google Looker is used to build a dashboard on top of the reporting layer table for visualization and reporting purposes.

## Repository Structure
The repository is organized as follows:

- Mage: Contains Mage scripts for data extraction, staging, and ingestion.
- Terraform_GCP: Holds Terraform configurations for provisioning GCP resources.
- dbt: Contains dbt models and transformation scripts.
- dataset: Raw data csv file