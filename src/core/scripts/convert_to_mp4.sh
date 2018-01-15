#!/usr/bin/env bash

sleep 3
cd $1
ffmpeg -i $2 -vcodec h264 $3
rm $2
