class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, func, text):
        result = ""
        key_index = 0
        for l in text:
            if l in self.alphabet:
                result += self.alphabet[(self.alphabet.index(l) + self.alphabet.index(self.key[key_index])) % len(self.alphabet)]
            else:
                result += l
            key_index += 1
            if key_index > len(self.key):
                key_index = 0
        return result

    def decode(self, text):
        result = ""
        key_index = 0
        for l in text:
            if l in self.alphabet:
                result += self.alphabet[
                    (self.alphabet.index(l) - self.alphabet.index(self.key[key_index])) % len(self.alphabet)]
            else:
                result += l
            key_index += 1
            if key_index > len(self.key):
                key_index = 0
        return result
