# Solución

```bash
docker exec -it {challengeX_ctf} bash
```

```bash
su luffy
password: onepiece
```


```bash
find . -name "poneglyph*"
```

Esto da como resultado:

```bash
luffy@2affc5ba053a:~$ find . -name "poneglyph*"
./ONEPIECE/East_Blue/Shells_Town/Casa_de_Helmeppo/poneglyph.zip
```

Usando 7z para extraer el archivo:
```bash
7z x ./East_Blue/Shells_Town/Casa_de_Helmeppo/poneglyph.zip -oponeglyph_descomprimido
```

Ingresando la contraseña `onepiece` resulta en el siguiente archivo:

```bash
luffy@2affc5ba053a:~/ONEPIECE/poneglyph_descomprimido$ ls -a
.  ..  poneglyph.jpeg
```

![Screenshot](https://github.com/markalbrand56/Cifrados-Proyecto-1/blob/main/media/luffy_1.png)

Ahora se mueve esta imagen al volumen compartido `/luffy_ctf` para trabajar con ella en la máquina local.

```bash
mv poneglyph.jpeg /luffy_ctf
```

![poneglyph.jpeg](https://github.com/markalbrand56/Cifrados-Proyecto-1/blob/main/challenges_volumes/luffy_ctf/poneglyph.jpeg)

Con la imagen en mi máquina local, se puede abrir sin problemas la imagen. Se puede notar que en la esquina superior
izquierda hay un texto que parece ser una llave, empezando con los caracteres 'eYU' y siguiendo con caracteres que parecen 
no ser ASCII. Esto es un indicio de que este es lo que hay que descifrar usando XOR. 

Al leer el contenido con python, se puede encontrar el segmento de bytes que representan este texto.

```text
eYU^\x14xPS[\x14S_T\x10@ZT\x10rQSBDC\x14bXBQ@WB\x10YZDPTUP\x12k_E\x14F^\x10\\[]Z\x10V[@\x11bQ]H^\x10_R\x12fQ^[\x12r_EZFCI\x1c
```

Usando esto como texto cifrado, y mi carnet `21004` como la llave, se obtiene la flag siguiente:

```text
When Jack and the Beasts Pirates invaded Zou to look for Raizo of Wano Country,
```

> Si se usa la imagen completa, el resultado no contiene ningún texto legible. Por lo tanto se asume
> que el texto cifrado es solo la parte que contiene el texto.

Por último, usando el siguiente comando se pueden encontrar diversos archivos de texto

```bash
luffy@2affc5ba053a:~/ONEPIECE$ find . -type f \( -iname "*.txt" -o -iname "*.enc" -o -iname "*.flag" \)
```

```text
./Dressrosa/Acacia/Casa_de_Rebecca/flag.txt
./Dressrosa/Royal_Palace/Casa_de_Viola/flag.txt
./East_Blue/Syrup_Village/Casa_de_Usopp/flag.txt
./East_Blue/Romance_Dawn/Casa_de_Shanks/flag.txt
./East_Blue/Shells_Town/Casa_de_Morgan/flag.txt
./East_Blue/Loguetown/Casa_de_Dragon/flag.txt
./Zou/Right_Belly_Fortress/Casa_de_Nekomamushi/flag.txt
./Zou/Right_Fore_Leg/Casa_de_Inuarashi/flag.txt
./Wano/Udon/Casa_de_Oden/flag.txt
./Fishman_Island/Coral_Mansion/Casa_de_Otohime/flag.txt
./Fishman_Island/Gyoverly_Hills/Casa_de_Otohime/flag.txt
```

De estos, el segundo archivo `./Dressrosa/Royal_Palace/Casa_de_Viola/flag.txt` contiene el único texto que no es legible.

Aplicando el mismo método de XOR, se obtiene la siguiente flag:

```text
FLAG_348a56efa179e2911c421c9c6ad83869
```