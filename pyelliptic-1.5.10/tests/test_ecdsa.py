import unittest
from binascii import hexlify

from pyelliptic import ECC


class TestECDSA(unittest.TestCase):

    def test_ecdsa(self):
        alice = ECC()
        plaintext = b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sig = alice.sign(plaintext)
        print(hexlify(sig))
        res = ECC(pubkey_x=alice.pubkey_x,
                  pubkey_y=alice.pubkey_y).verify(sig, plaintext)
        self.assertTrue(res)

    def test_ecdsa2(self):
        alice = ECC()
        plaintext = b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sig = b''.join((b'\x00', alice.sign(plaintext)))
        print(hexlify(sig))
        res = ECC(pubkey_x=alice.pubkey_x,
                  pubkey_y=alice.pubkey_y).verify(sig, plaintext)
        self.assertFalse(res)
