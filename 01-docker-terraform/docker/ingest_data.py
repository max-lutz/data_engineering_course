#!/usr/bin/env python
# coding: utf-8

import os
import argparse
from time import time
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

DTYPE = {
    'VendorID': 'Int64',
    'tpep_pickup_datetime': 'object',
    'tpep_dropoff_datetime': 'object',
    'store_and_fwd_flag': 'object',
    'RatecodeID': 'float64',
    'PULocationID': 'int64',
    'DOLocationID': 'int64',
    'passenger_count': 'Int64',
    'trip_distance': 'float64',
    'fare_amount': 'float64',
    'extra': 'float64',
    'mta_tax': 'float64',
    'tip_amount': 'float64',
    'tolls_amount': 'float64',
    'ehail_fee': 'float64',
    'improvement_surcharge': 'float64',
    'total_amount': 'float64',
    'payment_type': 'Int64',
    'trip_type': 'Int64',
    'congestion_surcharge': 'float64',
    'tolls_amount': 'float64',
}


def download_file(url: str):
    if url.endswith('.csv.gz'):
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output.csv'

    os.system(f"wget {url} -O {csv_name}")
    return csv_name


def get_table_row_count(db: str, user: str, host: str, password: str, table_name: str):
    conn = psycopg2.connect(f"dbname='{db}' user='{user}' host='{host}' password='{password}'")
    cur = conn.cursor()
    return cur.rowcount


def create_table_in_db(engine, table_name: str, df: pd.DataFrame):
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')


def ingest_data(user: str, password: str, host: str, port: int, db: str, table_name: str, url: str):
    """_summary_

    Args:
        user (str): _description_
        password (str): _description_
        host (str): _description_
        port (int): _description_
        db (str): _description_
        table_name (str): _description_
        url (str): _description_
    """
    filepath = download_file(url)

    print("File downloaded")

    print('Creating postgres engine')

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df_iter = pd.read_csv(filepath, iterator=True, chunksize=100_000, dtype=DTYPE, compression='gzip',
                          parse_dates=['tpep_pickup_datetime', 'tpep_dropoff_datetime'])

    for df in df_iter:
        t_start = time()
        if not get_table_row_count(db, user, host, password, table_name):
            create_table_in_db(engine, table_name, df)
        df.to_sql(name=table_name, con=engine, if_exists='append')
        print('inserted another chunk, took %.3f second' % (time() - t_start))

    print("Finished ingesting data into the postgres database")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the csv file')

    args = parser.parse_args()

    ingest_data(args.user, args.password, args.host, args.port, args.db, args.table_name, args.url)
