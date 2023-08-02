MORSE_TO_ENGLISH = {
    "._": "A", "_...": "B", "_._.": "C", "_..": "D", ".": "E", ".._.": "F", "__.": "G", "....": "H", "..": "I",
    ".___": "J", "_._": "K", "._..": "L", "__": "M", "_.": "N", "___": "O", ".__.": "P", "__._": "Q", "._.": "R",
    "...": "S", "_": "T", ".._": "U", "..._": "V", ".__": "W", "_.._": "X", "_.__": "Y", "__..": "Z", ".____": "1",
    "..___": "2", "...__": "3", "...._": "4", ".....": "5", "_....": "6", "__...": "7", "___..": "8", "____.": "9",
    "_____": "0", "__..__": ",", "._._._": ".", "..__..": "?", "_._._.": ";", "___...": ":", "_.._.": "/",
    "_...._": "-", ".____.": "'", "._.._.": "\"", "..__._": "_", "_.__.": "(", "_.__._": ")", "_..._": "=",
    "._._.": "+", " ": " ", "": ""
}

ENGLISH_TO_MORSE = {v: k for k, v in MORSE_TO_ENGLISH.items()}


class ParseError(Exception):
    pass


def english_to_morse(text):
    """
    Converts a string of valid English characters to Morse code.
    :param text: English string.
    :return: Converted Morse code representation of English input string.
    """
    text = text.upper()
    if not all(char in ENGLISH_TO_MORSE for char in text):
        raise ParseError("Input contains invalid characters for conversion to Morse.")
    # Morse chars separated by space, words separated by three
    # Trailing space to accommodate parsing of incomplete words
    return ' '.join(ENGLISH_TO_MORSE[char] for char in text) + ' '


def morse_to_english(text):
    """
    Converts a string of valid Morse characters to English.
    :param text: Morse string.
    :return: Converted English interpretation of Morse input string.
    """
    words = text.split('   ')  # Three spaces between words
    if not all(char in MORSE_TO_ENGLISH for word in words for char in word.split(' ')):
        raise ValueError("Input contains invalid characters for conversion to English.")
    return ' '.join(''.join(MORSE_TO_ENGLISH[char] for char in word.split(' ')) for word in words)
