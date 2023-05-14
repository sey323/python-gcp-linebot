variable "project_id" {
  type = string
}

variable "repository_name" {
  type = string
}

variable "region" {
  type = string
}

variable "line_channel_secret_id" {
  type = string
}

variable "line_channel_access_token_id" {
  type = string
}

variable "latest_tag" {
  type = string
}

resource "google_cloud_run_v2_service" "main" {
  name     = var.repository_name
  location = var.region
  project  = var.project_id

  labels = {
    "managed-by" = "gcp-cloud-build-deploy-cloud-run"
  }

  template {
    scaling {
      min_instance_count = 1
      max_instance_count = 3
    }
    containers {
      image = "asia-east1-docker.pkg.dev/coherent-bliss-386617/cloud-run-source-deploy/python-gcp-linebot/python-gcp-linebot:latest"
      resources {
        limits = {
          "memory" : "2Gi",
          "cpu" : "1000m"
        }
      }
      env {
        name = "LINE_CHANNEL_SECRET"
        value_source {
          secret_key_ref {
            secret  = var.line_channel_secret_id
            version = "latest"
          }
        }
      }
      env {
        name = "LINE_CHANNEL_ACCESS_TOKEN"
        value_source {
          secret_key_ref {
            secret  = var.line_channel_access_token_id
            version = "latest"
          }
        }
      }
    }
  }
}
