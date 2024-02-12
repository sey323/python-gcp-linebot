variable "repository_name" {
  type = string
}

variable "repository_branch" {
  type = string
}

variable "repository_group" {
  type = string
}

variable "project_id" {
  type = string
}

variable "region" {
  type = string
}

variable "github_secret_id" {
  type = string
}


resource "google_cloudbuildv2_connection" "main" {
  provider = google-beta
  project  = var.project_id
  location = var.region
  name     = var.repository_name

  github_config {
    app_installation_id = 30657788
    authorizer_credential {
      oauth_token_secret_version = var.github_secret_id
    }
  }
}

resource "google_cloudbuildv2_repository" "main" {
  provider          = google-beta
  location          = var.region
  name              = var.repository_name
  parent_connection = google_cloudbuildv2_connection.main.name
  project           = var.project_id
  remote_uri        = "https://github.com/${var.repository_group}/${var.repository_name}.git"
}

resource "google_cloudbuild_trigger" "main" {
  provider    = google-beta
  project     = var.project_id
  name        = "${var.repository_name}-trigger"
  description = "Build and deploy to Cloud Run service ${var.repository_name} on push to \"^main$\""
  location    = var.region
  filename    = "cloudbuild.yaml"

  repository_event_config {
    repository = google_cloudbuildv2_repository.main.id
    push {
      branch = var.repository_branch
    }
  }

  substitutions = {
    "_AR_HOSTNAME"   = "${var.region}-docker.pkg.dev"
    "_DEPLOY_REGION" = "${var.region}"
    "_PLATFORM"      = "managed"
    "_SERVICE_NAME"  = "${var.repository_name}"
    "_TRIGGER_NAME"  = "${var.repository_name}-trigger"
  }

  tags = [
    "gcp-cloud-build-deploy-cloud-run",
    "gcp-cloud-build-deploy-cloud-run-managed",
    "${var.repository_name}",
  ]
}

resource "null_resource" "wait_for_cloud_build_trigger" {
  # Cloud Build Trigger作成後、1回実行して、Cloud Runにデプロイする

  depends_on = [google_cloudbuild_trigger.main]
  provisioner "local-exec" {
    command = "gcloud builds triggers run ${google_cloudbuild_trigger.main.name} --branch=${var.repository_branch} --region=${var.region} --quiet"
  }

  provisioner "local-exec" {
    command = <<EOT
until [[ "$(gcloud builds list --region=${var.region} --format=json | jq -r '.[0].status')" == "SUCCESS" ]]; do 
  sleep 10
done
EOT
  }

  # 
  provisioner "local-exec" {
    command = "gcloud run services delete ${var.repository_name} --platform managed --region ${google_cloudbuild_trigger.main.location} -q"
  }
}

