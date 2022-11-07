import os 
import requests
from django.core.files import File

OCR_API_TOKEN_HEADER = 'randomid'
OCR_API_ENDPOINT = 'http://randomid2'


def extract_text_via_ocr_service(file_obj: File=None):
    data = {}
    if OCR_API_ENDPOINT is None:
        return data
    if OCR_API_TOKEN_HEADER is None:
        return data
    if file_obj is None:
        return data
    headers = {
        "Authorization": f"Bearer {OCR_API_TOKEN_HEADER}"
    }
    with file_obj.open("rb") as f:
        r = requests.post(OCR_API_ENDPOINT, files={"file", file_obj}, headers=headers)
        if r.status_code in range(200, 299):
            if r.headers.get("content-type") == 'application/json':
                data = r.json()
    return data