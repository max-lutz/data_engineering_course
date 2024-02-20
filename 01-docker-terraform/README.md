# Week 1: Docker and terraform

## Docker:

Use docker-compose to setup a postgres database and a pgadmin service.
Use docker to run a python script to load data into the postgres database.

Features:
- Run three docker containers at the same time
- Connect the containers via a network
- Persist the data when shutting down the containers using volumes

#### Results:
```
root@localhost:ny_taxi> SELECT COUNT(1) FROM test
+---------+
| count   |
|---------|
| 7275986 |
+---------+
SELECT 1
Time: 0.794s
```


#### Useful commands
    # Build docker image
    docker build -t nyc_taxi_ingest:1.0 .

    # Check that postgres is running:
    pgcli -h localhost -U root -d ny_taxi

    # Ingest one month of data
    docker run --network pg_network -e PYTHONUNBUFFERED=1 nyc_taxi_ingest:1.0 --user root --password root --host pgdatabase --port 5432 --db ny_taxi --table_name test --url https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2020-04.csv.gz





## Terraform:

Here we set up a bigquery dataset and a google cloud storage bucket using terraform


terraform commands used:
```
terraform init
terraform plan
terraform apply
terraform destroy
```

#### terraform plan

```
Terraform will perform the following actions:

  # google_bigquery_dataset.demo_dataset will be created
  + resource "google_bigquery_dataset" "demo_dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "example_dataset"
      + default_collation          = (known after apply)
      + delete_contents_on_destroy = false
      + effective_labels           = (known after apply)
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + is_case_insensitive        = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "EU"
      + max_time_travel_hours      = (known after apply)
      + project                    = "data-engineering-course-411410"
      + self_link                  = (known after apply)
      + storage_billing_model      = (known after apply)
      + terraform_labels           = (known after apply)
    }

  # google_storage_bucket.demo-bucket will be created
  + resource "google_storage_bucket" "demo-bucket" {
      + effective_labels            = (known after apply)
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "EU"
      + name                        = "data-engineering-course-411410-terra-bucket"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + rpo                         = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = (known after apply)
      + uniform_bucket_level_access = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "AbortIncompleteMultipartUpload"
            }
          + condition {
              + age                   = 1
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.
```


#### terraform apply

```
google_bigquery_dataset.demo_dataset: Creating...
google_storage_bucket.demo-bucket: Creating...
google_storage_bucket.demo-bucket: Creation complete after 1s [id=data-engineering-course-411410-terra-bucket]
google_bigquery_dataset.demo_dataset: Creation complete after 1s [id=projects/data-engineering-course-411410/datasets/example_dataset]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```

#### terraform destroy

```
google_bigquery_dataset.demo_dataset: Destroying... [id=projects/data-engineering-course-411410/datasets/example_dataset]
google_storage_bucket.demo-bucket: Destroying... [id=data-engineering-course-411410-terra-bucket]
google_bigquery_dataset.demo_dataset: Destruction complete after 1s
google_storage_bucket.demo-bucket: Destruction complete after 2s

Destroy complete! Resources: 2 destroyed.
```
