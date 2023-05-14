variable "region" {
  type = string
}

resource "google_artifact_registry_repository" "main" {
  location      = var.region
  repository_id = "cloud-run-source-deploy"
  description   = "cloud run docker repository"
  format        = "DOCKER"
}
