class EnglishMessage:
    
    def __init__(self, message):
        self.message = message
        self.letter_to_morse = {'a': '.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.',
                    'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 
                    'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.-', 
                    's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 
                    'y':'-.--', 'z':'--..', '0':'-----', '1':'.----', '2':'..---', 
                    '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', 
                    '8':'---..', '9':'----.', ' ':'/'
}


    def morse_encoded(self):
        morse = []

        for letter in self.message:
            letter = letter.lower()
            morse.append(self.letter_to_morse[letter])
        morse_message = " ".join(morse)
        return morse_message


class MorseMessage:
    def __init__(self, message):
        self.message = message
        letter_to_morse = {'a': '.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.',
                    'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 
                    'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.-', 
                    's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 
                    'y':'-.--', 'z':'--..', '0':'-----', '1':'.----', '2':'..---', 
                    '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', 
                    '8':'---..', '9':'----.', ' ':'/'
                }
        # We need to invert the dictionary. This will create a dictionary that can go from the morse back to the letter
        self.morse_to_letter = {}
        for letter in letter_to_morse:
            morse = letter_to_morse[letter]
            self.morse_to_letter[morse] = letter

    def morse_decoded(self):
        english = []
        # Now we cannot read by letter. We know that morse letters are seperated by a space, so we split the morse string
        # by spaces
        morse_letters = self.message.split(" ")

        for letter in morse_letters:
            english.append(self.morse_to_letter[letter])

        plain_message = "".join(english)
        return plain_message
  



