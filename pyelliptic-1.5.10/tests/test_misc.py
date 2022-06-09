#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2014 Yann GUIBET <yannguibet@gmail.com>.
# All rights reserved.
#
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     1. Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#
#     2. Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import unittest

from pyelliptic import ECC
from pyelliptic import hash as _hash


class TestEquals(unittest.TestCase):

    def test_equals(self):
        a = '\xb5\x85/\xe80\xfa\x04\xdf\x07\x83\x17P\x9dw\x02\x89'

        b = '\xb5\x85/\xe80\xfa\x04\xdf\x07\x83\x17P\x9dw\x02\x89'
        self.assertTrue(_hash.equals(a, b))

        b = '\xb4\x85/\xe80\xfa\x04\xdf\x07\x83\x17P\x9dw\x02\x89'
        self.assertFalse(_hash.equals(a, b))

        b = '\xb5\x85/\xe80\xfa\x04\xdf\x07\x83\x17P\x9dw\x02\x90'
        self.assertFalse(_hash.equals(a, b))

        b = '\xb4\x85/\xe80\xfa\x04\xdf\x07\x83\x17P\x9dw\x02'
        self.assertFalse(_hash.equals(a, b))


class TestCompatibilities(unittest.TestCase):

    def test_old_keys(self):
        alice = ECC()
        curve, px, py, i = ECC._old_decode_pubkey(alice._old_get_pubkey())
        curve2, pv, i = ECC._old_decode_privkey(alice._old_get_privkey())
        self.assertEqual(curve, curve2)
        alice2 = ECC(curve=curve, pubkey_x=px, pubkey_y=py, raw_privkey=pv)
        self.assertEqual(alice2.get_pubkey(), alice.get_pubkey())
        self.assertEqual(alice2.get_privkey(), alice.get_privkey())
