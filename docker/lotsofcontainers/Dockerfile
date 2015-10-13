FROM debian:jessie

MAINTAINER pono@osuosl.org

RUN echo "deb http://debian.osuosl.org/debian jessie main" > /etc/apt/sources.list
RUN echo "deb http://debian.osuosl.org/debian jessie-updates main" >> /etc/apt/sources.list
RUN echo "deb http://security.debian.org jessie/updates main" >> /etc/apt/sources.list
RUN apt-get -q update
RUN apt-get install -y man \
 sudo \
 openssh-server \
 python-pip virtualenv \
 screen irssi weechat-curses \
 vim nano less \
 git \
 locales
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
RUN locale-gen
RUN service ssh start
RUN useradd -m -G users -s /bin/bash ANIMAL
RUN echo ANIMAL:PASSWORD|chpasswd
RUN usermod -G sudo ANIMAL

EXPOSE 22
EXPOSE 8080

CMD ["/usr/sbin/sshd", "-D"]
