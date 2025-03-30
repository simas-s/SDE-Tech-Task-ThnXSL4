resource "google_cloud_run_v2_job" "weather_ingest" {
  name = "ingest-daily-weather"
  location = var.region

  template {
    template {
      containers {
        image = "europe-west2-docker.pkg.dev/essencemediacom-technical/containers/ingest:latest"
      }
    }
  }
}