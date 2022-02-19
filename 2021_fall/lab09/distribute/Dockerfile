FROM ubuntu:focal
MAINTAINER YingMuo

RUN apt-get update
RUN apt-get install xinetd -qy
RUN useradd -m rop_migration_rev
RUN chown -R root:root /home/rop_migration_rev
RUN chmod -R 755 /home/rop_migration_rev

CMD ["/usr/sbin/xinetd","-dontfork"]
