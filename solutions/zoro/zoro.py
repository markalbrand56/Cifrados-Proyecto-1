def xor_decrypt(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

with open('C:\\Users\\marka\\Coding\\UVG\\Cifrados\\Cifrados-Proyecto-1\\challenges_volumes\\zoro_ctf\\poneglyph.jpeg', 'rb') as f:
    ciphertext = f.read()
    print(ciphertext)

# Con el print anterior, extraigo la llave incrustada en la imagen y a esa le aplico el xor
hidden_key = b'FYU\x10y[_[\x10`@XRU\x14QYQYZWU\x10X]_\x11D_\x14FYU\x10f]PT\x10d]_UWXKAX\x10C[EXYZ\x12EXU\x14eYQ\\Q\x12eBUQ\x12E_\x10_WT@\x10\\[\\\x10VF]\\\x10C\\]FY^S\x12YY]GW]V\x1e'
print(f"\nEl cifrado es: {hidden_key}")
key = "21004"


plaintext = xor_decrypt(hidden_key, key.encode())

decoded = plaintext.decode('utf-8', errors='ignore')

with open("solution.txt", "w+", encoding="utf-8") as f:
    f.write(decoded)

print(f"\nLa flag es: '{decoded}'")

flag = "072d03661519c3535ace983613f97d543b0f82500691e1d6e0eafb10e7bdbb51521c6b2e67"
flag_bytes = bytes.fromhex(flag)

def rc4_crypt(data, key):
    S = list(range(256))
    j = 0
    out = []

    # KSA (Key Scheduling Algorithm)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # PRGA (Pseudo-Random Generation Algorithm)
    i = j = 0
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        out.append(byte ^ K)

    return bytes(out)

decoded_flag = rc4_crypt(flag_bytes, key.encode())

print(f"\nLa flag es: '{decoded_flag}'")