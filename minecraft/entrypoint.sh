#!/bin/sh
if [[ "$eula" == "true" ]]; then 
     echo eula=true > /minecraft-server/data/eula.txt
fi
eval $@



