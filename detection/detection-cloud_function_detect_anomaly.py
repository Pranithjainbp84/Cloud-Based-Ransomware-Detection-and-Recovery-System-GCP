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
