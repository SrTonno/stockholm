# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parser.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tvillare <tvillare@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/21 13:02:20 by tvillare          #+#    #+#              #
#    Updated: 2023/05/21 17:35:43 by tvillare         ###   ########.fr        #
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


def parseo():
	parser = argparse.ArgumentParser(description='Una replica del querer llorar(wanna cry)', add_help=False)

	parser.add_argument('-r', '--reverse',
					dest="r",
					type=str,
					help='Cantidad de subniveles debusqueda')

	parser.add_argument('-s', '--silent',
					dest='s',
					action='store_true',
					help='No mostrar output')

	parser.add_argument('-v', '--version',
					dest='v',
					action='store_true',
					help='vecion del programa')

	parser.add_argument('-h', '--help',
					dest='h',
					action='store_true',
					help='nueva ayuda')

	args = parser.parse_args()
	return args

def ft_help():
	if not(os.path.exists("./README.md")):
		print("Error: No existe Readme.md")
		return
	with open('README.md', 'r') as archivo:
		contenido = archivo.read()
	print(contenido)
