sudo apt update
sudo apt install xserver-xorg -y
sudo apt install mate-desktop-environment-core -y
sudo apt install lightdm -y
sudo apt install wget vlc fcitx-hangul fcitx-config-gtk dconf-cli fonts-unfonts-core -y
sudo apt install openjdk-8-jdk -y

#if [ ! -f videoKaraoke-0.1.0-dist.zip ]; then
#  wget http://download1510.mediafire.com/q9nzokcw8trg/g567nzri99pzifu/videoKaraoke-0.1.0-dist.zip
#fi
unzip -o videoKaraoke-0.1.1-dist.zip -d /home/pi/RetroPie/roms/ports/videoKaraoke
#rm videoKaraoke-0.1.0-dist.zip

cp -r ./patch/ports /home/pi/RetroPie/roms/
cp ./patch/setting.ini /home/pi/RetroPie/roms/ports/videoKaraoke/
cp ./patch/intro.* /home/pi/RetroPie/roms/ports/videoKaraoke/res/
sudo cp ./patch/youtube.luac /usr/lib/arm-linux-gnueabihf/vlc/lua/playlist/
sudo cp ./patch/lightdm.conf-pi3 /etc/lightdm/lightdm.conf

sudo chmod 755 ./start-pi3.sh

python ./joy-setup.py

sudo reboot