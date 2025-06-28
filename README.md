# Cloud-Based-Ransomware-Detection-and-Recovery-System-GCP

## Overview
A prototype system leveraging Google Cloud Platform’s free-tier services to detect, mitigate, and recover from ransomware attacks.

## Modules
- **Detection:** Cloud Logging, BigQuery, Cloud Functions
- **Mitigation:** IAM, Firewall, Security Command Center
- **Recovery:** Cloud Storage Versioning, Scheduler, Cloud Functions

## Setup
See [docs/implementation_guide.md](docs/implementation_guide.md) for step-by-step instructions.

## Authors
- Your Name
detection/cloud_function_detect_anomaly.py
python
from google.cloud import bigquery

def detect_anomaly(event, context):
    client = bigquery.Client()
    query = """
    SELECT 
        metric, 
        AVG(value) as mean, 
        STDDEV(value) as stddev,
        (value - AVG(value)) / STDDEV(value) AS z_score
    FROM `your_dataset.logs_table`
    GROUP BY metric, value
    HAVING ABS(z_score) > 3.0
    """
    results = client.query(query).result()
    if results.total_rows > 0:
        # Trigger alert logic here
        print("Anomaly detected!")
recovery/cloud_function_backup.py
python
from google.cloud import storage

def backup_data(event, context):
    # Logic to backup data from buckets
    pass
mitigation/iam_policy_template.yaml
text
bindings:
- members:
  - user:your-email@example.com
  role:roles/viewer
docs/implementation_guide.md
text
# Implementation Guide

## 1. GCP Environment Setup
...

## 2. Detection Configuration
...

## 3. Mitigation Deployment
...

## 4. Recovery Enablement
...

## 5. Testing
...
