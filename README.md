# Minecraft-Server-ngrok
This a simple docker-compose for quickly spinning up a Minecraft-Server(java-edition) without opening a port in your router through ngrok.
Default version right now is 1.21.1

## Instructions
This compose uses two containers. One provides ngrok tunneling to avoid port-forwarding, the other one is the Minecraft-server. As a best practive you should always read a Dockerfile before running it:
- [docker-compose](docker-compose.yml)
- [minecraft-server Dockerfile](minecraft/Dockerfile)
- [entrypoint.sh](minecraft/entrypoint.sh)

### ngrok
You will need to set `NGROK_AUTHTOKEN` to your ngrok-auth-token. You can also specify it in your compose file.
The IP of the server is going to be visible on [http://localhost:4040](http://localhost:4040); the ngrok status-page.
### Minecraft
The default version 1.21.1. [Here is the list of links to the official Minecraft server-jars (versions.csv)](minecraft/versions.csv) <br>
Currently, the server.jar is downloaded during build. The version has to be specified in docker-compose as a the build-arg `MINECRAFT_VERSION: 1.21.1` and needs to have a link in the versions.csv<br>
You can add links to your own server.jar's to `versions.csv` as well. <br>
If you need a newer version, check the versions.csv. If your version is already inside, you just need to edit the `MINECRAFT_VERSION` in the docker compose. If it is not there yet, just run  the [getServerVersions.py](scripts/getServerVersions.py) script. This repo will try to update it once a week with a github action.<br>
Your Minecraft-Server will be accessible through ngrok, as well as on `localhost:25566`

**You will need to accept the Minecraft eula:**<br>

- set `eula=true` in the environment section of the [compose](docker-compose.yml#L13)

The command-line oft the Minecraft server is usually available through the following command, but **be aware that `ctrl+c` kills the server. USE CTRL-P+CTRL+Q to exit instead**
```
docker attach minecraft-server-ngrok_minecraft_1
``` 

You can put your very own Minecraft-server-folder in the minecraft-data directory, which is going to be created by docker after the first launch.

## TL;DR
- Set `NGROK_AUTHTOKEN`
- Edit eula from false to `eula=true` in docker-compose
- Run `docker-compose up -d --build`
- Open http://localhost:4040 and copy url without `tcp://`
- Join the server
- Run `docker attach minecraft-server-ngrok_minecraft_1`
- Type `op <your_username>` 
