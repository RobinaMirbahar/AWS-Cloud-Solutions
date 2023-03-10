To write data to S3 in Parquet format from inside an AWS Lambda function, you can use the pyarrow library in Python or the aws-sdk library in TypeScript.

Here's an example implementation in Python:

## Usage/Examples

import pyarrow as pa
import pyarrow.parquet as pq
import boto3
import os

def write_to_parquet(data, s3_bucket, s3_key):
    # Create a PyArrow Table from your data
    table = pa.Table.from_pandas(data)

    # Write the table to a Parquet file in memory
    buffer = pa.BufferOutputStream()
    pq.write_table(table, buffer)

    # Create an S3 client and upload the Parquet file
    s3 = boto3.client('s3')
    s3.upload_fileobj(buffer, s3_bucket, s3_key)
    
    
This code creates a PyArrow Table from your data, writes it to a Parquet file in memory using the pq.write_table() method, 
and then uploads the file to S3 using the s3.upload_fileobj() method.

To append to an existing Parquet file, you can use the pq.ParquetWriter() method with the append=True option, like this:

def append_to_parquet(data, s3_bucket, s3_key):
    # Create a PyArrow Table from your data
    table = pa.Table.from_pandas(data)

    # Append the table to an existing Parquet file in S3
    s3 = boto3.client('s3')
    with pq.ParquetWriter('s3://{}/{}'.format(s3_bucket, s3_key), table.schema, compression='snappy', filesystem=s3, append=True) as writer:
        writer.write_table(table)
        
        
This code opens an existing Parquet file in S3 using the pq.ParquetWriter() method with append=True, 
and then writes the PyArrow Table to it using the writer.write_table() method.

