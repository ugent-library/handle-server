FROM openjdk:jre-alpine

WORKDIR /opt/handle-server
COPY . .

CMD /opt/handle-server/bin/hdl-server /opt/handle-server/svr_1
