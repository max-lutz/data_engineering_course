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