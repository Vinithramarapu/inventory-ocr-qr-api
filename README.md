# Inventory OCR + QR Code API

This project demonstrates an AWS-based inventory tracking API using OCR (via Amazon Textract) and QR code detection.

## Features

- Upload image to S3
- Trigger AWS Lambda
- Extract text using Textract (OCR)
- Detect QR codes using Pyzbar
- Respond with JSON output

## Tech Stack

- AWS S3
- AWS Lambda (Python)
- Amazon Textract
- API Gateway
- pyzbar (for QR code decoding)

## Setup Instructions

1. Deploy the Lambda function using AWS Console or CLI
2. Connect API Gateway to the Lambda
3. Upload an image to S3 bucket and test

