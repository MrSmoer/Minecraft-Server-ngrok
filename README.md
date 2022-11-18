# Minecraft-Server-ngrok
This a simple docker-compose for quickly spinning up a minecraft-server with ngrok.
Standard is 1.19.2

## Instructions
This compose uses two containers, one provides ngrok tunneling to avoid port-forwarding, the other one for the minecraft-server. As a best practive you should always read a Dockerfile before running it:
- [docker-compose](docker-compose.yml)
- [minecraft-server Dockerfile](minecraft/Dockerfile)
### ngrok
You will need to set `NGROK_AUTHTOKEN` to your ngrok-auth-token. You can also specify it in your compose file.
The IP of the server is going to be visible on http://localhost:4040 on the ngrok status-page.
### Minecraft
The version is currently 1.19.2. You can replace the link in the docker-compose with another version of the server.jar. [Here is a list](jarfiles.txt) <br>
Currently, the server.jar is downloaded from Minecraft.net during build. <br>
You can acces the server through ngrok, as well as on `localhost:25565`

The server command-line is usually available through the following command, but be aware that `ctrl+c` **kills the server. USE CTRL-P+CTRL+Q**
```
docker attach minecraft-server-ngrok_minecraft_1
``` 

After the obligatory first failed start you will need to accept the minecraft eula:<br>

- set `eula=true` in the environment section of the compose

The minecraft-data is an ordinary minecraft-server-folder
## TL;DR
- Set `NGROK_AUTHTOKEN`
- Edit eula from false to `eula=true` in docker-compose
- Run `docker-compose up -d --build`
- Open http://localhost:4040 and copy url without `tcp://`
- Join the server
- Run `docker attach minecraft-server-ngrok_minecraft_1`
- Type `op <your_username>` 
