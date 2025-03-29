resource "google_cloudbuild_trigger" "merge_main" {
  name = "merge-main"
  filename = "../cloudbuild.yaml"
  github {
    owner = "simas-s"
    name = "SDE-Tech-Task-ThnXSL4"

    push {
      branch = "^main$"
    }
  }
}