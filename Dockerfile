FROM debian:buster-20230522

RUN apt update -y && \
	apt upgrade -y && \
	apt install python3 \
				python3-pip \
				vim  -y


RUN pip3 install cryptography && \
	pip3 install pyAesCrypt && \
	pip3 install pycrypto

COPY parser.py parser.py
COPY ft_encript.py ft_encript.py
COPY stockholm.py stockholm.py
COPY README.md README.md

ADD kk.tar.gz /root/infection
