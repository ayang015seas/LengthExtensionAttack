#!/usr/bin/python3
# -*- coding: latin1 -*-
blob = """          ��3:KRUJ:��p�HB��B�7�$����p�<OF_�وK����==�U�i)�`�n��Ɠ/��gj�6��b1�F[&L I��L:��5�{�<��F�%����A�Ĝ�S�;�/_�뛝
"""
from hashlib import sha256
from pymd5 import md5, padding

s = sha256(blob.encode()).hexdigest()
h = md5(blob.encode())
# print(s)

a = int(s, 16)
if (a == 54171495150671847562167626440040326493091383282435000388274959178230348685946):
	print("I am good and friendly.")
else:
	print("I am an evil payload, prepare to suffer.")

# print(a)
# print(h.hexdigest())