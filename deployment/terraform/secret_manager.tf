resource "google_secret_manager_secret" "openweather_api_key" {
  secret_id = "openweather-api-key"
  replication {
    automatic = true
  }
}