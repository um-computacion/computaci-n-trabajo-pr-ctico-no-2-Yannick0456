import unittest
import sys
import os

# Agregar el directorio src al path para poder importar el módulo palindrome
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    
    def test_simple_palindromes(self):
        """Prueba palabras simples que son palíndromos."""
        self.assertTrue(is_palindrome("ana"))
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("oso"))
        self.assertTrue(is_palindrome("reconocer"))
        self.assertTrue(is_palindrome("somos"))
    
    def test_non_palindromes(self):
        """Prueba palabras que no son palíndromos."""
        self.assertFalse(is_palindrome("hola"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("programacion"))
        self.assertFalse(is_palindrome("algoritmo"))
        self.assertFalse(is_palindrome("universidad"))
    
    def test_phrase_palindromes(self):
        """Prueba frases que son palíndromos."""
        self.assertTrue(is_palindrome("Anita lava la tina"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("Madam, I'm Adam"))
    
    def test_phrase_non_palindromes(self):
        """Prueba frases que no son palíndromos."""
        self.assertFalse(is_palindrome("Hola mundo"))
        self.assertFalse(is_palindrome("Esta frase no es un palíndromo"))
        self.assertFalse(is_palindrome("Python es un lenguaje de programación"))
        self.assertFalse(is_palindrome("TDD es una metodología de desarrollo"))
    
    def test_case_insensitive(self):
        """Prueba que la función ignore mayúsculas y minúsculas."""
        self.assertTrue(is_palindrome("Radar"))
        self.assertTrue(is_palindrome("AnA"))
        self.assertTrue(is_palindrome("SoMoS"))
        self.assertTrue(is_palindrome("Oso"))
    
    def test_ignore_punctuation(self):
        """Prueba que la función ignore signos de puntuación."""
        self.assertTrue(is_palindrome("Ana!"))
        self.assertTrue(is_palindrome("¿Radar?"))
        self.assertTrue(is_palindrome("o.s.o"))
        self.assertTrue(is_palindrome("re,co:no;cer"))
    
    def test_ignore_spaces(self):
        """Prueba que la función ignore espacios."""
        self.assertTrue(is_palindrome("a n a"))
        self.assertTrue(is_palindrome("ra d ar"))
        self.assertTrue(is_palindrome("  oso  "))
        self.assertTrue(is_palindrome("re co no cer"))
    
    def test_edge_cases(self):
        """Prueba casos límite."""
        self.assertTrue(is_palindrome(""))  # Cadena vacía
        self.assertTrue(is_palindrome("a"))  # Un solo carácter
        self.assertTrue(is_palindrome(" "))  # Solo espacios
        self.assertTrue(is_palindrome("!"))  # Solo signos de puntuación
    
    def test_alphanumeric_palindromes(self):
        """Prueba palíndromos con números."""
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("a1b2b1a"))
        self.assertTrue(is_palindrome("123 321"))
        self.assertFalse(is_palindrome("123456"))
        self.assertFalse(is_palindrome("a1b2c3"))

if __name__ == '__main__':
    unittest.main()