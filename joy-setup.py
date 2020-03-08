#!/usr/bin/python

import os, sys
from subprocess import *
import xml.etree.ElementTree as ET

PATH_ROM = '/home/pigaming/RetroArena/roms/kodi/videoKaraoke/'
ES_INPUT = '/opt/retroarena/configs/all/emulationstation/es_input.cfg'
RETROARCH_CFG = '/opt/retroarena/configs/all/retroarch-joypads/'

def load_es_cfg():
    doc = ET.parse(ES_INPUT)
    root = doc.getroot()
    #tag = root.find('inputConfig')
    tags = root.findall('inputConfig')
    num = 1
    print '\n'
    for i in tags:
        print str(num) + ". " + i.attrib['deviceName']
        num = num+1
    dev_select = input('\nSelect your joystick: ')

    return tags[dev_select-1].attrib['deviceName']


def load_retroarch_cfg(dev_name):
    print 'Device Name: ', dev_name, '\n'
    
    retroarch_key = {}
    f = open(RETROARCH_CFG + dev_name + '.cfg', 'r')
    while True:
        line = f.readline()
        if not line: 
            break
        if '_btn' in line or '_axis' in line:
            line = line.replace('\n','')
            line = line.replace('input_','')
            line = line.replace('_btn','')
            line = line.replace('_axis','')
            words = line.split()
            retroarch_key[words[0]] = words[2].replace('"','')
    f.close()
    
    f = open(PATH_ROM + "button.cfg", 'w')
    f.write(str(retroarch_key)+'\n')
    f.close()

print '\n\n'
use_joy = input('Activate joystick input? (1=Yes, 2=No): ')
if use_pause == 1:
    dev_name = load_es_cfg()
    load_retroarch_cfg(dev_name)