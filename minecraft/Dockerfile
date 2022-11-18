FROM alpine:latest
RUN apk add openjdk17
RUN mkdir /minecraft-server/jar -p
ARG JAR_DOWNLOAD_LINK
ENV JAR_DOWNLOAD_LINK ${JAR_DOWNLOAD_LINK}
RUN wget ${JAR_DOWNLOAD_LINK} -O server.jar
RUN mv server.jar /minecraft-server/jar
WORKDIR /minecraft-server/data
COPY entrypoint.sh /minecraft-server/jar/entrypoint.sh
RUN chmod +x /minecraft-server/jar/entrypoint.sh
#ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT [ "/minecraft-server/jar/entrypoint.sh","java -jar /minecraft-server/jar/server.jar"]