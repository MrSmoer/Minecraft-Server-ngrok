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
The version is currently 1.19.2. You can replace the link in the Dockerfile for another version of the server.jar. <br>
The server.jar is downloaded from Minecraft.net during build. <br>
You can acces the server through ngrok, as well as on `localhost:5565`

After the obligatory first failed start you will need to accept the minecraft eula. There are multiple ways that do the same:<br>
<br>
- edit `minecraft-data/eula.txt` inside the volume. 
- run ```sudo echo eula=true > minecraft-data/eula.txt``` 
- or set `eula=true` in the environment section of the compose.

The minecraft-data is an ordinary minecraft-server-folder
## TLDR
- Set `NGROK_AUTHTOKEN`
- Edit eula from false to `eula=true` in docker-compose
