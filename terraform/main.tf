
data "external" "env" {
  program = ["/bin/sh", "./env.sh"]
}

data "google_project" "project" {
}

module "api" {
  source = "./module/api"
}

module "iam" {
  source         = "./module/iam"
  depends_on     = [module.api]
  project_id     = var.project_id
  project_number = data.google_project.project.number
}

module "secretmanager" {
  source          = "./module/secretmanager"
  depends_on      = [module.api]
  repository_name = var.repository_name
  project_id      = var.project_id

  github_token              = data.external.env.result["github_token"]
  line_channel_access_token = data.external.env.result["line_channel_access_token"]
  line_channel_secret       = data.external.env.result["line_channel_secret"]
}

module "artifactregistory" {
  source     = "./module/artifactregistory"
  depends_on = [module.api]
  region     = var.region
}

module "cloudbuild" {
  source            = "./module/cloudbuild"
  depends_on        = [module.iam, module.secretmanager, module.artifactregistory]
  project_id        = var.project_id
  repository_group  = var.repository_group
  repository_name   = var.repository_name
  repository_branch = var.repository_branch
  region            = var.region
  github_secret_id  = module.secretmanager.github_secret_id
}

module "cloudrun" {
  source                       = "./module/cloudrun"
  depends_on                   = [module.cloudbuild]
  project_id                   = var.project_id
  repository_name              = var.repository_name
  region                       = var.region
  line_channel_secret_id       = module.secretmanager.line_channel_secret_id
  line_channel_access_token_id = module.secretmanager.line_channel_access_token_id
  latest_tag                   = "latest"
}
