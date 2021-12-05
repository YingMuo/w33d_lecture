FROM ubuntu:focal
MAINTAINER YingMuo

RUN apt-get update
RUN apt-get install xinetd -qy
RUN useradd -m rop_revenge
RUN chown -R root:root /home/rop_revenge
RUN chmod -R 755 /home/rop_revenge

CMD ["/usr/sbin/xinetd","-dontfork"]
