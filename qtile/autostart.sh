#!/bin/sh

#icons System

# systray battery icon
#cbatticon -u 5 &
# systray volume
volumeicon &

udiskie -t &

nm-applet &

nitrogen --restore &