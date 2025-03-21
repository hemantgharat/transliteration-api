# Devanagari Transliteration API

## Overview
The **Devanagari Transliteration API** is a FastAPI-based service that converts words written in **ITRANS format** into **Devanagari script**. Additionally, it provides similar word suggestions from a predefined list of Hindi words using fuzzy matching.

## Features
- **Transliteration:** Converts input words from ITRANS format to Devanagari script.
- **Word Suggestions:** Suggests similar words from a Hindi word list using fuzzy matching.
- **CORS Support:** Allows cross-origin requests.
- **FastAPI Integration:** Lightweight and high-performance.

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Clone the Repository
```bash
git clone https://github.com/hemantgharat/transliteration-api.git
cd transliteration-api
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Required Packages
The API relies on the following Python packages:
- `fastapi` - Web framework for building APIs
- `uvicorn` - ASGI server for running FastAPI apps
- `indic-transliteration` - Library for transliteration between scripts
- `rapidfuzz` - Fuzzy string matching for suggestion generation

Install them manually if needed:
```bash
pip install fastapi uvicorn indic-transliteration rapidfuzz
```

## Usage

### Running the API Server
Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload
```
The API will be accessible at `http://127.0.0.1:8000`.

### API Endpoints

#### 1. Transliteration Endpoint
**URL:** `/transliterate/`

**Method:** `GET`

**Query Parameter:**
- `word` (string, required) - The word in ITRANS format (e.g., `kya`, `shakti`).

**Response:**
```json
{
  "input": "kyaa",
  "transliterated": "क्या",
  "suggestions": [
    { "word": "क्या", "score": "100%" },
    { "word": "क्यों", "score": "85%" }
  ]
}
```

## Configuration
### Hindi Word List
Ensure you have a file named `hindi_words.txt` containing a list of Hindi words in Devanagari script, one word per line.

## Author
- **Hemant Gharat**

