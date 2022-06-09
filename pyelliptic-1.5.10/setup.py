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
from setuptools import setup

from setuptools.command.test import test


class TestCommand(test, object):

    user_options = [('openssl-1-1', None, "Use OpenSSL 1.1 binaries")]

    def initialize_options(self):
        super(TestCommand, self).initialize_options()
        self.test_module = 'tests'
        self.test_suite = ''
        self.openssl_1_1 = False

    def run(self):
        if self.openssl_1_1:
            from ctypes import util
            util.find_library = self._fixed_library_path

        import pyelliptic
        from pyelliptic import OpenSSL

        print('> ---------------------------------------------- ')
        print('> version:', pyelliptic.__version__)
        print('> library:', pyelliptic.openssl.libname)
        print('> openssl:', '1.1' if OpenSSL.using_openssl_1_1 else 'pre-1.1')
        print('> ---------------------------------------------- ')

        super(TestCommand, self).run()

    @staticmethod
    def _fixed_library_path(*_args, **_kwargs):
        import sys
        from os.path import abspath, dirname, join

        if sys.platform == 'win32':
            lib_name = 'libcrypto-1_1-x64.dll'
        elif sys.platform == 'darwin':
            lib_name = 'libcrypto.1.1.dylib'
        else:
            lib_name = 'libcrypto.so.1.1'

        lib_dir = join(abspath(dirname(__file__)), 'tests', 'lib')
        return join(lib_dir, lib_name)


setup(
    name="pyelliptic",
    version='1.5.10',
    url='https://github.com/mfranciszkiewicz/pyelliptic',
    license='BSD',
    description=
    "Python OpenSSL wrapper for modern cryptography with " +
    "ECC, AES, HMAC, Blowfish, ...",
    author='Yann GUIBET, Marek Franciszkiewicz',
    author_email='yannguibet@gmail.com, marek@golem.network',
    packages=['pyelliptic'],
    cmdclass={
        'test': TestCommand
    },
    classifiers=[
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Environment :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Security :: Cryptography',
    ],
)
