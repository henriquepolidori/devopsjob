FROM ubuntu:20.04

RUN apt install python3-pip
RUN python3 install mysql.connector

CMD ["/bin/sleep", "3650d"]
