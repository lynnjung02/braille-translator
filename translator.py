import sys

braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO..O', 't': '.OOO.O',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO..', 'x': 'OO..OO', 'y': 'OO.OO',
    'z': 'O..OOO', 'space': '......',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    'capital follows': '.....0', 'decimal follows': '.0...0', 'number follows': '.0.000', '.': '..00.0', 
    ',': '..0...', '?': '..0.00', '!': '..000.', ':': '..00..', ';': '..0.0.',
    '-': '....00', '/': '.0..0.', '<': '.00..0', '>': '0..00.', '(': '0.0..0',
    ')': '.0.00.'
}

def english_to_braille(text):
    return ''.join(braille_dict[char.lower()] for char in text if char in braille_dict)

def braille_to_english(braille):
    inv_braille_dict = {v: k for k, v in braille_dict.items()}
    words = braille.split('......')
    result = []
    for word in words:
        letters = [word[i:i+6] for i in range(0, len(word), 6)]
        translated = ''.join(inv_braille_dict.get(letter, '') for letter in letters)
        result.append(translated)
    return ' '.join(result)

def main():
    if len(sys.argv) < 2:
        return
    input_text = sys.argv[1]
    if all(c in "O." for c in input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))

if __name__ == "__main__":
    main()