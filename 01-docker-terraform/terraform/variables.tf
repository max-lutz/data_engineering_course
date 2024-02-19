variable "credentials" {
  description = "my credentials"
  default     = "/home/max_lutz/.gc/ny-rides.json"
}

variable "project" {
  description = "project name"
  default     = "data-engineering-course-411410"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default = "europe-west9"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default = "EU"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  #Update the below to what you want your dataset to be called
  default = "example_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  #Update the below to a unique bucket name
  default = "data-engineering-course-411410-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
