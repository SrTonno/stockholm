# stockholm.py

## Descripción
El programa "stockholm.py" imita el comportamiento del ransomware WannaCry, pero se limita a aplicar en el directorio "infection" dentro del directorio home del usuario. Este programa tiene la capacidad de encriptar y desencriptar los archivos dentro de ese directorio utilizando una contraseña proporcionada por el usuario.

## Opciones
- (default): Solicita una contraseña al usuario y encripta los archivos dentro de "infection".
- -r: Solicita una contraseña al usuario y desencripta los archivos previamente encriptados dentro de "infection".
- -s: Ejecuta el programa en modo silencioso, sin mostrar ningún output en pantalla.
- -v: Muestra la versión del programa.
- -h: Muestra la ayuda y la lista de opciones.

## Ejemplo

### Encriptar
> python3 stockholm.py <contraseña>
### Desncriptar
> python3 stockholm.py -r <contraseña>
## Lenguaje
Este programa está escrito en Python3.

## Librerías utilizadas
- sys
- os
- re
- hashlib
- argparse
- struct
- time
- platform
- pyAesCrypt
