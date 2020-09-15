# most code ares borrowed from the follwing websites with modification
# website1:https://github.com/the-javapocalypse/Python-File-Encryptor/blob/master/script.py
# website2:https://gist.github.com/mimoo/11383475

from Crypto import Random
from Crypto.Cipher import AES
import hashlib
import argparse

class Encryptor:
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        #os.remove(file_name)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        if file_name[-3:] == "enc":
            with open(file_name[:-4], 'wb') as fo:
                fo.write(dec)
        else:
            with open(file_name+".dec", 'wb') as fo:
                fo.write(dec)
        #os.remove(file_name)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--encrypt", action="store_true", default=False, help='encrypt file')
    parser.add_argument("-d", "--decrypt", action="store_true", default=False, help='decrypt file')
    parser.add_argument('-input', action='store', help='input file path')
    parser.add_argument('-key', action='store', help='password used to encrypt or decrypt')
    args = parser.parse_args()
    if not (args.encrypt or args.decrypt):
        parser.error('No action requested, add -e for encrypt or -d for decrypt')

    keyh = hashlib.sha256(args.key.encode('utf-8')).digest()
    myenc = Encryptor(keyh)
    if args.encrypt:
        #print("start encryption...", end='')
        print("start encryption...")
        myenc.encrypt_file(args.input)
        print("encryption succeed...")
    else:
        #print("start decryption...", end='')
        print("start decryption...")
        myenc.decrypt_file(args.input)
        print("decryption succeed...")

if __name__ == "__main__":
    main()
