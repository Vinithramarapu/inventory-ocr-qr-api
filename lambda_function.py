import json
import boto3
import base64
from pyzbar.pyzbar import decode
from PIL import Image
import io

def lambda_handler(event, context):
    textract = boto3.client('textract')
    s3 = boto3.client('s3')

    bucket = event['bucket']
    key = event['key']

    # OCR using Textract
    response = textract.detect_document_text(
        Document={'S3Object': {'Bucket': bucket, 'Name': key}}
    )
    text = " ".join([item["DetectedText"] for item in response["Blocks"] if item["BlockType"] == "LINE"])

    # Get image from S3 and decode QR code
    obj = s3.get_object(Bucket=bucket, Key=key)
    img_data = obj['Body'].read()
    img = Image.open(io.BytesIO(img_data))
    qr_data = [barcode.data.decode('utf-8') for barcode in decode(img)]

    return {
        'statusCode': 200,
        'body': json.dumps({
            'extracted_text': text,
            'qr_codes': qr_data
        })
    }
