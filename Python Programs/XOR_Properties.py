'''
What is XOR (⊕)?
XOR stands for "Exclusive OR". It's a bitwise operation that compares each bit:

0 ⊕ 0 = 0 (same bits = 0)
0 ⊕ 1 = 1 (different bits = 1)
1 ⊕ 0 = 1 (different bits = 1)
1 ⊕ 1 = 0 (same bits = 0)
Key XOR Properties (shown in your comments):
Self-Inverse: A ⊕ A = 0

Anything XORed with itself equals zero
Identity: A ⊕ 0 = A

XORing with zero doesn't change the value
Commutative: A ⊕ B = B ⊕ A

Order doesn't matter
Most Important: (A ⊕ B) ⊕ B = A

If you XOR something and then XOR with the same thing again, you get back the original
The Cryptographic Puzzle Explained:
You were given these clues:

Step-by-Step Solution:
Step 1: Find KEY2
We know: KEY2 ⊕ KEY1 = result
We want: KEY2
Using the self-inverse property: (KEY2 ⊕ KEY1) ⊕ KEY1 = KEY2
So: KEY2 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e ⊕ a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
Step 2: Find KEY3
We know: KEY2 ⊕ KEY3 = result
We want: KEY3
Using the self-inverse property: (KEY2 ⊕ KEY3) ⊕ KEY2 = KEY3
So: KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1 ⊕ KEY2
Step 3: Find FLAG
We know: FLAG ⊕ KEY1 ⊕ KEY2 ⊕ KEY3 = result
We want: FLAG
Using the self-inverse property: (FLAG ⊕ KEY1 ⊕ KEY2 ⊕ KEY3) ⊕ KEY1 ⊕ KEY2 ⊕ KEY3 = FLAG
So: FLAG = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf ⊕ KEY1 ⊕ KEY2 ⊕ KEY3
Why This Works (The Math):
Think of XOR like a reversible lock:

If secret ⊕ key = locked_box
Then locked_box ⊕ key = secret (unlocks it!)
In your puzzle:

Someone took the FLAG and "locked" it by XORing it with all three keys
To "unlock" it, you XOR the locked result with all three keys again
The keys cancel themselves out, leaving just the original FLAG
Real-World Applications:
One-Time Pad: Unbreakable encryption using XOR
Stream Ciphers: Many use XOR operations
Error Detection: XOR used in checksums
Cryptographic Hash Functions: Often use XOR in their algorithms
The Final Answer:
Your FLAG decoded to: crypto{x0r_i5_ass0c1at1v3}

The flag itself is a hint about XOR being "associative" - meaning you can group the operations in any order: (A ⊕ B) ⊕ C = A ⊕ (B ⊕ C)

This is why we could solve for each key step by step, using the associative property to rearrange the XOR operations!


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Alternatives:

from pwn import xor
k1=bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
k2_3=bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
flag=bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
print(xor(k1,k2_3,flag))



def XOR(var1,var2):
    return bytes(a^b for a,b in zip(var1, var2))

KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
KEY2_3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
Flag = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

Result = XOR(XOR(KEY1,KEY2_3),Flag)
print(Result.decode('utf-8'))



from Crypto.Util.number import *
k1=bytes_to_long(bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'))
k2_3=bytes_to_long(bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'))
flag_k1_2_3=bytes_to_long(bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'))

print(long_to_bytes(k1^k2_3^flag_k1_2_3))



# The hint indicates converting to bytes but it is not necessay, this soultion uses raw hex values

key1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
key2_key1 = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
key2_key3 = 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
flag_key1_key3_key2 = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

# Determine key2 used to encode key2_key1 by XOR with the specified key1
key2 = key1 ^ key2_key1

# determine key3 used to encode key2_key3 by XOR with calculated key2 from previous step
key3 =  key2_key3 ^ key2

# Determine flag used to encode flag_key1_key3_key2 by XOR with key1, key2 and key3 
flag = flag_key1_key3_key2 ^ key1 ^ key3 ^ key2

# Output the flag converted to utf-8 - note the [2:] strips off the 0x at the beginning
# of the converted hex value to string value needed by bytes.fromhex()
print(bytes.fromhex(hex(flag)[2:]).decode('utf-8'))
'''
from Crypto.Util.number import *

# Given values
KEY1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_XOR_KEY1_hex = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"  # KEY2 ^ KEY1
KEY2_XOR_KEY3_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"  # KEY2 ^ KEY3
FLAG_XOR_ALL_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"  # FLAG ^ KEY1 ^ KEY3 ^ KEY2

# Convert to integers
KEY1 = int(KEY1_hex, 16)
KEY2_XOR_KEY1 = int(KEY2_XOR_KEY1_hex, 16)
KEY2_XOR_KEY3 = int(KEY2_XOR_KEY3_hex, 16)
FLAG_XOR_ALL = int(FLAG_XOR_ALL_hex, 16)

print("=== Step 1: Calculate KEY2 ===")
# To get KEY2: Since we have KEY2 ^ KEY1, and we know KEY1
# KEY2 = (KEY2 ^ KEY1) ^ KEY1
KEY2 = KEY2_XOR_KEY1 ^ KEY1
print(f"KEY2 = {hex(KEY2)}")

print("\n=== Step 2: Calculate KEY3 ===")
# To get KEY3: Since we have KEY2 ^ KEY3, and we now know KEY2
# KEY3 = (KEY2 ^ KEY3) ^ KEY2
KEY3 = KEY2_XOR_KEY3 ^ KEY2
print(f"KEY3 = {hex(KEY3)}")

print("\n=== Step 3: Calculate FLAG ===")
# We have FLAG ^ KEY1 ^ KEY3 ^ KEY2, and we know all the keys
# FLAG = (FLAG ^ KEY1 ^ KEY3 ^ KEY2) ^ KEY1 ^ KEY3 ^ KEY2
FLAG = FLAG_XOR_ALL ^ KEY1 ^ KEY3 ^ KEY2
print(f"FLAG (as int) = {FLAG}")
print(f"FLAG (as hex) = {hex(FLAG)}")

print("\n=== Step 4: Convert FLAG to readable text ===")
try:
    flag_text = long_to_bytes(FLAG).decode()
    print(f"FLAG (as text) = {flag_text}")
except UnicodeDecodeError:
    flag_bytes = long_to_bytes(FLAG)
    print(f"FLAG (as bytes) = {flag_bytes}")
    print(f"FLAG (as hex string) = {flag_bytes.hex()}")

print("\n=== Verification ===")
print(f"KEY2 ^ KEY1 = {hex(KEY2 ^ KEY1)} (should match {KEY2_XOR_KEY1_hex})")
print(f"KEY2 ^ KEY3 = {hex(KEY2 ^ KEY3)} (should match {KEY2_XOR_KEY3_hex})")
print(f"FLAG ^ KEY1 ^ KEY2 ^ KEY3 = {hex(FLAG ^ KEY1 ^ KEY2 ^ KEY3)} (should match {FLAG_XOR_ALL_hex})")




lesson_5 = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
flag = 'crypto{'

key = [lesson_5[a] ^ ord(b) for a, b in enumerate(flag)]
print('Decoded key:', ''.join(chr(a) for a in key))

key.append(ord('y'))
print('Full key:', ''.join(chr(a) for a in key))

flag = ''.join(chr(lesson_5[a] ^ key[a % len(key)]) for a in range(len(lesson_5)))
print('Full flag:', flag)