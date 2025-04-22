def xor_decrypt(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

with open('C:\\Users\\marka\\Coding\\UVG\\Cifrados\\Cifrados-Proyecto-1\\challenges_volumes\\usopp_ctf\\poneglyph.jpeg', 'rb') as f:
    ciphertext = f.read()
    print(ciphertext)

# Con el print anterior, extraigo la llave incrustada en la imagen y a esa le aplico el xor
hidden_key = b'aTFUZFTU^\x14VPIC\x14^PDUF\x1e\x11DXQ\x12bDBUE\x11xQ@A\x1d\x10dFSWQ\\SSC\x10|UE\x1d\x10QZV\x11bQ]H^\x17C\x14AP]EFSX\x10S[_CQTQA\x11VBQWU\x10X]_\x11VB[_\x11DXQ\x12a_^QU]I@\\\x1c'
print(f"\nEl cifrado es: {hidden_key}")
key = "21004"


plaintext = xor_decrypt(hidden_key, key.encode())

decoded = plaintext.decode('utf-8', errors='ignore')

with open("solution.txt", "w+", encoding="utf-8") as f:
    f.write(decoded)

print(f"\nLa flag es: '{decoded}'")