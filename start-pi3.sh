#!/bin/bash

if [ -f /home/pi/RetroPie/roms/ports/urserver/urserver ]; then
  /home/pi/RetroPie/roms/ports/urserver/urserver --daemon
fi
pushd /home/pi/RetroPie/roms/ports/videoKaraoke
java -jar VideoKaraoke.jar
popd