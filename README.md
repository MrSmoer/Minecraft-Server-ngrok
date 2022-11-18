# Minecraft-Server-ngrok
This a simple docker-compose for quickly spinning up a minecraft-server with ngrok.

## Instructions
This compose uses two containers, one provides ngrok tunneling to avoid port-forwarding, the other one for the minecraft-server. As a best practive you should always read a Dockerfile before running it:
- [docker-compose](docker-compose.yml)
- [minecraft-server Dockerfile](minecraft/Dockerfile)
### ngrok
You will need to set `NGROK_AUTHTOKEN` to your ngrok-auth-token. You can also specify it in your compose file.
The IP of the server is going to be visible on http://localhost:4040 on the ngrok status-page.
### Minecraft
It is available through ngrok, as well as on `localhost:5565`

The server.jar is downloaded from Minecraft.net during build.
After the obligatory first failed start you will need to enable the minecraft eula by editing the file `minecraft-data/eula.txt` inside the volume. 

Alternatively you can run
```sudo echo eula=true > minecraft-data/eula.txt``` 
 
 You can also set `eula=true` in the environment section of the compose.

The minecraft-data is an ordinary minecraft-server-folder
## TLDR
- Set `NGROK_AUTHTOKEN`
- Edit eula from false to `eula=true` in docker-compose
