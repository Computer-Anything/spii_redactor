# Flask PII Redactor

This project is a Flask web application that allows users to upload an image file and receive a redacted version of the text extracted from that image. The application uses EasyOCR for text extraction and SpaCy for PII detection and redaction.

## Features

- Upload an image file.
- Extract text from the uploaded image.
- Detect and redact Personally Identifiable Information (PII) such as names, emails, phone numbers, and zip codes.
- Display the original image alongside the redacted text.

---

## Inspiration

The inspiration for this project came from an earlier Jupyter Notebook implementation that demonstrated the process of extracting text from images, detecting PII using SpaCy, and redacting sensitive information. This notebook served as a prototype and proof of concept, which was then extended into a full-fledged Flask web application for ease of use and accessibility.

---

## Project Structure

```
flask-pii-redactor
├── app
│   ├── __init__.py          # Initializes the Flask application
│   ├── routes.py            # Contains route definitions for the application
│   ├── static
│   │   └── styles.css       # CSS styles for the application
│   └── templates
│       ├── base.html        # Base template for the application
│       ├── index.html       # Main page for file uploads
│       └── result.html      # Page to display results after processing
├── uploads                   # Directory for temporarily storing uploaded images
├── requirements.txt          # Lists project dependencies
├── run.py                   # Entry point for running the Flask application
└── README.md                # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-pii-redactor
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python run.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Upload an image file containing text.

4. View the original image and the redacted text on the results page.

## Dependencies

- Flask
- EasyOCR
- SpaCy
- Other necessary libraries listed in `requirements.txt`

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
