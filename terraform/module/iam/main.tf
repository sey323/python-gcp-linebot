variable "project_id" {
  type = string
}

variable "project_number" {
  type = string
}

resource "google_project_iam_binding" "secret_accessors" {
  provider = google-beta
  role     = "roles/secretmanager.secretAccessor"
  project  = var.project_id

  members = [
    "serviceAccount:service-${var.project_number}@gcp-sa-cloudbuild.iam.gserviceaccount.com",
    "serviceAccount:${var.project_number}-compute@developer.gserviceaccount.com"
  ]
}

resource "google_project_iam_binding" "cloudbuild" {
  provider = google-beta
  for_each = toset([
    "roles/run.developer",
    "roles/iam.serviceAccountUser"
  ])
  role    = each.key
  project = var.project_id

  members = ["serviceAccount:${var.project_number}@cloudbuild.gserviceaccount.com"]
}

