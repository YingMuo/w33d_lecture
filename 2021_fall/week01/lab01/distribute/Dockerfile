FROM ubuntu:focal
MAINTAINER YingMuo

RUN apt-get update
RUN apt-get install xinetd -qy
RUN useradd -m guess
RUN chown -R root:root /home/guess
RUN chmod -R 755 /home/guess

CMD ["/usr/sbin/xinetd","-dontfork"]
