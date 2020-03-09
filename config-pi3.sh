sudo service lightdm stop
dconf write /org/mate/panel/toplevels/bottom/auto-hide true
dconf write /org/mate/panel/toplevels/top/auto-hide true
cp -r ./patch/fcitx/* /home/pi/.config/fcitx/
mkdir /home/pi/.config/autostart
cp ./patch/start.sh.desktop-pi3 /home/pi/.config/autostart/start.sh.desktop
sudo service lightdm start