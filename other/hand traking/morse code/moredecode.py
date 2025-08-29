# Morse code dictionary
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B',
    '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K',
    '.-..': 'L', '--': 'M', '-.': 'N',
    '---': 'O', '.--.': 'P', '--.-': 'Q',
    '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W',
    '-..-': 'X', '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8',
    '----.': '9'
}

def morse_to_text(morse_code: str) -> str:
    """
    Convert Morse code into plain text.
    Words are separated by ' / ' or 3 spaces.
    Letters are separated by spaces.
    """
    words = morse_code.strip().replace("   ", " / ").split(" / ")
    decoded_words = []

    for word in words:
        letters = word.split()
        decoded_letters = [MORSE_CODE_DICT.get(letter, '?') for letter in letters]
        decoded_words.append("".join(decoded_letters))

    return " ".join(decoded_words)

# Example usage:
file = "hand traking/morse code/morse.txt"
with open(file) as f:
    morse = f.read()
    print(morse)

print(morse_to_text(morse))  # Output: SOS HELP
