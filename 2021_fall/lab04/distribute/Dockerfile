FROM ubuntu:focal
MAINTAINER YingMuo

RUN apt-get update
RUN apt-get install xinetd -qy
RUN useradd -m canary
RUN chown -R root:root /home/canary
RUN chmod -R 755 /home/canary

CMD ["/usr/sbin/xinetd","-dontfork"]
