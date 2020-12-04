from src.functions import EncoderDecoder


class Test_EncoderDecoder:
    encode_message = EncoderDecoder("hello", 256)
    decode_message = EncoderDecoder("dahhk", 256)
    char_encode = EncoderDecoder("a", 4)
    char_decode = EncoderDecoder("A", 4)

    def test_encrypt(self):
        assert self.encode_message.encrypt() == "dahhk"

    def test_decrypt(self):
        assert self.decode_message.decrypt() == "hello"

    def test__encryptAlphabet(self):
        assert self.encode_message._encryptAlphabet("A") == "w"

    def test__encryptDigit(self):
        assert self.encode_message._encryptDigit("5") == "1"

    def test__encryptPunctutation(self):
        assert self.encode_message._encryptPunctuation("@") == "@"

    def test__decryptAlphabet(self):
        assert self.decode_message._decryptAlphabet("w") == "A"

    def test__decryptDigit(self):
        assert self.decode_message._decryptDigit("1") == "5"

    def test__decryptPunctutation(self):
        assert self.decode_message._decryptPunctuation(".") == "."