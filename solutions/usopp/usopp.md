# Solución

Para este tercer reto, se siguió la misma metodología que en los dos anteriores.

```bash
docker exec -it {challengeX_ctf} bash
```

Usando la flag encontrada en el reto anterior, se inicia sesión como `usopp`:

```bash
su usopp
password: FLAG_7bf472c0a9f8c3bda0057209c9ad1aed
```

Se vuelve a usar el comando `find` para buscar archivos que contengan la palabra `poneglyph` en su nombre:

```bash
find . -name "poneglyph*"
```

Esto da como resultado:

```bash
usopp@2a73d406848a:~$ find . -name "poneglyph*"
./ONEPIECE/Zou/Right_Belly_Fortress/Casa_de_Inuarashi/poneglyph.zip
```

Usando 7z para extraer el archivo:
```bash
7z x ./ONEPIECE/Zou/Right_Belly_Fortress/Casa_de_Inuarashi/poneglyph.zip -oponeglyph_descomprimido
```

Ingresando la contraseña `FLAG_7bf472c0a9f8c3bda0057209c9ad1aed` resulta en el siguiente archivo:

```bash
usopp@2a73d406848a:~$ ls
ONEPIECE  poneglyph_descomprimido
usopp@2a73d406848a:~$ cd poneglyph_descomprimido/
usopp@2a73d406848a:~/poneglyph_descomprimido$ ls
poneglyph.jpeg
```

![Screenshot](https://github.com/markalbrand56/Cifrados-Proyecto-1/blob/main/media/usopp_1.png)

Ahora se mueve esta imagen al volumen compartido `/usopp_ctf` para trabajar con ella en la máquina local.

```bash
cp poneglyph.jpeg /usopp_ctf
```

![poneglyph.jpeg](https://github.com/markalbrand56/Cifrados-Proyecto-1/blob/main/challenges_volumes/usopp_ctf/poneglyph.jpeg)

Con la imagen en mi máquina local, se puede abrir sin problemas la imagen. Se puede notar nuevamente que en la esquina superior
izquierda hay un texto que parece ser una llave, empezando con los caracteres 'aTUFZ' y siguiendo con caracteres que parecen 
no ser ASCII. Esto es un indicio de que este es lo que hay que descifrar usando XOR. 

Al leer el contenido con python, se puede encontrar el segmento de bytes que representan este texto.

```text
aTFUZFTU^\x14VPIC\x14^PDUF\x1e\x11DXQ\x12bDBUE\x11xQ@A\x1d\x10dFSWQ\\SSC\x10|UE\x1d\x10QZV\x11bQ]H^\x17C\x14AP]EFSX\x10S[_CQTQA\x11VBQWU\x10X]_\x11VB[_\x11DXQ\x12a_^QU]I@\\\x1c
```

Usando esto como texto cifrado, y mi carnet `21004` como la llave, se obtiene la flag siguiente:

```text
Seventeen days later, the Straw Hats, Trafalgar Law, and Raizo's samurai comrades freed him from the Poneglyph.
```

Por último, usando el siguiente comando se pueden encontrar diversos archivos de texto

```bash
usopp@2a73d406848a:~/poneglyph_descomprimido$ find . -type f \( -iname "*.txt" -o -iname "*.enc" -o -iname "*.flag" \)
```

```text
./ONEPIECE/Dressrosa/Corrida_Colosseum/Casa_de_Viola/flag.txt
./ONEPIECE/Dressrosa/Acacia/Casa_de_Rebecca/flag.txt
./ONEPIECE/Dressrosa/Toy_House/Casa_de_Trebol/flag.txt
./ONEPIECE/East_Blue/Syrup_Village/Casa_de_Merry/flag.txt
./ONEPIECE/East_Blue/Orange_Town/Casa_de_Nami/flag.txt
./ONEPIECE/East_Blue/Shells_Town/Casa_de_Helmeppo/flag.txt
./ONEPIECE/East_Blue/Loguetown/Casa_de_Dragon/flag.txt
./ONEPIECE/Zou/Right_Hind_Leg/Casa_de_Nekomamushi/flag.txt
./ONEPIECE/Zou/Right_Belly_Fortress/Casa_de_Nekomamushi/flag.txt
./ONEPIECE/Zou/Right_Fore_Leg/Casa_de_Kawamatsu/flag.txt
./ONEPIECE/Fishman_Island/Gyoncorde_Plaza/Casa_de_Otohime/flag.txt
```

De estos, el archivo `./ONEPIECE/Zou/Right_Fore_Leg/Casa_de_Kawamatsu/flag.txt` contiene el único texto que no es legible.

Como lo dice el enunciado, ahora la flag esta codificada con un algoritmo de Stream Cipher. Para romper el cifrado,
se decidió utilizar un script de python que utiliza fuerza bruta para encontrar la llave. Con este script, se puede ver
que la mayoría de las llaves no funcionan, resultando en una única seed que funciona, la `1234` dando como resultado la siguiente flag:

```text
FLAG_fcbd8689ff72334dbd43f119306e1a9d
```

![Screenshot](https://github.com/markalbrand56/Cifrados-Proyecto-1/blob/main/media/usopp_2.png)
