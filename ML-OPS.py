🚀 AWS Glue & Step Functions Code for Credit Card Fraud Detection (MLOps Project)
I'll provide:
✅ AWS Glue ETL script → Cleans & preprocesses transaction data for fraud detection.
✅ Step Functions workflow → Automates data pipeline (extract, process, classify fraud, store).
✅ EventBridge trigger → Starts workflow when new transactions arrive in S3.

📌 Workflow Overview
🔹 Real-Time Credit Card Fraud Detection Using AWS
1️⃣ New transactions uploaded to S3 → EventBridge triggers Step Functions.
2️⃣ Step Functions executes AWS Glue → Cleans, transforms & prepares data.
3️⃣ Step Functions calls SageMaker Endpoint → Classifies transactions as fraud/not fraud.
4️⃣ Stores fraud transactions separately in S3 / DynamoDB for alerting.
5️⃣ Triggers SNS notification if fraud detected (Alert Security Team).

✅ Architecture Flow

S3 (New Transactions) → EventBridge → Step Functions
  ↳ AWS Glue (ETL) → Preprocessed Data → SageMaker Model (Fraud Detection)
  ↳ If fraud detected → Store in S3 / DynamoDB → SNS Alert
🔹 Step 1: AWS Glue ETL Script (Preprocessing Transactions)
📌 Cleans raw transaction data & prepares it for fraud detection model.

import sys
import boto3
import pandas as pd
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Glue Context
spark = SparkSession.builder.appName("CreditCardFraudDetectionETL").getOrCreate()
glueContext = GlueContext(spark)

# Read transaction data from S3
s3_bucket = "your-raw-transactions-bucket"
input_path = f"s3://{s3_bucket}/raw_transactions.csv"
df = spark.read.csv(input_path, header=True, inferSchema=True)

# Data Cleaning & Feature Engineering
df_cleaned = df.select(
    col("TransactionID"),
    col("Amount").cast("float"),
    col("Location"),
    col("CardType"),
    col("Timestamp"),
    col("IsFraud").cast("int")  # Target label for training
)

# Save preprocessed data to S3
output_bucket = "your-preprocessed-transactions-bucket"
output_path = f"s3://{output_bucket}/processed_transactions/"
df_cleaned.write.mode("overwrite").parquet(output_path)

print("Preprocessing complete. Data saved to S3.")
✅ What This Glue Script Does:
✔ Reads raw transactions from S3
✔ Cleans & formats data (casting columns correctly)
✔ Saves processed transactions back to S3

🔹 Step 2: Step Functions Workflow (ETL + Fraud Detection)
📌 This Step Functions state machine:
✅ Starts AWS Glue ETL job
✅ Calls SageMaker fraud detection model
✅ Stores results in S3 / DynamoDB
✅ Sends an SNS alert if fraud is detected

Step Functions State Machine (JSON)
{
  "Comment": "Credit Card Fraud Detection Workflow",
  "StartAt": "StartGlueETL",
  "States": {
    "StartGlueETL": {
      "Type": "Task",
      "Resource": "arn:aws:states:::glue:startJobRun",
      "Parameters": {
        "JobName": "CreditCardFraudETL"
      },
      "Next": "InvokeSageMaker"
    },
    "InvokeSageMaker": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sagemaker:invokeEndpoint",
      "Parameters": {
        "EndpointName": "fraud-detection-endpoint",
        "Body.$": "$.preprocessedData"
      },
      "Next": "CheckFraudResult"
    },
    "CheckFraudResult": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.prediction",
          "NumericEquals": 1,
          "Next": "StoreFraudulentTransaction"
        }
      ],
      "Default": "StoreNonFraudTransaction"
    },
    "StoreFraudulentTransaction": {
      "Type": "Task",
      "Resource": "arn:aws:states:::dynamodb:putItem",
      "Parameters": {
        "TableName": "FraudulentTransactions",
        "Item": {
          "TransactionID": { "S.$": "$.TransactionID" },
          "Amount": { "N.$": "$.Amount" },
          "Location": { "S.$": "$.Location" }
        }
      },
      "Next": "SendSNSAlert"
    },
    "StoreNonFraudTransaction": {
      "Type": "Task",
      "Resource": "arn:aws:states:::s3:putObject",
      "Parameters": {
        "Bucket": "your-safe-transactions-bucket",
        "Key.$": "States.Format('transactions/{TransactionID}.json', $.TransactionID)",
        "Body.$": "$"
      },
      "End": true
    },
    "SendSNSAlert": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sns:publish",
      "Parameters": {
        "TopicArn": "arn:aws:sns:us-east-1:123456789012:FraudAlerts",
        "Message.$": "States.Format('Fraud detected! Transaction ID: {}', $.TransactionID)"
      },
      "End": true
    }
  }
}
✅ How This Works:
✔ Starts AWS Glue ETL Job → Cleans transactions.
✔ Invokes SageMaker model → Classifies transactions.
✔ Checks if fraud detected → If yes, store in DynamoDB & send SNS alert.
✔ If no fraud, store transaction safely in S3.

🔹 Step 3: Triggering the Workflow Using EventBridge
📌 Trigger Step Functions when new transactions arrive in S3.
✅ EventBridge Rule Configuration (AWS CLI)

aws events put-rule --name "TriggerFraudWorkflow" --event-pattern '{
  "source": ["aws.s3"],
  "detail-type": ["Object Created"],
  "detail": {
    "bucket": {
      "name": ["your-raw-transactions-bucket"]
    }
  }
}'

✅ Target the Step Functions Workflow

aws events put-targets --rule "TriggerFraudWorkflow" --targets '[{
  "Id": "1",
  "Arn": "arn:aws:states:us-east-1:123456789012:stateMachine:CreditCardFraudDetection"
}]'

📌 How This Works:
✔ EventBridge detects new file uploads to S3.
✔ Triggers Step Functions → Starts ETL + Fraud Detection Pipeline.

🚀 Summary
Component	What It Does
AWS Glue	Cleans & processes raw transaction data for fraud detection.
Step Functions	Manages workflow: ETL → Model Inference → Fraud Check.
SageMaker	Detects fraudulent transactions using a trained ML model.
DynamoDB	Stores fraudulent transactions for further analysis.
S3	Stores safe transactions securely.
SNS	Sends fraud alerts to security teams.
EventBridge	Detects new transactions & triggers workflow.
🚀 Why This is Interview-Ready?
✔ Shows strong AWS architecture understanding.
✔ Demonstrates ETL, Event-Driven & ML workflows.
✔ Covers AWS Glue, Step Functions, EventBridge, SageMaker, DynamoDB.

📌 Potential Interview Question:
🧐 "How would you modify this workflow for real-time fraud detection?"
✅ Answer: Use Kinesis Data Streams instead of S3 + Glue for low-latency fraud detection.