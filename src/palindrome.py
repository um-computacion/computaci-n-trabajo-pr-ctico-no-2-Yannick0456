# src/palindrome.py

def clean_text(text):
    return ''.join(char.lower() for char in text if char.isalnum())


