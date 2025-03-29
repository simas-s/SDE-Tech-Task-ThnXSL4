resource "google_bigquery_dataset" "raw_layer" {
  dataset_id = "raw"
  location = var.region
}

resource "google_bigquery_table" "daily_weather" {
  dataset_id = google_bigquery_dataset.raw_layer.dataset_id
  table_id = "daily_weather"
  schema = file("../schemas/raw/daily_weather.json")
}