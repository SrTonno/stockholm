# stockholm

## Descripción
El programa "stockholm.py" imita el comportamiento del ransomware WannaCry, pero se limita a aplicar en el directorio "infection" dentro del directorio home del usuario. Este programa tiene la capacidad de encriptar y desencriptar los archivos dentro de ese directorio utilizando una contraseña proporcionada por el usuario.

## Opciones
- `(default)`: Solicita una contraseña al usuario y encripta los archivos dentro de "infection".
- `-r` o `--reverse`: Solicita una contraseña al usuario y desencripta los archivos previamente encriptados dentro de "infection".
- `-s` o `--silent`: Ejecuta el programa en modo silencioso, sin mostrar ningún output en pantalla.
- `-v` o `--version`: Muestra la versión del programa.
- `-h` o `--help`: Muestra la ayuda y la lista de opciones.

## Ejemplo

### Encriptar
> python3 stockholm.py <contraseña>
### Desncriptar
> python3 stockholm.py -r
> Introduce la contraeña: <contraseña>
## Lenguaje
Este programa está escrito en Python3.
 
### Librerías utilizadas
- sys
- os
- re
- hashlib
- argparse
- platform
- pyAesCrypt
- pycrypto

#### Para instalar las dependencias
> pip install -r requirements.txt
