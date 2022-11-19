FROM alpine:latest
RUN mkdir /minecraft-server/jar -p
RUN apk add openjdk17-jre-headless
COPY versions.csv /minecraft-server/jar/versions.csv
ARG MINECRAFT_VERSION
ENV MINECRAFT_VERSION ${MINECRAFT_VERSION}
RUN wget $(awk -v ref="$MINECRAFT_VERSION" -F','  ' $1 == ref  { print substr($2, 1, length($2)-1) }' /minecraft-server/jar/versions.csv) -O server.jar
RUN mv server.jar /minecraft-server/jar
WORKDIR /minecraft-server/data
COPY entrypoint.sh /minecraft-server/jar/entrypoint.sh
RUN chmod +x /minecraft-server/jar/entrypoint.sh
ENTRYPOINT [ "/minecraft-server/jar/entrypoint.sh","java -jar /minecraft-server/jar/server.jar"]