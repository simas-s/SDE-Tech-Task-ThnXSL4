resource "google_service_account" "cloudrun_sa" {
  account_id   = "cloudrun-service-acc"
  display_name = "Cloud Run Service Account"
  project      = var.project_id
}

resource "google_project_iam_member" "cloudrun" {
  for_each = toset([
    "roles/bigquery.jobUser",
    "roles/bigquery.dataEditor",
    "roles/secretmanager.secretAccessor",
    "roles/iam.serviceAccountUser"])
  project = var.project_id
  role = each.key
  member = "serviceAccount:${google_service_account.cloudrun_sa.email}"
}

resource "google_service_account" "cloud_scheduler_sa" {
  account_id = "cloudscheduler-service-acc"
  display_name = "Cloud Scheduler Service Account"
  project = var.project_id
}

resource "google_project_iam_member" "cloudscheduler" {
  for_each = toset([
  "roles/run.invoker",
  "roles/iam.serviceAccountUser"])
  project = var.project_id
  role = each.key
  member = "serviceAccount:${google_service_account.cloud_scheduler_sa.email}"
}

resource "google_cloud_run_v2_job" "weather_ingest" {
  name = "ingest-daily-weather"
  location = var.region

  template {
    template {
      service_account = google_service_account.cloudrun_sa.email

      containers {
        image = "europe-west2-docker.pkg.dev/essencemediacom-technical/containers/ingest:latest"

        env {
          name = "PROJECT_ID"
          value = var.project_id
        }
      }
    }
  }
}

resource "google_cloud_scheduler_job" "daily_ingest" {
  name = "daily-ingest"
  schedule = "0 9 * * *"
  region = var.region
  project = var.project_id

  http_target {
    http_method = "POST"
    uri = "https://${var.region}-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/${var.project_number}/jobs/${google_cloud_run_v2_job.weather_ingest.name}:run"
    oauth_token {
      service_account_email = google_service_account.cloud_scheduler_sa.email
    }
  }
}
