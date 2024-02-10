## OLAP vs OLTP

OLAP: online analytical processes
OLTP: online transaction processes

|                     | OLTP                                                                                              | OLAP                                                                              |
| ------------------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Purpose             | Control and run essential business operations in real time                                        | Plan, solve problems, support decisions, discover hidden insights                 |
| Data updates        | Short, fast updates initiated by user                                                             | Data periodically refreshed with scheduled, long-running batch jobs               |
| Database design     | Normalized databases for efficiency                                                               | Denormalized databases for analysis                                               |
| Space requirements  | Generally small if historical data is archived                                                    | Generally large due to aggregating large datasets                                 |
| Backup and recovery | Regular backups required to ensure business continuity and meet legal and governance requirements | Lost data can be reloaded from OLTP database as needed in lieu of regular backups |
| Productivity        | Increases productivity of end users                                                               | Increases productivity of business managers, data analysts, and executives        |
| Data view           | Lists day-to-day business transactions                                                            | Multi-dimensional view of enterprise data                                         |
| User examples       | Customer-facing personnel, clerks, online shoppers                                                | Knowledge workers such as data analysts, business analysts, and executives        |


## Data warehouse

A data warehouse is an OLAP solution and is used for reporting and data analysis
They have multiple data source.
Outputs can be data marts.

## BigQuery

Serverless data warehouse. Scalable and high-availability. Storage and computing is separate.
Features: ML; geospatial data, BI.

On demand pricing

## Tips

Partition your database by date to improve performance and reduce cost.
Clustering will sort rows inside a partition. Can also improve performance.

Table with data size < 1GB don't show significant improvementwith partitioning and clustering.

Big query can do automatic re-clustering.


    -- Creating a partition and cluster table
    CREATE OR REPLACE TABLE taxi-rides-ny.nytaxi.yellow_tripdata_partitoned_clustered
    PARTITION BY DATE(tpep_pickup_datetime)
    CLUSTER BY VendorID AS
    SELECT * FROM taxi-rides-ny.nytaxi.external_yellow_tripdata;


## BigQuery best practices

Cost reduction
- avoid SELECT * 
- price your queries before running them
- use clustered or aprtitioned tables
- use streaming inserts with caution
- materialize query results in stages

Query performance
- Filter on partitioned columns
- Denormalizing data
- Use nested or repeated columns
- Use external data sources should be appropriately used
- Reduce data before joins
- Do not treat with clauses as prepared statements
- Avoid oversharding tables
- Avoid JavaScript user-defined functions
- Use approximate aggregation functions (HyperLogLog++)
- Order Last, for query operations to maximize performance
- Optimize your join patterns
  - As a best practice, place the table with the largest number of rows first,  followed by the table with the fewest rows, and then place the remaining tables by decreasing size.

## ML in BigQuery


    -- SELECT THE COLUMNS INTERESTED FOR YOU
    SELECT passenger_count, trip_distance, PULocationID, DOLocationID, payment_type, fare_amount, tolls_amount, tip_amount
    FROM `taxi-rides-ny.nytaxi.yellow_tripdata_partitoned` WHERE fare_amount != 0;

---
    -- CREATE A ML TABLE WITH APPROPRIATE TYPE
    CREATE OR REPLACE TABLE `taxi-rides-ny.nytaxi.yellow_tripdata_ml` (
    `passenger_count` INTEGER,
    `trip_distance` FLOAT64,
    `PULocationID` STRING,
    `DOLocationID` STRING,
    `payment_type` STRING,
    `fare_amount` FLOAT64,
    `tolls_amount` FLOAT64,
    `tip_amount` FLOAT64
    ) AS (
    SELECT passenger_count, trip_distance, cast(PULocationID AS STRING), CAST(DOLocationID AS STRING),
    CAST(payment_type AS STRING), fare_amount, tolls_amount, tip_amount
    FROM `taxi-rides-ny.nytaxi.yellow_tripdata_partitoned` WHERE fare_amount != 0
    );

---

    -- CREATE MODEL WITH DEFAULT SETTING
    CREATE OR REPLACE MODEL `taxi-rides-ny.nytaxi.tip_model`
    OPTIONS
    (model_type='linear_reg',
    input_label_cols=['tip_amount'],
    DATA_SPLIT_METHOD='AUTO_SPLIT') AS
    SELECT
    *
    FROM
    `taxi-rides-ny.nytaxi.yellow_tripdata_ml`
    WHERE
    tip_amount IS NOT NULL;

---

    -- CHECK FEATURES
    SELECT * FROM ML.FEATURE_INFO(MODEL `taxi-rides-ny.nytaxi.tip_model`);

---

    -- EVALUATE THE MODEL
    SELECT
    *
    FROM
    ML.EVALUATE(MODEL `taxi-rides-ny.nytaxi.tip_model`,
    (
    SELECT
    *
    FROM
    `taxi-rides-ny.nytaxi.yellow_tripdata_ml`
    WHERE
    tip_amount IS NOT NULL
    ));

---

    -- PREDICT THE MODEL
    SELECT
    *
    FROM
    ML.PREDICT(MODEL `taxi-rides-ny.nytaxi.tip_model`,
    (
    SELECT
    *
    FROM
    `taxi-rides-ny.nytaxi.yellow_tripdata_ml`
    WHERE
    tip_amount IS NOT NULL
    ));

---

    -- PREDICT AND EXPLAIN
    SELECT
    *
    FROM
    ML.EXPLAIN_PREDICT(MODEL `taxi-rides-ny.nytaxi.tip_model`,
    (
    SELECT
    *
    FROM
    `taxi-rides-ny.nytaxi.yellow_tripdata_ml`
    WHERE
    tip_amount IS NOT NULL
    ), STRUCT(3 as top_k_features));

---

    -- HYPER PARAM TUNNING
    CREATE OR REPLACE MODEL `taxi-rides-ny.nytaxi.tip_hyperparam_model`
    OPTIONS
    (model_type='linear_reg',
    input_label_cols=['tip_amount'],
    DATA_SPLIT_METHOD='AUTO_SPLIT',
    num_trials=5,
    max_parallel_trials=2,
    l1_reg=hparam_range(0, 20),
    l2_reg=hparam_candidates([0, 0.1, 1, 10])) AS
    SELECT
    *
    FROM
    `taxi-rides-ny.nytaxi.yellow_tripdata_ml`
    WHERE
    tip_amount IS NOT NULL;