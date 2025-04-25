# Cifrado de información

## Proyecto 1: Cifrados de Flujo – Desafíos en Seguridad

<a id="readme-top"></a>

<!--
PROJECT DESCRIPTION
-->
## 📜 Descripción

Este proyecto tiene como finalidad que los alumnos comprendan y apliquen conceptos de cifrados de flujo mediante la resolución 
de retos prácticos basados en algoritmos criptográficos como RC4, XOR y ChaCha20. A través de estos ejercicios, explorarán la 
importancia de claves, nonces y seguridad en la implementación de cifrados modernos.

## Resolución

En este archivo se encuentra el **resumen** de la resolución a los cuatro desafíos de este laboratorio. Para más detalles
y el código utilizado en cada uno de los retos, se puede consultar la carpeta `solutions` en el repositorio. En ella
cada desafío tiene su propia carpeta con el código y la documentación correspondiente.

### Luffy

Para este primer desafío, se utilizó el siguiente comando para acceder al contenedor de Docker:
```bash
docker exec -it {challengeX_ctf} bash
```

Usando la contraseña inicial se inicia sesión como `luffy`:
```bash
su luffy
password: onepiece
```

#### Poneglyph

![Poneglyph Luffy]((https://github.com/markalbrand56/Cifrados-Proyecto-1/blob/main/challenges_volumes/luffy_ctf/poneglyph.jpeg))

Una vez con el acceso, se encuentra el archivo `poneglyph.zip` en la ruta `./ONEPIECE/East_Blue/Shells_Town/Casa_de_Helmeppo/`,
después de extraerla se obtiene el archivo `poneglyph.jpeg`. Este luego se copia al volumen compartido `luffy_ctf` para ser
analizado en la máquina local.

Al abrir la imagen se puede observar que en la esquina superior izquierda hay un texto que parece ser una llave, empezando con los caracteres 'eYU' y
siguiendo con caracteres que parecen no ser ASCII. Esto es un indicio de que este es lo que hay que descifrar usando XOR.

Con el código de `luffy.py` se abrió la imagen y se inspeccionaron el contenido en forma de bytes. En la salida se encontró el 
segmento de bytes que representan el texto cifrado.

```text
eYU^\x14xPS[\x14S_T\x10@ZT\x10rQSBDC\x14bXBQ@WB\x10YZDPTUP\x12k_E\x14F^\x10\\[]Z\x10V[@\x11bQ]H^\x10_R\x12fQ^[\x12r_EZFCI\x1c
```

A esta cadena de bytes se le aplicó el cifrado XOR con la llave `21004` (mi carnet) y se obtuvo el texto

```text
When Jack and the Beasts Pirates invaded Zou to look for Raizo of Wano Country,
```

#### Flag

Luego de procesar la imagen, se buscó la flag. Se encontraron 12 archivos llamados `flag.txt` en el contenedor.
Explorando dichos archivos se encontró un contenido fuera de lo común: una cadena de caracteres que no representaban una
oración coherente. De esta manera se identificó que el archivo `./Dressrosa/Royal_Palace/Casa_de_Viola/flag.txt` contenía la flag.

Aplicándole el algoritmo XOR con la llave `21004`, se obtuvo el siguiente resultado:

```text
FLAG_348a56efa179e2911c421c9c6ad83869
```

### Zoro

Para el segundo desafío, se siguió un procedimiento similar al primero.

```bash
docker exec -it {challengeX_ctf} bash
```

Usando la flag encontrada en el reto anterior, se inicia sesión como `zoro`:

```bash
su zoro
password: FLAG_348a56efa179e2911c421c9c6ad83869
```

#### Poneglyph

![Poneglyph Zoro]((https://github.com/markalbrand56/Cifrados-Proyecto-1/blob/main/challenges_volumes/zoro_ctf/poneglyph.jpeg))

Nuevamente, se buscó el archivo `poneglyph.zip`, encontrándolo en la carpeta `./East_Blue/Shells_Town/Casa_de_Rika/`. 
Siguiendo el mismo procedimiento que en el primer desafío, se extrajo el archivo y se obtuvo la imagen `poneglyph.jpeg`.
Esta imagen se movió al volumen compartido `/zoro_ctf` para trabajar con ella en la máquina local.

Al abrir la imagen, se observó nuevamente un texto en la esquina superior izquierda que parecía ser una llave, 
comenzando con los caracteres 'FYU' y seguido de caracteres no ASCII. Esto sugiere que este es el texto a 
descifrar, esta vez usando el algoritmo RC4 como lo indica el título del reto.

Usando el código de `zoro.py`, se abrió la imagen y se inspeccionó el contenido en forma de bytes. Los bytes encontrados fueron:

```text
FYU\x10y[_[\x10`@XRU\x14QYQYZWU\x10X]_\x11D_\x14FYU\x10f]PT\x10d]_UWXKAX\x10C[EXYZ\x12EXU\x14eYQ\\Q\x12eBUQ\x12E_\x10_WT@\x10\\[\\\x10VF]\\\x10C\\]FY^S\x12YY]GW]V\x1e
```

A esta cadena de bytes se le aplicó el cifrado RC4 con la llave `21004` (mi carnet) y se obtuvo el texto

```text
the Mink Tribe chained him to the Road Poneglyph within the Whale Tree to keep him from showing himself.
```

#### Flag

Luego de procesar la imagen, se buscó la flag. Se encontraron 11 archivos llamados `flag.txt` en el contenedor.
Explorando dichos archivos se encontró un contenido fuera de lo común: una cadena de caracteres que no representaban una
oración coherente. De esta manera se identificó que el archivo `./East_Blue/Baratie/Casa_de_Patty/flag.txt`.

Ahora, en vez de utilizar el algoritmo XOR, se aplicó el algoritmo RC4 con la llave `21004` y se obtuvo el siguiente resultado:

```text
FLAG_7bf472c0a9f8c3bda0057209c9ad1aed
```

### Usopp

Para el tercer desafío, se siguió un procedimiento similar a los anteriores.

```bash
docker exec -it {challengeX_ctf} bash
```

Usando la flag encontrada en el reto anterior, se inicia sesión como `usopp`:

```bash
su usopp
password: FLAG_7bf472c0a9f8c3bda0057209c9ad1aed
```

#### Poneglyph

![Poneglyph Usopp]((https://github.com/markalbrand56/Cifrados-Proyecto-1/blob/main/challenges_volumes/usopp_ctf/poneglyph.jpeg))

Nuevamente, se buscó el archivo `poneglyph.zip`, encontrándolo en la carpeta `./ONEPIECE/Zou/Right_Belly_Fortress/Casa_de_Inuarashi`.
Siguiendo el mismo procedimiento que en el primer desafío, se extrajo el archivo y se obtuvo la imagen `poneglyph.jpeg`.
Esta imagen se movió al volumen compartido `/usopp_ctf` para trabajar con ella en la máquina local.

Al abrir la imagen, se observó nuevamente un texto en la esquina superior izquierda que parecía ser una llave,
comenzando con los caracteres 'aTUFZ' y seguido de caracteres no ASCII. Esto sugiere que este es el texto a
descifrar, esta vez usando el algoritmo XOR como lo indica el título del reto.

Usando el código de `usopp.py`, se abrió la imagen y se inspeccionó el contenido en forma de bytes. Los bytes encontrados fueron:

```text
aTFUZFTU^\x14VPIC\x14^PDUF\x1e\x11DXQ\x12bDBUE\x11xQ@A\x1d\x10dFSWQ\\SSC\x10|UE\x1d\x10QZV\x11bQ]H^\x17C\x14AP]EFSX\x10S[_CQTQA\x11VBQWU\x10X]_\x11VB[_\x11DXQ\x12a_^QU]I@\\\x1c
```

A esta cadena de bytes se le aplicó el cifrado XOR con la llave `21004` (mi carnet) y se obtuvo el texto

```text
Seventeen days later, the Straw Hats, Trafalgar Law, and Raizo's samurai comrades freed him from the Poneglyph.
```

#### Flag

Luego de procesar la imagen, se buscó la flag. Se encontraron 11 archivos llamados `flag.txt` en el contenedor.

Explorando dichos archivos se encontró un contenido fuera de lo común: una cadena de caracteres que no representaban una
oración coherente. De esta manera se identificó que el archivo `./ONEPIECE/Zou/Right_Fore_Leg/Casa_de_Kawamatsu/flag.txt` contenía la flag.

Esta vez era necesario romper un XOR Cipher Custom (como lo dice el nombre del reto), por lo que esta vez se usó un enfoque
de fuerza bruta para encontrar la llave. Se probó con todas las combinaciones posibles de 4 caracteres alfanuméricos y se encontró la
llave `1234`

> Se había preparado el método de análisis de frecuencia para el caso de que fuera necesario analizar las llaves posibles,
> pero no fue necesario debido a que las demás combinaciones de 4 caracteres alfanuméricos generaban errores de tipo UnicodeDecodeError.

Esto resultó en la flag:

```text
FLAG_fcbd8689ff72334dbd43f119306e1a9d
```

### Nami

Para el cuarto desafío, se siguió un procedimiento similar a los anteriores.

```bash
docker exec -it {challengeX_ctf} bash
```

Usando la flag encontrada en el reto anterior, se inicia sesión como `nami`:

```bash
su nami
password: FLAG_fcbd8689ff72334dbd43f119306e1a9d
```

#### Poneglyph

![Poneglyph Nami]((https://github.com/markalbrand56/Cifrados-Proyecto-1/blob/main/challenges_volumes/nami_ctf/poneglyph.jpeg))

Nuevamente, se buscó el archivo `poneglyph.zip`, encontrándolo en la carpeta `./ONEPIECE/Dressrosa/Royal_Palace/Casa_de_Riku_Dold_III`.
Siguiendo el mismo procedimiento que en el primer desafío, se extrajo el archivo y se obtuvo la imagen `poneglyph.jpeg`.
Esta imagen se movió al volumen compartido `/nami_ctf` para trabajar con ella en la máquina local.

Al abrir la imagen, se observó nuevamente un texto en la esquina superior izquierda. Esta vez el texto era prácticamente ilegible a simple vista.
Imprimiendo los bytes de la imagen, se encontraron caracteres fuera de lugar, con el mismo patrón que en los ejercicios anteriores.
Esto permitió encontrar el texto que parecía ser la llave.

```text
sWDUF\x12c_R]\\\x11TUW[AXUFWU\x10D\\W\x11b_UV\x11`_ZWV\\IDZ\x1d\x10yZGPBQGZX\x10ULB]QYZWU\x10Y@A\x11@EFB^CU\x14]W\x10BQDTQ\\]\\V\x10D\\W\x11\\_WSEY_Z\x12^V\x10xSDWX\x14fP\\U\x14EYU^\x14[EC\x10]\\W_BYSEY_Z\x12FQC\x14Q^]R]\\TT\x10C[EX\x10@ZPD\x10[T\x11DXQ\x12^DXQ@\x11DXFWT\x10b[SU\x10`[\\TW\\MBYC\x1e
```

A esta cadena de bytes se le aplicó el cifrado ChaCha20 con la llave `21004` (mi carnet) y se obtuvo el texto:

```text
After Robin deciphered the Road Poneglyph, Inuarashi explained its purpose of revealing the location of Laugh Tale when its information was combined with that of the other three Road Poneglyphs.
```

#### Flag

Luego de procesar la imagen, se buscó la flag. Se encontraron 10 archivos llamados `flag.txt` en el contenedor.
Explorando dichos archivos se encontró un contenido fuera de lo común: una cadena de caracteres que no representaban una
oración coherente. De esta manera se identificó que el archivo `./ONEPIECE/Zou/Right_Fore_Leg/Casa_de_Kawamatsu/flag.txt` contenía la flag.

Para este reto final, se necesitaba romper el algoritmo de cifrado ChaCha20. Este algoritmo es más complejo que los anteriores debido
a que necesita una llave y un nonce. La llave debe de ser de 32 bytes y el nonce es posible que sea de 8, 12 o 24 bytes (al menos en la librería de python).
Esto significaba que si se quería hacer por fuerza bruta, era necesario generar todas las combinaciones posibles de llaves,
y a cada combinación de llave se le necesitaría generar todas las combinaciones posibles de nonce, de las 3 posibles longitudes.

Esto hubiera sido un proceso extremadamente largo, pero por suerte se decidió probar algo simple como utilizar como llave 
`21004` y como nonce `21004`, lo cuál resultó ser la combinación correcta.

## Resultado

### Texto

```text
When Jack and the Beasts Pirates invaded Zou to look for Raizo of Wano Country,
the Mink Tribe chained him to the Road Poneglyph within the Whale Tree to keep him from showing himself.
Seventeen days later, the Straw Hats, Trafalgar Law, and Raizo's samurai comrades freed him from the Poneglyph.
After Robin deciphered the Road Poneglyph, Inuarashi explained its purpose of revealing the location of Laugh Tale when its information was combined with that of the other three Road Poneglyphs.
```

## Developer's

<a href="https://github.com/markalbrand56">
  <img width='75' src="https://avatars.githubusercontent.com/u/62487869?v=4" alt="Mark Albrand" />
</a>

* [![Linkedin][Linkedin]][Linkedin-mark]
* [![GitHub][GitHub]][GitHub-lud]

<p align="right">(<a href="#readme-top">Ir al inicio</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[Linkedin-mark]: https://www.linkedin.com/in/mark-alexander-albrand-mendoza/
[Linkedin]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[Github-lud]: https://github.com/markalbrand56
[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
