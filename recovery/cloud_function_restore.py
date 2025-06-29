from google.cloud import storage

def restore_data(bucket_name, object_name, version_id):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(object_name, generation=version_id)
    blob.download_to_filename("restored_file")
