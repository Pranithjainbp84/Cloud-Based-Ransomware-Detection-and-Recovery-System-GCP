SELECT 
    metric, 
    AVG(value) as mean, 
    STDDEV(value) as stddev,
    (value - AVG(value)) / STDDEV(value) AS z_score
FROM `your_dataset.logs_table`
GROUP BY metric, value
HAVING ABS(z_score) > 3.0
