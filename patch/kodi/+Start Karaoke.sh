#!/bin/bash
sudo service lightdm start
if [ ! -f /home/pigaming/.config/autostart/start.sh.desktop ]; then
  sleep 10
  sudo service lightdm stop
  dconf write /org/mate/panel/toplevels/bottom/auto-hide true
  dconf write /org/mate/panel/toplevels/top/auto-hide true
  cp -r /home/pigaming/KaraokeLauncher/patch/fcitx/* /home/pigaming/.config/fcitx/
  mkdir /home/pigaming/.config/autostart
  cp /home/pigaming/KaraokeLauncher/patch/start.sh.desktop /home/pigaming/.config/autostart/start.sh.desktop
  sudo service lightdm start
fi
/usr/bin/python /home/pigaming/KaraokeLauncher/joy-input.py /dev/input/js0 &
/usr/bin/python /home/pigaming/KaraokeLauncher/run.py
sudo service lightdm stop