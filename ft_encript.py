# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_encript.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tvillare <tvillare@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/21 13:08:16 by tvillare          #+#    #+#              #
#    Updated: 2023/05/27 16:54:10 by tvillare         ###   ########.fr        #
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

# Tamaño del búfer de cifrado/descifrado (en bytes)
buffer_size = 64 * 1024

# Cifrado de un archivo
def cifrar_archivo(input, clave, s):
	output = input + ".ft"
	if os.path.exists(output):
		if (s != True):
			print(f"Error {output} ya existe se creara con _stockholm.ft")
		output = input + "_stockholm.ft"
	if not(os.path.exists(output)):
		pyAesCrypt.encryptFile(input, output, clave, buffer_size)
		os.remove(input)
		if (s != True):
			print(f"encrypt -> {output}")

# Descifrado de un archivo cifrado
def descifrar_archivo(input, clave, s):
	#output = input.rstrip(".ft")
	output = re.sub(r"(_stockholm)?\.ft$", "", input)
	if not(os.path.exists(output)):
		try:
			pyAesCrypt.decryptFile(input, output, clave, buffer_size)
			os.remove(input)
			if (s != True):
				print(f"dencrypt -> {output}")
		except:
			return



def check_passwd(secret):
	if (secret == None) or (len(secret) < 16):
		print("Contraseña muy corta")
		sys.exit()
	#passwd = hashlib.sha256(secret.encode('utf-8')).digest()
	return secret
