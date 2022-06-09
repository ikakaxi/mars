import unittest
from binascii import unhexlify, hexlify

from pyelliptic import Cipher, OpenSSL


class TestCipher(unittest.TestCase):

    @unittest.skipIf('aes-256-ctr' not in OpenSSL.cipher_algo,
                     'aes-256-ctr is not supported by the SSL library')
    def test_aes256ctr(self):
        ciphername = "aes-256-ctr"

        iv_hex = b"f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"
        iv = unhexlify(iv_hex)
        key_hex = b"603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4"
        key = unhexlify(key_hex)
        plain_hex = b"6bc1bee22e409f96e93d7e117393172a"
        plaintext = unhexlify(plain_hex)

        ctx = Cipher(key, iv, 1, ciphername=ciphername)
        enc = ctx.ciphering(plaintext)
        print(hexlify(enc))

        ctx = Cipher(key, iv, 0, ciphername=ciphername)
        self.assertEqual(plaintext, ctx.ciphering(enc))

    def test_aes256cfb(self):
        ciphername = "aes-256-cfb"
        key_hex = b"603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4"
        key = unhexlify(key_hex)
        iv_hex = b"000102030405060708090A0B0C0D0E0F"
        iv = unhexlify(iv_hex)
        plain_hex = b"6bc1bee22e409f96e93d7e117393172a"
        plaintext = unhexlify(plain_hex)

        ctx = Cipher(key, iv, 1, ciphername=ciphername)
        enc = ctx.ciphering(plaintext)
        print(hexlify(enc))

        ctx = Cipher(key, iv, 0, ciphername=ciphername)
        self.assertEqual(plaintext, ctx.ciphering(enc))

    def test_aes256cbc(self):
        ciphername = "aes-256-cbc"
        iv_hex = b"000102030405060708090A0B0C0D0E0F"
        iv = unhexlify(iv_hex)
        key_hex = b"603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4"
        key = unhexlify(key_hex)
        plain_hex = b"6bc1bee22e409f96e93d7e117393172a"
        plaintext = unhexlify(plain_hex)

        ctx = Cipher(key, iv, 1, ciphername=ciphername)
        enc = ctx.ciphering(plaintext)
        print(hexlify(enc))

        ctx = Cipher(key, iv, 0, ciphername=ciphername)
        self.assertEqual(plaintext, ctx.ciphering(enc))
