resource "google_storage_bucket" "cloud_build_logs" {
  name = "${var.project_id}-cloud-build-logs"
  location = var.region
}