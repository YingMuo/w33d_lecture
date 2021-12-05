FROM ubuntu:focal
MAINTAINER YingMuo

RUN apt-get update
RUN apt-get install xinetd -qy
RUN useradd -m rop_migration
RUN chown -R root:root /home/rop_migration
RUN chmod -R 755 /home/rop_migration

CMD ["/usr/sbin/xinetd","-dontfork"]
