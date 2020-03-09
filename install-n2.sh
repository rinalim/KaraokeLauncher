sudo apt update
sudo apt install ubuntu-mate-desktop -y
sudo apt install wget vlc fcitx-hangul fcitx-config-gtk language-pack-ko -y
sudo apt install openjdk-8-jdk -y

#if [ ! -f videoKaraoke-0.1.0-dist.zip ]; then
#  wget http://download1510.mediafire.com/q9nzokcw8trg/g567nzri99pzifu/videoKaraoke-0.1.0-dist.zip
#fi
unzip -o videoKaraoke-0.1.0-dist.zip -d /home/pigaming/RetroArena/roms/kodi/videoKaraoke
#rm videoKaraoke-0.1.0-dist.zip

cp -r ./patch/kodi /home/pigaming/RetroArena/roms/
cp ./patch/setting.ini /home/pigaming/RetroArena/roms/kodi/videoKaraoke/
cp ./patch/intro.* /home/pigaming/RetroArena/roms/kodi/videoKaraoke/res/
sudo cp ./patch/youtube.luac /usr/lib/aarch64-linux-gnu/vlc/lua/playlist/
sudo cp ./patch/lightdm.conf /etc/lightdm/

sudo chmod 755 ./start-n2.sh

python ./joy-setup.py

sudo /home/pigaming/mali/install.sh 

sudo reboot