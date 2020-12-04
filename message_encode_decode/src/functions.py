import string


class EncoderDecoder:

    ALPHABET = string.ascii_letters
    NUMBERS = string.digits
    PUNCTUATIONS = string.punctuation

    def __init__(self, message, key):
        self.message = message
        self.key = key

    def encrypt(self):
        encrypted_message = ""
        for char in self.message:
            if char.isalpha():
                new_char = self._encryptAlphabet(char)
                encrypted_message += new_char
            elif char.isdigit():
                new_number = self._encryptDigit(char)
                encrypted_message += new_number
            elif char in self.PUNCTUATIONS:
                new_punctuation = self._encryptPunctuation(char)
                encrypted_message += new_punctuation
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt(self):
        decrypted_message = ""
        for char in self.message:
            if char.isalpha():
                new_char = self._decryptAlphabet(char)
                decrypted_message += new_char
            elif char.isdigit():
                new_number = self._decryptDigit(char)
                decrypted_message += new_number
            elif char in self.PUNCTUATIONS:
                new_punctuation = self._decryptPunctuation(char)
                decrypted_message += new_punctuation
            else:
                decrypted_message += char
        return decrypted_message

    def _encryptAlphabet(self, char):
        old_position = self.ALPHABET.index(char)
        new_position = old_position + self.key
        if new_position > (len(self.ALPHABET) - 1):
            new_position %= len(self.ALPHABET)
            char = self.ALPHABET[new_position]
            return char
        char = self.ALPHABET[new_position]
        return char

    def _encryptDigit(self, number):
        old_position = self.NUMBERS.index(number)
        new_position = old_position + self.key
        if new_position > (len(self.NUMBERS) - 1):
            new_position %= len(self.NUMBERS)
            number = self.NUMBERS[new_position]
            return number
        number = self.NUMBERS[new_position]
        return number

    def _encryptPunctuation(self, punctuation):
        old_position = self.PUNCTUATIONS.index(punctuation)
        new_position = old_position + self.key
        if new_position > (len(self.PUNCTUATIONS) - 1):
            new_position %= len(self.PUNCTUATIONS)
            print(new_position)
            punctuation = self.PUNCTUATIONS[new_position]
            return punctuation
        punctuation = self.PUNCTUATIONS[new_position]
        return punctuation

    def _decryptAlphabet(self, char):
        old_position = self.ALPHABET.index(char)
        new_position = old_position - self.key
        if new_position < 0:
            new_position %= len(self.ALPHABET)
            char = self.ALPHABET[new_position]
            return char
        char = self.ALPHABET[new_position]
        return char

    def _decryptDigit(self, number):
        old_position = self.NUMBERS.index(number)
        new_position = old_position - self.key
        if new_position < 0:
            new_position %= len(self.NUMBERS)
            number = self.NUMBERS[new_position]
            return number
        number = self.NUMBERS[new_position]
        return number

    def _decryptPunctuation(self, punctuation):
        old_position = self.PUNCTUATIONS.index(punctuation)
        new_position = old_position - self.key
        if new_position < 0:
            new_position %= len(self.PUNCTUATIONS)
            punctuation = self.PUNCTUATIONS[new_position]
            return punctuation
        punctuation = self.PUNCTUATIONS[new_position]
        return punctuation

