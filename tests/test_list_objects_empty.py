import pytest
import allure
from datetime import datetime
from botocore.exceptions import ClientError

@allure.epic("VK S3 Bucket Smoke Tests")
@allure.feature("ListObjects method")
@allure.story("Verify ListObjects on Empty and Deleted Buckets")
@allure.severity(allure.severity_level.CRITICAL)

def test_list_objects_empty_bucket(vk_s3):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    bucket_name = f"test-bucket-sk-empty-{timestamp}"

    with allure.step("Create a bucket"):
        vk_s3.create_bucket(Bucket=bucket_name)

    try:
        with allure.step("List bucket and verify it's empty"):
            response = vk_s3.list_objects_v2(Bucket=bucket_name)
            print(response)

            assert response['KeyCount'] == 0
            assert 'Contents' not in response


    finally:
        with allure.step("Delete bucket"):
            vk_s3.delete_bucket(Bucket=bucket_name)

    with allure.step("Verify deleted bucket no longer listed"):
        with pytest.raises(ClientError) as exc_info:
            vk_s3.list_objects_v2(Bucket=bucket_name)

        error_response = exc_info.value.response
        error_code = error_response['Error']['Code']

        assert error_code == 'NoSuchBucket'
        print(f"Received expected error : {error_code}")


