#-*-coding: utf-8 -*-
#!/usr/bin/python

import os, sys, struct, time, fcntl, termios, signal
import curses, errno
import xml.etree.ElementTree as ET
import ast

#    struct js_event {
#        __u32 time;     /* event timestamp in milliseconds */
#        __s16 value;    /* value */
#        __u8 type;      /* event type */
#        __u8 number;    /* axis/button number */
#    };

reload(sys)
sys.setdefaultencoding('utf-8')

JS_MIN = -32768
JS_MAX = 32768
JS_REP = 0.20

JS_THRESH = 0.75

JS_EVENT_BUTTON = 0x01
JS_EVENT_AXIS = 0x02
JS_EVENT_INIT = 0x80

if os.path.isdir("/home/pigaming/RetroArena") == True :
    PATH_ROM = '/home/pigaming/RetroArena/roms/kodi/videoKaraoke/'
if os.path.isdir("/home/pi/RetroPie") == True :
    PATH_ROM = '/home/pi/RetroPie/roms/ports/videoKaraoke/'

SELECT_BTN_ON = False
START_BTN_ON = False

event_format = 'IhBB'
event_size = struct.calcsize(event_format)
js_fds = []
btn_select = -1
btn_start = -1

retroarch_key = {}
user_key = {}

es_conf = 1

def run_cmd(cmd):
    # runs whatever in the cmd variable
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output
    
def full_arg():
    if len(sys.argv) > 2 and sys.argv[2] == '-full':
        return True
    else:
        return False
        
def load_button():

    global retroarch_key

    if os.path.isfile(PATH_ROM + "button.cfg") == True:
        f = open(PATH_ROM + "button.cfg", 'r')
        retroarch_key = ast.literal_eval(f.readline())
        f.close()
    else:
        sys.exit(0)

def is_running(pname):
    ps_grep = run_cmd("ps -ef | grep " + pname + " | grep -v grep")
    if len(ps_grep) > 1:
        return True
    else:
        return False
    
def signal_handler(signum, frame):
    close_fds(js_fds)
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def get_devices():
    devs = []
    if sys.argv[1] == '/dev/input/jsX':
        for dev in os.listdir('/dev/input'):
            if dev.startswith('js'):
                devs.append('/dev/input/' + dev)
    else:
        devs.append(sys.argv[1])

    return devs

def open_devices():
    devs = get_devices()

    fds = []
    for dev in devs:
        try:
            fds.append(os.open(dev, os.O_RDONLY | os.O_NONBLOCK ))
        except:
            pass

    return devs, fds

def close_fds(fds):
    for fd in fds:
        os.close(fd)

def read_event(fd):
    while True:
        try:
            event = os.read(fd, event_size)
        except OSError, e:
            if e.errno == errno.EWOULDBLOCK:
                return None
            return False

        else:
            return event
    
def process_event(event):

    global SELECT_BTN_ON, START_BTN_ON

    (js_time, js_value, js_type, js_number) = struct.unpack(event_format, event)

    # ignore init events
    if js_type & JS_EVENT_INIT:
        return False

    if js_type == JS_EVENT_BUTTON:
        if js_value == 1:
            if js_number == btn_select:
                SELECT_BTN_ON = True
            elif js_number == btn_start:
                START_BTN_ON = True
            else:
                return False
        elif js_value == 0:
            if js_number == btn_select:
                SELECT_BTN_ON = False
            elif js_number == btn_start:
                START_BTN_ON = False
            else:
                return False
        
        if SELECT_BTN_ON == True and START_BTN_ON == True:
            #print "Select+Start Pushed"
            os.system("pkill -ef Karaoke.jar")
            sys.exit(0)

    return True

def main():
    
    global btn_select, btn_start
    load_button()
    
    btn_select = int(retroarch_key['select'])
    btn_start = int(retroarch_key['start'])
    
    js_fds=[]
    rescan_time = time.time()
    while True:
        do_sleep = True
        if not js_fds:
            js_devs, js_fds = open_devices()
            if js_fds:
                i = 0
                current = time.time()
                js_last = [None] * len(js_fds)
                for js in js_fds:
                    js_last[i] = current
                    i += 1
            else:
                time.sleep(1)
        else:
            i = 0
            for fd in js_fds:
                event = read_event(fd)
                if event:
                    do_sleep = False
                    #if time.time() - js_last[i] > JS_REP:
                    if time.time() - js_last[i] > 0:                        
                        if process_event(event):
                            js_last[i] = time.time()
                elif event == False:
                    close_fds(js_fds)
                    js_fds = []
                    break
                i += 1

        if time.time() - rescan_time > 2:
            rescan_time = time.time()
            if cmp(js_devs, get_devices()):
                close_fds(js_fds)
                js_fds = []

        if do_sleep:
            time.sleep(0.01)

if __name__ == "__main__":
    import sys

    try:
        main()

    # Catch all other non-exit errors
    except Exception as e:
        sys.stderr.write("Unexpected exception: %s" % e)
        sys.exit(1)

    # Catch the remaining exit errors
    except:
        sys.exit(0)
