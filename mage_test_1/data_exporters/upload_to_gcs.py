from google.cloud import storage
from pandas import DataFrame
from datetime import datetime
import pytz
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:

    bucket_name = os.getenv('GCS_BUCKET')

    now = datetime.utcnow()
    pt = pytz.timezone("America/Los_Angeles")
    now_pst = pytz.utc.localize(now).astimezone(pt)

    object_key = f'test_file_{now_pst.strftime("%Y-%m-%d_%H%M")}.csv'

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(object_key)

    blob.upload_from_string(df.to_csv())

    print(
        f"df uploaded to {bucket}/{object_key}."
    )
