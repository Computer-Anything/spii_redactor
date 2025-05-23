# PII Detection and Redaction Notebook

This Jupyter Notebook demonstrates the process of detecting and redacting Personally Identifiable Information (PII) from text extracted from images. It uses EasyOCR for Optical Character Recognition (OCR) and SpaCy for Named Entity Recognition (NER) to identify and redact sensitive information such as names, emails, phone numbers, and zip codes.

## Features

- **OCR with EasyOCR**: Extract text from images.
- **PII Detection with SpaCy**: Identify sensitive entities like names, emails, phone numbers, and zip codes.
- **PII Redaction**: Redact sensitive information using SpaCy and regex patterns.
- **Visualization**: Display the original image alongside the redacted text.

## How to Use

1. Install the required libraries:
   ```bash
   pip install easyocr spacy torch matplotlib pillow
