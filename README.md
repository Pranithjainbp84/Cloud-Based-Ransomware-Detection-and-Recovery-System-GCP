# Cloud-Based-Ransomware-Detection-and-Recovery-System-GCP

## Overview
A prototype system leveraging Google Cloud Platform’s free-tier services to detect, mitigate, and recover from ransomware attacks.

## Modules
- **Detection:** Cloud Logging, BigQuery, Cloud Functions
- **Mitigation:** IAM, Firewall, Security Command Center
- **Recovery:** Cloud Storage Versioning, Scheduler, Cloud Functions


# Implementation Guide

## 1. GCP Environment Setup
- Create a new GCP project.
- Enable required APIs: Cloud Logging, BigQuery, Cloud Functions, Cloud Storage, IAM, Security Command Center, Cloud Scheduler.

## 2. Detection Configuration
- **Cloud Logging:**  
  - Enable logging for all critical resources (VMs, Storage, IAM, etc.).
- **BigQuery:**  
  - Set up a log sink to export logs from Cloud Logging to BigQuery.
- **Cloud Functions:**  
  - Deploy a function that queries BigQuery for anomalies (e.g., spikes in file access or deletions).
  - Use statistical methods (e.g., z-score) to detect outliers.
- **Alerting:**  
  - Integrate Cloud Functions with SendGrid/Twilio (or Pub/Sub) to send email/SMS alerts on detection.

## 3. Mitigation Deployment
- **IAM:**  
  - Apply least-privilege roles using IAM policies.
  - Regularly review and audit permissions.
- **Firewall Rules:**  
  - Restrict access to critical resources by IP and port.
- **Security Command Center:**  
  - Enable and configure to monitor for misconfigurations, exposed resources, and suspicious activity.

## 4. Recovery Enablement
- **Cloud Storage Versioning:**  
  - Enable object versioning on all important buckets.
- **Cloud Scheduler:**  
  - Schedule regular backups using Cloud Functions.
- **Cloud Functions (Recovery):**  
  - Deploy functions to restore data from previous versions or backups.

## 5. Testing
- Simulate ransomware behavior (e.g., mass file encryption or deletion) in a test environment.
- Verify:
  - Detection triggers alerts.
  - IAM/firewall rules limit spread.
  - Recovery functions restore data from backups/versions.

### References
- [Google Cloud: Mitigating ransomware attacks](https://cloud.google.com/architecture/security/mitigating-ransomware-attacks)[1]
- [Disaster Recovery Planning Guide (GCP)](https://cloud.google.com/architecture/dr-scenarios-planning-guide)[2]
- [ScaleSec: Cloud-Native Ransomware Protection in GCP](https://scalesec.com/blog/cloud-native-ransomware-protection-gcp/)[3]

