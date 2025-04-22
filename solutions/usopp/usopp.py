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

import random
from collections import Counter

# Frecuencias del alfabeto español
spanish_freq = {
    'A': 0.1253, 'B': 0.0142, 'C': 0.0468, 'D': 0.0586, 'E': 0.1368,
    'F': 0.0069, 'G': 0.0101, 'H': 0.0070, 'I': 0.0625, 'J': 0.0044,
    'K': 0.0002, 'L': 0.0497, 'M': 0.0315, 'N': 0.0671, 'Ñ': 0.0031,
    'O': 0.0868, 'P': 0.0251, 'Q': 0.0088, 'R': 0.0687, 'S': 0.0798,
    'T': 0.0463, 'U': 0.0393, 'V': 0.0090, 'W': 0.0002, 'X': 0.0022,
    'Y': 0.0090, 'Z': 0.0052,
}

def xor_decrypt(data, keystream):
    return bytes([b ^ keystream[i] for i, b in enumerate(data)])

def generate_keystream(seed, length):
    random.seed(seed)
    return bytes([random.randint(0, 255) for _ in range(length)])

def score_text(text):
    text = text.upper()
    count = Counter(c for c in text if c in spanish_freq)
    total = sum(count.values())
    if total == 0:
        return 0
    frequencies = {char: count[char] / total for char in count}
    score = sum(abs(frequencies.get(char, 0) - spanish_freq[char]) for char in spanish_freq)
    return score

# Carga de flag en hex
flag_hex = "a77742694e4c51d71d30393088918b7b1c6e09339d1d45da104b26bb19a9c683ed4e07d16d"
flag_bytes = bytes.fromhex(flag_hex)

# Brute force: seeds de 1 a 999999
best = []

for seed in range(1, 9999):
    keystream = generate_keystream(seed, len(flag_bytes))
    decrypted = xor_decrypt(flag_bytes, keystream)

    try:
        decoded = decrypted.decode("utf-8")
        score = score_text(decoded)

        best.append((seed, score))

    except UnicodeDecodeError:
        continue


# Ordenar por puntuación
best.sort(key=lambda x: x[1], reverse=True)
print(best)
# Mostrar los mejores resultados
print("Mejores resultados:")
for seed, score in best[:10]:
    print(f"Seed: {seed}, Score: {score:.4f}")
    keystream = generate_keystream(seed, len(flag_bytes))
    decrypted = xor_decrypt(flag_bytes, keystream)
    decoded = decrypted.decode("utf-8", errors="ignore")
    print(f"Texto descifrado: {decoded}")