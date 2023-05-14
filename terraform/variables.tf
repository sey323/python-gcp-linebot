variable "region" {
  type        = string
  description = "region"
  default     = "asia-east1"
}

variable "service_account_key" {
  type        = string
  description = "gcp project service account key file path"
  default     = "terraform-key.json"
}

variable "project_id" {
  type        = string
  description = "gcp project id"
}

variable "repository_group" {
  type        = string
  description = "repository group"
  default     = "sey323"
}

variable "repository_name" {
  type    = string
  default = "python-gcp-linebot"
}

variable "repository_branch" {
  type    = string
  default = "main"
}



