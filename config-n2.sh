sudo service lightdm stop
dconf write /org/mate/panel/toplevels/bottom/auto-hide true
dconf write /org/mate/panel/toplevels/top/auto-hide true
cp -r ./patch/fcitx/* /home/pigaming/.config/fcitx/
mkdir /home/pigaming/.config/autostart
cp ./patch/start.sh.desktop /home/pigaming/.config/autostart/
sudo service lightdm start