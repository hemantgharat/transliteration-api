import re
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from indic_transliteration.sanscript import transliterate, ITRANS, DEVANAGARI
from rapidfuzz import process

app = FastAPI(
    title="Devanagari Transliteration API",
    description="An API that transliterates words to Devanagari script and provides similar word suggestions.",
    version="1.0.0",
    contact={
        "name": "Hemant Gharat",
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_hindi_words():
    """
    Loads a list of Devanagari words from a text file.
    """
    with open("hindi_words.txt", "r", encoding="utf-8") as f:
        return set(f.read().splitlines())

hindi_words = load_hindi_words()

def extract_first_hindi_character(word: str) -> str:
    """
    Extracts the first Devanagari character from a word (excluding matras).
    """
    hindi_pattern = r"[\u0900-\u097F]"
    match = re.search(hindi_pattern, word)
    return match.group(0) if match else ""

@app.get("/transliterate/", summary="Transliterate ITRANS to Devanagari", tags=["Transliteration"])
def transliterate_word(word: str):
    """
    Converts a word written in **ITRANS format** to **Devanagari script** and suggests similar words.
    
    - **word**: Input word in ITRANS format (e.g., "kya", "kyun", "shakti").
    
    **Returns:**  
    - `input`: The original word.
    - `transliterated`: The word converted to Devanagari script.
    - `suggestions`: A list of similar words in Devanagari script with scores.
    """
    transliterated_word = transliterate(word, ITRANS, DEVANAGARI)
    suggestions = process.extract(transliterated_word, hindi_words, limit=10)
    threshold = 40
    first_character = extract_first_hindi_character(transliterated_word)
    filtered_suggestions = [
        {"word": s[0], "score": f"{s[1]}%"}
        for s in suggestions
        if s[1] >= threshold and s[0].startswith(first_character)
    ]

    return {
        "input": word,
        "transliterated": transliterated_word,
        "suggestions": filtered_suggestions
    }
