FROM alpine:latest
RUN apk add openjdk17
RUN mkdir /minecraft-server/jar -p
RUN wget https://piston-data.mojang.com/v1/objects/f69c284232d7c7580bd89a5a4931c3581eae1378/server.jar
RUN mv server.jar /minecraft-server/jar
WORKDIR /minecraft-server/data
COPY entrypoint.sh /minecraft-server/jar/entrypoint.sh
RUN chmod +x /minecraft-server/jar/entrypoint.sh
#ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT [ "/minecraft-server/jar/entrypoint.sh","java -jar /minecraft-server/jar/server.jar"]