FROM alpine:latest
RUN apk add openjdk17
RUN mkdir /minecraft-server/jar -p
RUN mkdir /minecraft-server/data -p
RUN echo eula=true > /minecraft-server/data/eula.txt
RUN wget https://piston-data.mojang.com/v1/objects/f69c284232d7c7580bd89a5a4931c3581eae1378/server.jar
RUN mv server.jar /minecraft-server/jar
WORKDIR /minecraft-server/data
RUN echo eula=true > eula.txt
ENTRYPOINT java -jar /minecraft-server/jar/server.jar