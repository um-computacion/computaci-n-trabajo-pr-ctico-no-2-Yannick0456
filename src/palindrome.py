# src/palindrome.py

def clean_text(text):
    return ''.join(char.lower() for char in text if char.isalnum())

def is_palindrome(text):
    cleaned = clean_text(text)
    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    try:
        while True:
            entrada = input("Ingrese una palabra o frase: ")
            if is_palindrome(entrada):
                print(f'"{entrada}" es un palíndromo')
            else:
                print(f'"{entrada}" no es un palíndromo')
    except KeyboardInterrupt:
        print("\nPrograma terminado.")

