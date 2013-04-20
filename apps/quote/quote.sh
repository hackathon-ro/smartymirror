#!/bin/bash

orginal=`pwd`
cd /home/pi/smartmirror/apps/quote
/usr/games/fortune -s >tell
/usr/games/xcowsay < tell &
./speech_from_file.sh tell
cd $original
