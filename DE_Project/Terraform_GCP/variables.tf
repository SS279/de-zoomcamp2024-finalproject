variable "credentials" {
  description = "My Credentials"
  default     = "key/dezoomcamp-411914-6c5c8d31dd66.json"
  #ex: if you have a directory where this file is called keys with your service account json file
  #saved there as my-creds.json you could use default = "./keys/my-creds.json"
}


variable "project" {
  description = "Project"
  default     = "dezoomcamp-411914"
}

variable "region" {
  description = "Region"
  default     = "europe-west2-a"
}

variable "location" {
  description = "Project Location"
  default     = "EUROPE-WEST2"
}

variable "dezoomcamp_final_proj_bucket" {
  description = "DEZoomcamp final project Storage Bucket Name"
  #Update the below to a unique bucket name
  default     = "dezoomcamp_london_crimes_bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

variable "dezoomcamp_finalproj_bqdataset" {
  description = "DEZoomcamp final project BigQuery Dataset Name"
  #Update the below to what you want your dataset to be called
  default     = "crimes_in_uk"
}