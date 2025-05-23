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
   ```

2. Download the SpaCy language model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

3. Open the notebook `pii_redaction_ocr.ipynb` in Jupyter Notebook or JupyterLab.

4. Follow the steps in the notebook to:
   - Extract text from an image.
   - Detect and redact PII.
   - Visualize the results.

5. Replace the `image_path` variable with the path to your image file to test with your own data.

## Example Output

- **Original Image**: Displays the uploaded image.
- **Redacted Text**: Shows the text with sensitive information redacted.

## Future Plans

This notebook serves as a prototype for a Flask web application that will allow users to upload images via a web interface and receive redacted results. Stay tuned for the Flask app implementation!

## Dependencies

- EasyOCR
- SpaCy
- Torch
- Matplotlib
- Pillow

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
```
