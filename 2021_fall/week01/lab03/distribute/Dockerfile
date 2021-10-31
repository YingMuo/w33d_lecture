FROM ubuntu:focal
MAINTAINER YingMuo

RUN apt-get update
RUN apt-get install xinetd -qy
RUN useradd -m ret2sc
RUN chown -R root:root /home/ret2sc
RUN chmod -R 755 /home/ret2sc

CMD ["/usr/sbin/xinetd","-dontfork"]
