## What is analytics engineering?

Data domain development
1. Massively parallel processing databases (BigQuery, Snowflake, Redshift) reduced the cost of storing and processing data
2. Data pipeline as a service (Fivetran or stitch) simplified the ETL process
3. SQL first tools (Looker)
4. Version controls systems
5. Self service analytics
6. Data governance

Analytics engineer fills the gap between data engineers and data analyst (scientists)

## Data modeling concepts

ETL: extracting the sources then transforming then loading
More stable data analysis, higher storage and compute costs

ELT: Transforming the data once it is in the DWH.
Faster and mroe flexible data analysis, lower cost and lower maintenance.

ELT has become very popular thanks to cloud paltforms because storage is cheap and compute is scalable. It is easier and faster to trasnform the data once it is in the datawarehouse.
Fivetran is a popular tool to extract data from any platform (Salesforce for example) and load it in a datawarehouse.

Kimball's dimension modeling
- deliver data understandable to the business user
- deliver fast query performance
- There can be redundant data
Other approaches: Bill Inmon and data vault.

Kimball's dimensional modeling
- facts table (verbs)
- dimension tables (nouns)

- stage area (raw data) not exposed to everyone
- process area (raw to data models), not exposed to everyone
- presentation area, exposed to business stakeholders.

## What is dbt?
Data Build Tool
Allows anyone that knows SQL to deploy analytics code following software engineering best practices like modularity, portability, CI/CD and documentation.

It has become the industry standard for data transformation.

dbt allows you to develop and apply the trasnformation inside the data warehouse to go from raw data to optimized format ready for consumption.

dbt:
- develop
- version control, CI/CD
- tests and documentation

Materialization strategies
- table: drop table if already exists and create the table 
- view:
- incremental: only the latest data 
- ephemeral

#### Tests in dbt
Tests in dbt are esentially a SQL query. It returns the number of records that fail the tests.

Tests are written in the .yml file.

#### Documentation in dbt
The documentation can be rendered as a website.
The documentation is written in the .yml file.

#### Deployment
Deployment workflow:
- develop in user branch
- open a pull request to merge into the main branch
- merge to main
- run the new models in the prod env using the main branch
- schedule the models

A deployment env will usually have a different schema in our data warehouse and ideally a different user.

You can schedule jobs to run in prod.


## dbt CLI

Install packages `dbt deps`
`dbt run --select filename`