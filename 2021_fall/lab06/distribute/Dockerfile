FROM ubuntu:focal
MAINTAINER YingMuo

RUN apt-get update
RUN apt-get install xinetd -qy
RUN useradd -m babyrop
RUN chown -R root:root /home/babyrop
RUN chmod -R 755 /home/babyrop

CMD ["/usr/sbin/xinetd","-dontfork"]
