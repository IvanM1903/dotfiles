#!/bin/sh

#configuracion teclado español
setxkbmap es &
#ajustar segundo escritorio
xrandr --output HDMI-A-0 --mode 2560x1080 --rate 75 --scale 1.25x1.25 --noprimary --right-of eDP
#fondo de pantalla
feh --bg-fill ~/.config/qtile/wallpaper.png --bg-fill ~/.config/qtile/wallpaper.png
#compositor de ventanas
picom &
#cambiar botones zurdo
xmodmap -e "pointer = 3 2 1"
