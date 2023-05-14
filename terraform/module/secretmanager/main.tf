
variable "repository_name" {
  type = string
}

variable "project_id" {
  type = string
}

variable "github_token" {
  type = string
}

variable "line_channel_access_token" {
  type = string
}

variable "line_channel_secret" {
  type = string
}

resource "google_secret_manager_secret" "line_channel_access_token" {
  secret_id = "LINE_CHANNEL_ACCESS_TOKEN"

  labels = {
    label = var.repository_name
  }

  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret_version" "line_channel_access_token" {
  provider    = google-beta
  secret      = google_secret_manager_secret.line_channel_access_token.id
  secret_data = var.line_channel_access_token
}

output "line_channel_access_token_id" {
  value = google_secret_manager_secret.line_channel_access_token.secret_id
}

resource "google_secret_manager_secret" "line_channel_secret" {
  secret_id = "LINE_CHANNEL_SECRET"

  labels = {
    label = var.repository_name
  }

  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret_version" "line_channel_secret" {
  provider    = google-beta
  secret      = google_secret_manager_secret.line_channel_secret.id
  secret_data = var.line_channel_secret
}

output "line_channel_secret_id" {
  value = google_secret_manager_secret.line_channel_secret.secret_id
}

resource "google_secret_manager_secret" "git_hub" {
  secret_id = "github-token-secret"

  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret_version" "git_hub" {
  provider    = google-beta
  secret      = google_secret_manager_secret.git_hub.id
  secret_data = var.github_token
}

output "github_secret_id" {
  value = google_secret_manager_secret_version.git_hub.id
}
