This repository includes an ETL pipeline which reads data from the OpenWeather API and loads it into BigQuery, some
analytical SQL for the ingested data and some infrastructure deployment.

The deployment folder contains a schema definition for the target BigQuery table, and a Terraform configuration to
deploy resources in GCP.
The cloudbuild.yaml file contains deployment steps for containerising code and applying infrastructure changes.

To execute an ETL run in Cloud Run:
gcloud run jobs execute ingest-daily-weather --args="YYYY-MM-DD"
