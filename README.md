# VK Cloud S3 Bucket Smoke Tests

This project contains **smoke tests** for the VK Cloud S3 `ListObjects` [API](https://cloud.vk.com/docs/tools-for-using-services/api/api-spec/s3-rest-api/bucket-api#listobjects
) using `pytest` and `boto3==1.35.99`.  
Allure is used for generating test reports.

---

## Prerequisites

- Python 3.12+
- Install the required Python packages:
  ```
  pip install pytest boto3==1.35.99 allure-pytest
  ```
- Install Allure CLI (for generating reports):
  - MacOS: `brew install allure`

---

## Run Tests

Run pytest and collect Allure results:
```
pytest --alluredir=allure-results
```

---

## View the Allure Report

1. Serve live report:
   ```
   allure serve allure-results
   ```

---

## Credentials

Make sure you have your VK Cloud S3 credentials configured in:  
`tests/config.py`:
```
ENDPOINT_URL = 'https://hb.ru-msk.vkcloud-storage.ru'
AWS_ACCESS_KEY_ID = 'your-access-key'
AWS_SECRET_ACCESS_KEY = 'your-secret-key'
```

---
