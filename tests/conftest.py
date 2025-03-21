import boto3
import pytest
from config import ENDPOINT_URL, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

@pytest.fixture(scope="session")
def vk_s3():
    client = boto3.client(
        service_name='s3',
        endpoint_url=ENDPOINT_URL,
        region_name='ru-msk',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    return client