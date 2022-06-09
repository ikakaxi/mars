import unittest
from binascii import hexlify

from pyelliptic import ECC


class TestCIES(unittest.TestCase):

    def test_ecies(self):
        alice = ECC()
        plaintext = b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ciphertext = alice.encrypt(plaintext, alice.get_pubkey())
        print(hexlify(ciphertext))
        self.assertEqual(plaintext, alice.decrypt(ciphertext))

    def test_ecies_rc4(self):
        alice = ECC()
        plaintext = b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ciphertext = alice.encrypt(plaintext, alice.get_pubkey(),
                                 ciphername="rc4")
        print(hexlify(ciphertext))
        self.assertEqual(plaintext, alice.decrypt(ciphertext, ciphername="rc4"))
