FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
&& apt-get upgrade \
&& apt-get install -y python3 git \
&& git config --global user.email "john.h.johnston4@gmail.com" \
&& git config --global user.name "John Johnston" \
&& mkdir Projects \
&& cd /Projects \
&& git clone https://github.com/jjohn49/MyBot.git

COPY entryPoint.py .

ENTRYPOINT [ "python3", "entryPoint.py" ]