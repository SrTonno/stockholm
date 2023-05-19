FROM debian

RUN apt update -y && \
	apt upgrade -y && \
	apt install python3 python3-pip -y


COPY stockholm.py stockholm.py

RUN pip install cryptography && \
	pip install pyAesCrypt

ADD kk.tar.gz /home/
