#!/bin/bash
sudo service lightdm start
/usr/bin/python /home/pigaming/KaraokeLauncher/joy-input.py /dev/input/js0
/usr/bin/python /home/pigaming/KaraokeLauncher/run.py
sudo service lightdm stop