PROJECT_ID=$1

gcloud auth application-default login --disable-quota-project

echo ${PROJECT_ID}
gcloud config set project ${PROJECT_ID}
gcloud iam service-accounts create terraform-account \
  --display-name "Used by Terraform on the local machine"
gcloud projects add-iam-policy-binding ${PROJECT_ID} \
  --member serviceAccount:terraform-account@${PROJECT_ID}.iam.gserviceaccount.com \
  --role roles/editor

# Save Service Account json File
gcloud iam service-accounts keys create key/terraform-key.json \
  --iam-account terraform-account@${PROJECT_ID}.iam.gserviceaccount.com
