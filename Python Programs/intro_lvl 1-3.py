#!/usr/bin/env python3

import sys
import base64
from Crypto.Util.number import *
from Crypto.Util.strxor import strxor


if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

print("Here is your flag:")
print("".join(chr(o) for o in ords))
#print("".join(chr(o ^ 0x32) for o in ords))

hex = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
hexBase64 = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
print(bytes.fromhex(hex).decode())
hexBytes = bytes.fromhex(hexBase64)
print(base64.b64encode(hexBytes))

intConversion = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(long_to_bytes(intConversion).decode())

label = "label"
random = 13

# Method 1: Using manual XOR
xorred_manual = "".join(chr(ord(char) ^ 13) for char in label)
print(f"Manual XOR - Original: {label}")
print(f"Manual XOR - Result: {xorred_manual}")

# Method 2: Using PyCryptodome's strxor() function
label_bytes = label.encode('utf-8')  # Convert string to bytes
key_bytes = bytes([random] * len(label_bytes))  # Create key of same length
xorred_crypto = strxor(label_bytes, key_bytes).decode('utf-8')
print(f"PyCryptodome strxor() - Original: {label}")
print(f"PyCryptodome strxor() - Result: {xorred_crypto}")

# Method 3: More concise with PyCryptodome
xorred_concise = strxor(label.encode(), bytes([random] * len(label))).decode()
print(f"Concise PyCryptodome - Result: {xorred_concise}")

