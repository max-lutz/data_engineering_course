## Question 1: What is count of records for the 2022 Green Taxi Data??
Answer: 840,402

## Question 2:
Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

Answer: 0 MB for the External Table and 6.41MB for the Materialized Table

## Question 3:
How many records have a fare_amount of 0?
Answer: 1,622

## Question 4:
What is the best strategy to make an optimized table in Big Query if your query will always order the results by PUlocationID and filter based on lpep_pickup_datetime? (Create a new table with this strategy)
Answer: Partition by lpep_pickup_datetime Cluster on PUlocationID


## Question 5:
Write a query to retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 (inclusive)

Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed. What are these values?

Choose the answer which most closely matches.
Answer: 12.82 MB for non-partitioned table and 1.12 MB for the partitioned table


## Question 6:
Where is the data stored in the External Table you created?
Answer:  GCP Bucket

## Question 7:
It is best practice in Big Query to always cluster your data:
Answer: False



# Code:

    -- external table
    CREATE OR REPLACE EXTERNAL TABLE `homework.green_taxi_external`
    OPTIONS (
    format = 'PARQUET',
    uris = ['gs://data-engineering-course-...-data-warehouse-eu/green_tripdata_2022-*.parquet']
    );

---

    -- bigquery table not partitioned
    CREATE OR REPLACE TABLE `homework.green_taxi`
    AS SELECT * FROM `homework.green_taxi_external`;

---

    -- partition and cluster
    CREATE OR REPLACE TABLE `homework.green_taxi_partitioned_clustered`
    PARTITION BY DATE(lpep_pickup_datetime)
    CLUSTER BY PUlocationID AS (
    SELECT * FROM `homework.green_taxi`
    );

---

    -- question 1
    SELECT COUNT(VendorID)
    FROM `data-engineering-course-411410.homework.green_taxi`

---

    -- question 2
    SELECT DISTINCT(PULocationID)
    FROM `data-engineering-course-411410.homework.green_taxi`

    SELECT DISTINCT(PULocationID)
    FROM `data-engineering-course-411410.homework.green_taxi_external`

---

    -- question 3
    SELECT COUNT(fare_amount)
    FROM `data-engineering-course-411410.homework.green_taxi`
    WHERE fare_amount = 0

---

    -- question 5
    SELECT DISTINCT(PULocationID)
    FROM `data-engineering-course-411410.homework.green_taxi_partitioned_clustered`
    WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30'
