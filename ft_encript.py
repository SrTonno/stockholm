# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_encript.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tvillare <tvillare@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/21 13:08:16 by tvillare          #+#    #+#              #
#    Updated: 2023/05/21 14:48:55 by tvillare         ###   ########.fr        #
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

# Cifrado de un archivo
def cifrar_archivo(input, clave, s):
	output = input + ".ft"
	if not(os.path.exists(output)):
		pyAesCrypt.encryptFile(input, output, clave, buffer_size)
		os.remove(input)
		if (s != True)
				print(f"file -> {output}")

# Descifrado de un archivo cifrado
def descifrar_archivo(input, clave):
	#output = input.rstrip(".ft")
	output = re.sub(r"\.ft$", "", input)
	if not(os.path.exists(output)):
		pyAesCrypt.decryptFile(input, output, clave, buffer_size)
		os.remove(input)
		if (s != True)
			print(f"file -> {output}")

# Tamaño del búfer de cifrado/descifrado (en bytes)
buffer_size = 64 * 1024


def get_passwd():
	secret = input("Introduce la contraeña: ")
	if (len(secret) < 16):
		print("Contraseña muy corta")
		sys.exit()
	passwd = hashlib.sha256(secret.encode('utf-8')).digest()
	return passwd

def check_passwd(secret):
	if (len(secret) < 16):
		print("Contraseña muy corta")
		sys.exit()
	passwd = hashlib.sha256(secret.encode('utf-8')).digest()
	return passwd
