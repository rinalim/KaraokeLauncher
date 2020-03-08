dconf write /org/mate/panel/toplevels/bottom/auto-hide true
dconf write /org/mate/panel/toplevels/top/auto-hide true
cp ./patch/config /home/pigaming/.config/fcitx/
mkdir /home/pigaming/.config/autostart
cp ./patch/start.sh.desktop /home/pigaming/.config/autostart/
sudo service lightdm restart