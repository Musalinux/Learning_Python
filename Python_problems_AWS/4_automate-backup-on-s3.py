"""
Here we will automate the database backup and upload them to S3 
- Use the python with subprocess to execute databse backup commands.
- boto3 library to upload backup to s3 bucket

subprocess.run(['mysqldump', '-u', 'root', '-p', db_name,'>', dump_file], check=True)
^^ Executes mysqldump command to create database dump and 
store it in dump_file

boto3 client -> create s3 instance.
"""

import subprocess
import boto3

def automate_backup(db_name, s3_bucket, s3_key):
    dump_file = f'/tmp/{db_name}.sql' # create a temporary dump file
    subprocess.run(['mysqldump', '-u', 'root', '-p', db_name,'>', dump_file], check=True)
    
    # Upload database dump file to S3:
    s3 = boto3.client('s3')
    s3.upload_file(dump_file, s3_bucket, s3_key)
    print (f"Uploaded {dump_file} to s3://{s3_bucket}/{s3_key}")

db_name = 'default'
s3_bucket = 'my-bucket'
s3_key =  'test-key'

automate_backup(db_name, s3_bucket, s3_key)