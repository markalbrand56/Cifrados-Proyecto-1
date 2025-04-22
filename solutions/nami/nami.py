def xor_decrypt(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

with open('C:\\Users\\marka\\Coding\\UVG\\Cifrados\\Cifrados-Proyecto-1\\challenges_volumes\\nami_ctf\\poneglyph.jpeg', 'rb') as f:
    ciphertext = f.read()
    print(ciphertext)

# Con el print anterior, extraigo la llave incrustada en la imagen y a esa le aplico el xor
hidden_key = b'sWDUF\x12c_R]\\\x11TUW[AXUFWU\x10D\\W\x11b_UV\x11`_ZWV\\IDZ\x1d\x10yZGPBQGZX\x10ULB]QYZWU\x10Y@A\x11@EFB^CU\x14]W\x10BQDTQ\\]\\V\x10D\\W\x11\\_WSEY_Z\x12^V\x10xSDWX\x14fP\\U\x14EYU^\x14[EC\x10]\\W_BYSEY_Z\x12FQC\x14Q^]R]\\TT\x10C[EX\x10@ZPD\x10[T\x11DXQ\x12^DXQ@\x11DXFWT\x10b[SU\x10`[\\TW\\MBYC\x1e'
print(f"\nEl cifrado es: {hidden_key}")
key = "21004"


plaintext = xor_decrypt(hidden_key, key.encode())

decoded = plaintext.decode('utf-8', errors='ignore')

with open("solution.txt", "w+", encoding="utf-8") as f:
    f.write(decoded)

print(f"\nLa flag es: '{decoded}'")

flag = "406741b0ff88d323d03e2948042e9909a79467ba21c95fe34cbb0529a3d9b6537a9312f3b1"
flag_bytes = bytes.fromhex(flag)
