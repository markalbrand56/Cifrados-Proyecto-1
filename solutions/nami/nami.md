# Solución

Para este el último reto, se siguió la misma metodología que en los dos anteriores.

```bash
docker exec -it {challengeX_ctf} bash
```

Usando la flag encontrada en el reto anterior, se inicia sesión como `usopp`:

```bash
su nami
password: FLAG_fcbd8689ff72334dbd43f119306e1a9d
```

Se vuelve a usar el comando `find` para buscar archivos que contengan la palabra `poneglyph` en su nombre:

```bash
find . -name "poneglyph*"
```

Esto da como resultado:

```bash
nami@d7e64ac7c05a:~$ find . -name "poneglyph*"
./ONEPIECE/Dressrosa/Royal_Palace/Casa_de_Riku_Dold_III/poneglyph.zip
```

Usando 7z para extraer el archivo:
```bash
 7z x ./ONEPIECE/Dressrosa/Royal_Palace/Casa_de_Riku_Dold_III/poneglyph.zip -oponeglyph_descomprimido
```

Ingresando la contraseña `FLAG_fcbd8689ff72334dbd43f119306e1a9d` resulta en el siguiente archivo:

```bash
nami@d7e64ac7c05a:~$ cd poneglyph_descomprimido/
nami@d7e64ac7c05a:~/poneglyph_descomprimido$ ls -a
.  ..  poneglyph.jpeg
```

![Screenshot](https://github.com/markalbrand56/Cifrados-Proyecto-1/blob/main/media/nami_1.png)

Ahora se mueve esta imagen al volumen compartido `/nami_ctf` para trabajar con ella en la máquina local.

```bash
cp poneglyph.jpeg /nami_ctf
```

![poneglyph.jpeg](https://github.com/markalbrand56/Cifrados-Proyecto-1/blob/main/challenges_volumes/nami_ctf/poneglyph.jpeg)

Con la imagen en mi máquina local, se puede abrir sin problemas la imagen. Se puede notar nuevamente que en la esquina superior
izquierda hay un texto que parece ser una llave, pero en este caso el texto es prácticamente ilegible a simple vista.
Entonces, imprimiendo los bytes de la imagen, en las primeras líneas se pueden ver caracteres fuera de lugar, con el mismo
patrón que en los ejercicios anteriores. Gracias a esto fue posible encontrar el texto que parece ser la llave.

Al leer el contenido con python, se puede encontrar el segmento de bytes que representan este texto.

```text
sWDUF\x12c_R]\\\x11TUW[AXUFWU\x10D\\W\x11b_UV\x11`_ZWV\\IDZ\x1d\x10yZGPBQGZX\x10ULB]QYZWU\x10Y@A\x11@EFB^CU\x14]W\x10BQDTQ\\]\\V\x10D\\W\x11\\_WSEY_Z\x12^V\x10xSDWX\x14fP\\U\x14EYU^\x14[EC\x10]\\W_BYSEY_Z\x12FQC\x14Q^]R]\\TT\x10C[EX\x10@ZPD\x10[T\x11DXQ\x12^DXQ@\x11DXFWT\x10b[SU\x10`[\\TW\\MBYC\x1e
```

Usando esto como texto cifrado, y mi carnet `21004` como la llave, se obtiene la flag siguiente:

```text
After Robin deciphered the Road Poneglyph, Inuarashi explained its purpose of revealing the location of Laugh Tale when its information was combined with that of the other three Road Poneglyphs.
```

Por último, usando el siguiente comando se pueden encontrar diversos archivos de texto

```bash
nami@d7e64ac7c05a:~$ find . -type f \( -iname "*.txt" -o -iname "*.enc" -o -iname "*.flag" \)
```

```text
./ONEPIECE/Dressrosa/Acacia/Casa_de_Riku_Dold_III/flag.txt
./ONEPIECE/Dressrosa/Flower_Hill/Casa_de_Riku_Dold_III/flag.txt
./ONEPIECE/East_Blue/Orange_Town/Casa_de_Boodle/flag.txt
./ONEPIECE/East_Blue/Shells_Town/Casa_de_Rika/flag.txt
./ONEPIECE/Zou/Left_Hind_Leg/Casa_de_Nekomamushi/flag.txt
./ONEPIECE/Zou/Right_Fore_Leg/Casa_de_Nekomamushi/flag.txt
./ONEPIECE/Zou/Right_Fore_Leg/Casa_de_Kawamatsu/flag.txt
./ONEPIECE/Wano/Flower_Capital/Casa_de_Oden/flag.txt
./ONEPIECE/Wano/Onigashima/Casa_de_Kaido/flag.txt
./ONEPIECE/Fishman_Island/Mermaid_Cove/Casa_de_Otohime/flag.txt
```

De estos, el archivo `./ONEPIECE/Zou/Right_Fore_Leg/Casa_de_Kawamatsu/flag.txt` contiene el único texto que no es legible.

Como lo dice el enunciado, ahora la flag esta codificada con un algoritmo de ChaCha20. 

Este algoritmo depende de una llave y un nonce. Es un cifrado difícil de romper con fuerza bruta, así que se probaron primero algunos
diferentes valores, usando mi carnet como punto de partida.

Al final, se encontró que efectivamente mi carnet era tanto el nonce como la llave, en configuración de 256 bits para la llave y de 64 bits para el nonce.
Con esto, se encontró la última flag:

```text
FLAG_914bacd0923f836359edcf71b726b935
```

![Screenshot](https://github.com/markalbrand56/Cifrados-Proyecto-1/blob/main/media/nami_2.png)
