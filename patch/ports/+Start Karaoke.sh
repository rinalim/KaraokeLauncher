#!/bin/bash
sudo service lightdm start
if [ ! -f /home/pi/.config/autostart/start.sh.desktop ]; then
  sleep 10
  sudo service lightdm stop
  dconf write /org/mate/panel/toplevels/bottom/auto-hide true
  dconf write /org/mate/panel/toplevels/top/auto-hide true
  cp -r /home/pi/KaraokeLauncher/patch/fcitx/* /home/pi/.config/fcitx/
  mkdir /home/pi/.config/autostart
  cp /home/pi/KaraokeLauncher/patch/start.sh.desktop-pi3 /home/pi/.config/autostart/start.sh.desktop
  sudo service lightdm start
fi
/usr/bin/python /home/pi/KaraokeLauncher/joy-input.py /dev/input/js0 &
/usr/bin/python /home/pi/KaraokeLauncher/run.py
sudo service lightdm stop