resource "google_artifact_registry_repository" "containers" {
  location      = "europe-west2"
  repository_id = "containers"
  format        = "DOCKER"
}
