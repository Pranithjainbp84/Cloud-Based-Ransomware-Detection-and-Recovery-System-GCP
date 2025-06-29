#!/bin/bash
# Simulate ransomware-like file renaming in a test bucket

gsutil mv gs://test-bucket/*.txt gs://test-bucket/encrypted/
