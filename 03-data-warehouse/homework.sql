--create external table
CREATE OR REPLACE EXTERNAL TABLE `homework.green_taxi_external`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://data-engineering-course-411410-data-warehouse-eu/green_tripdata_2022-*.parquet']
);


-- create bigquery table not partitioned
CREATE OR REPLACE TABLE `homework.green_taxi`
AS SELECT * FROM `homework.green_taxi_external`;


-- crate table partition and cluster
CREATE OR REPLACE TABLE `homework.green_taxi_partitioned_clustered`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID AS (
  SELECT * FROM `homework.green_taxi`
);



-- question 1
SELECT COUNT(VendorID)
FROM `data-engineering-course-411410.homework.green_taxi`


-- question 2
SELECT DISTINCT(PULocationID)
FROM `data-engineering-course-411410.homework.green_taxi`

SELECT DISTINCT(PULocationID)
FROM `data-engineering-course-411410.homework.green_taxi_external`


-- question 3
SELECT COUNT(fare_amount)
FROM `data-engineering-course-411410.homework.green_taxi`
WHERE fare_amount = 0


-- question 5
SELECT DISTINCT(PULocationID)
FROM `data-engineering-course-411410.homework.green_taxi_partitioned_clustered`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30'


-- question 8
SELECT COUNT(*)
FROM `data-engineering-course-411410.homework.green_taxi`
