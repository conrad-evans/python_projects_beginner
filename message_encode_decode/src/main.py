from src.functions import EncoderDecoder


def run():
    message = input("Enter message to be decode/encode: ")
    key = int(input("Enter secret key: "))
    print("\n")

    encode_decode = EncoderDecoder(message, key)
    encrypted_message = encode_decode.encrypt()

    print("[Encrypted] : " + encrypted_message)
    print("[Decrypted] : " + EncoderDecoder(encrypted_message, key).decrypt())
