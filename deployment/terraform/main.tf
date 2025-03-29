terraform {
  required_version = "1.4.5"

  backend "gcs" {
    prefix = "state"
    bucket = "essencemediacom-technical-terraform"
  }

  required_providers {
    google = {
      version = "6.27.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region = var.region
}

resource "google_projcet_service" "required_services" {
  for_each = toset([
    "cloudbuild.googleapis.com"
  ])
  service = each.key
  project = var.project_id

}