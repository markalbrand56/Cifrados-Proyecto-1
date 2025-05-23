def xor_decrypt(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

with open('C:\\Users\\marka\\Coding\\UVG\\Cifrados\\Cifrados-Proyecto-1\\challenges_volumes\\luffy_ctf\\poneglyph.jpeg', 'rb') as f:
    ciphertext = f.read()
    print(ciphertext)

# Con el print anterior, extraigo la llave incrustada en la imagen y a esa le aplico el xor
hidden_key = b'eYU^\x14xPS[\x14S_T\x10@ZT\x10rQSBDC\x14bXBQ@WB\x10YZDPTUP\x12k_E\x14F^\x10\\[]Z\x10V[@\x11bQ]H^\x10_R\x12fQ^[\x12r_EZFCI\x1c'
print(f"\nEl cifrado es: {hidden_key}")
key = "21004"


plaintext = xor_decrypt(hidden_key, key.encode())

decoded = plaintext.decode('utf-8', errors='ignore')

with open("solution.txt", "w+", encoding="utf-8") as f:
    f.write(decoded)

print(f"\nLa flag es: '{decoded}'")

# aplicarle xor con 21004 a '747d71776b01050851010454565105050855020d03005304060352095302535508030c0408'
flag = "747d71776b01050851010454565105050855020d03005304060352095302535508030c0408"
flag_bytes = bytes.fromhex(flag)
flag_decrypted = xor_decrypt(flag_bytes, key.encode())

decoded_flag = flag_decrypted.decode('utf-8', errors='ignore')

print(f"\nLa flag es: '{decoded_flag}'")