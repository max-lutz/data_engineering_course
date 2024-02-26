# Processing data

## Batch

Batch jobs run frequently:
- weekly
- daily
- hourly
- every 5 minutes...

Tools:
- python script
- SQL
- spark

Advantages of batch jobs:
- easy to manage
- retry
- scale

Disadvantage:
- delay

Most of the jobs are batch processing.


## Spark

A data processing engine. It is multi language (python, scala, java).
It relies on a cluster to execute the jobs.

Spark covers batch and streaming.

#### When to use Spark?
When your data is in a data lake.
Load data from a data lake, execute the job on spark and save the results back to a data lake.

If you can express something with SQL use SQL if not use Spark (ML).

A typical process for training a model could be:
raw data --> data lake --> SQL (athena) --> Spark --> python (train ML)
                                              |               |
                                              v               v
                                        Spark (apply ML)    model
                                              |
                                              v
                                            data lake


#### Spark dataframes

Transformations are lazy (not executed immediatly)
Actions (show(), take(), head()) trigger the transformation to be run.


You can define functions in python for pyspark and test them and version control them. It's better than trying to do this in SQL.

## Spark internals

#### Spark cluster:
- master node and multiple executor nodes
- jobs are send to master and then executors

Now data is stored on the cloud (S3 or GCS), Hadoop and HDFS are less popular now.

#### Spark group by

- each executor receives a partition of the data
- it applies the filtering and group by on this data
- the data of each executor is reshuffled: data with the same key are sent to the same node (the key corresponds to the the groupby columns)
- these executor then apply another group by to combine the records per key.

#### Spark joins

Both tables are large: Sort merge join.
- each executor gets a partition of a large table
- joins start with a reshuffle and then a reduce operation.

One table is large and the other is small: broadcast exchange
- each executor gets a copy of the small table and a partition of the big table

## RDDs: resilient distributed datasets

Dataframes are built on top of RDDs.
Dataframes have schema.

## How tu run Spark in the cloud?
