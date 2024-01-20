# Question 1. Knowing docker tags
Answer -rm

# Question 2. Understanding docker first run
Answer 0.42.0

# Question 3. Count records
Answer 15612

# Question 4. Largest trip for each day
Answer 2019-09-26

query:
SELECT extract(epoch from CAST(g.lpep_dropoff_datetime AS TIME) - 
			   CAST(g.lpep_pickup_datetime AS TIME)) as diff,
	g.lpep_pickup_datetime, g.lpep_dropoff_datetime,
	g.trip_distance, g.fare_amount, g.tolls_amount
FROM public.green_taxi_data as g
ORDER BY diff DESC
LIMIT 100;

# Question 5. Three biggest pick up Boroughs
Answer: "Brooklyn" "Manhattan" "Queens"

query:
SELECT z."Borough", round(CAST(sum(g.total_amount) AS numeric), 0) as sum_total_amount
FROM public.green_taxi_data as g
LEFT JOIN public.zones as z
ON g."PULocationID" = z."LocationID"
WHERE CAST(g.lpep_pickup_datetime AS DATE) = '2019-09-18'
	AND z."Borough" != 'Unknown'
GROUP BY z."Borough"
HAVING round(CAST(sum(g.total_amount) AS numeric), 0) > 50000
ORDER BY sum_total_amount DESC;

# Question 6. Largest tip
Answer: Kips Bay  (not in the possible answers...)

query:
SELECT puz."Zone" as puz, doz."Zone" as poz, g.tip_amount, g.lpep_pickup_datetime
FROM public.green_taxi_data as g
LEFT JOIN public.zones as puz
ON g."PULocationID" = puz."LocationID"
LEFT JOIN public.zones as doz
ON g."DOLocationID" = doz."LocationID"
WHERE puz."Zone" = 'Astoria'
ORDER BY g.tip_amount DESC
LIMIT 100;

# Question 7. Creating Resources


	Terraform used the selected providers to generate the following execution plan. Resource actions are
	indicated with the following symbols:
	+ create

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