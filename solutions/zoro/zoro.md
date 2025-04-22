# Solución

Para este segundo reto, se siguió un procedimiento similar al primero.

```bash
docker exec -it {challengeX_ctf} bash
```

Usando la flag encontrada en el reto anterior, se inicia sesión como `zoro`:

```bash
su zoro
password: FLAG_348a56efa179e2911c421c9c6ad83869
```

Se vuelve a usar el comando `find` para buscar archivos que contengan la palabra `poneglyph` en su nombre:

```bash
find . -name "poneglyph*"
```

Esto da como resultado:

```bash
zoro@89bf91b1a510:~/ONEPIECE$ find . -name "poneglyph*"
./East_Blue/Shells_Town/Casa_de_Rika/poneglyph.zip
```

Usando 7z para extraer el archivo:
```bash
7z x ./East_Blue/Shells_Town/Casa_de_Rika/poneglyph.zip -oponeglyph_descomprimido
```

Ingresando la contraseña `FLAG_348a56efa179e2911c421c9c6ad83869` resulta en el siguiente archivo:

```bash
zoro@89bf91b1a510:~/ONEPIECE$ ls
Dressrosa  East_Blue  Fishman_Island  Wano  Zou  poneglyph_descomprimido
zoro@89bf91b1a510:~/ONEPIECE$ cd poneglyph_descomprimido/
zoro@89bf91b1a510:~/ONEPIECE/poneglyph_descomprimido$ ls
poneglyph.jpeg
```

![Screenshot](https://github.com/markalbrand56/Cifrados-Proyecto-1/blob/main/media/zoro_1.png)

Ahora se mueve esta imagen al volumen compartido `/zoro_ctf` para trabajar con ella en la máquina local.

```bash
mv poneglyph.jpeg /zoro_ctf
```

![poneglyph.jpeg](https://github.com/markalbrand56/Cifrados-Proyecto-1/blob/main/challenges_volumes/zoro_ctf/poneglyph.jpeg)

Con la imagen en mi máquina local, se puede abrir sin problemas la imagen. Se puede notar nuevamente que en la esquina superior
izquierda hay un texto que parece ser una llave, empezando con los caracteres 'FYU' y siguiendo con caracteres que parecen 
no ser ASCII. Esto es un indicio de que este es lo que hay que descifrar usando XOR. 

Al leer el contenido con python, se puede encontrar el segmento de bytes que representan este texto.

```text
FYU\x10y[_[\x10`@XRU\x14QYQYZWU\x10X]_\x11D_\x14FYU\x10f]PT\x10d]_UWXKAX\x10C[EXYZ\x12EXU\x14eYQ\\Q\x12eBUQ\x12E_\x10_WT@\x10\\[\\\x10VF]\\\x10C\\]FY^S\x12YY]GW]V\x1e
```

Usando esto como texto cifrado, y mi carnet `21004` como la llave, se obtiene la flag siguiente:

```text
the Mink Tribe chained him to the Road Poneglyph within the Whale Tree to keep him from showing himself.
```

Por último, usando el siguiente comando se pueden encontrar diversos archivos de texto

```bash
zoro@89bf91b1a510:~/ONEPIECE$ find . -type f \( -iname "*.txt" -o -iname "*.enc" -o -iname "*.flag" \)
```

```text
./Dressrosa/Acacia/Casa_de_Riku_Dold_III/flag.txt
./Dressrosa/Acacia/Casa_de_Rebecca/flag.txt
./Dressrosa/Toy_House/Casa_de_Trebol/flag.txt
./East_Blue/Syrup_Village/Casa_de_Usopp/flag.txt
./East_Blue/Arlong_Park/Casa_de_Nami/flag.txt
./East_Blue/Baratie/Casa_de_Patty/flag.txt
./Zou/Left_Hind_Leg/Casa_de_Nekomamushi/flag.txt
./Zou/Left_Fore_Leg/Casa_de_Inuarashi/flag.txt
./Wano/Flower_Capital/Casa_de_Oden/flag.txt
./Wano/Udon/Casa_de_Kozuki_Momonosuke/flag.txt
./Fishman_Island/Gyoverly_Hills/Casa_de_Shirahoshi/flag.txt
```

De estos, el sexto archivo `./East_Blue/Baratie/Casa_de_Patty/flag.txt` contiene el único texto que no es legible.

Aplicando el mismo método de XOR, la llave no se logra descifrar. Como el nombre del reto lo dice, esta esta codificada
usando RC4. Usando el scipt desarrollado de Python para romper RC4, se logra obtener la siguiente flag:

```text
FLAG_7bf472c0a9f8c3bda0057209c9ad1aed
```

![Screenshot](https://github.com/markalbrand56/Cifrados-Proyecto-1/blob/main/media/luffy_2.png)
