# Crimes committed in London Boroughs - 2022 and 2023

## Project Overview
This project focuses on building a data pipeline for extracting, staging, ingesting, and transforming data from an API source into Google BigQuery for further analysis and reporting. The pipeline is orchestrated using Mage with additional infrastructure setup managed by Terraform. Transformation and modeling of data are conducted using dbt Cloud, with reporting facilitated through Google Looker.

## Looker Dashboard
[Crimes in London Boroughs](https://lookerstudio.google.com/reporting/7aa8f78a-ff53-4f05-b0e0-38d700ce1ba6)

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
2. Staging Data: Extracted data is staged in Google Cloud Storage.
3. Ingestion: Staged data is ingested into BigQuery.
4. Transformation: Data transformation is conducted using dbt Cloud with three layers: source layer, staging layer, and reporting layer.
5. Infrastructure Setup: Terraform provisions necessary infrastructure components such as GCS bucket and BigQuery dataset.
6. Dashboarding: Google Looker is used to build a dashboard on top of the reporting layer table for visualization and reporting purposes.

## Repository Structure
The repository is organized as follows:

/Mage: Contains Mage scripts for data extraction, staging, and ingestion.
/Terraform_GCP: Holds Terraform configurations for provisioning GCP resources.
/dbt: Contains dbt models and transformation scripts.
/dataset: Raw data csv file

## Setup Instructions
1. Clone Repository: Clone this repository to your local machine.
2. Install Dependencies: Ensure you have Mage, Terraform, dbt Cloud, and Google Looker setup and configured.
3. Configuration:
    - Update Mage scripts with API credentials and GCP credentials.
    - Modify Terraform configurations for specific project requirements.
    - Configure dbt models according to data transformation needs.
4. Execute Scripts: Run Mage scripts for data extraction, Terraform scripts for infrastructure setup, and dbt commands for data transformation.
5. Dashboard Creation: Utilize Google Looker to create reports and dashboards based on the reporting layer tables.