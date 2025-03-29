resource "google_service_account" "cloudbuild_sa" {
  account_id   = "cloudbuild-service-acc"
  display_name = "Cloud Build Service Account"
  project      = var.project_id
}

resource "google_cloudbuild_trigger" "merge_main" {
  name = "merge-main"
  filename = "../cloudbuild.yaml"
  service_account = google_service_account.cloudbuild_sa.id
  github {
    owner = "simas-s"
    name = "SDE-Tech-Task-ThnXSL4"

    push {
      branch = "^main$"
    }
  }
}