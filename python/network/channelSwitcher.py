#gnu/linux only
import os
import itertools as itr
import time
import getopt
import sys

def help():
    print "[X] not enough parameters\n[*] -i for interface"
    sys.exit(0)

def switcher():
    while True:
        for channel in itr.chain(range(1, 13), range(36,60,4), range(100,144,4), range(149,165,4)):
            os.popen("sudo iwconfig %s channel %s" % (interface, str(channel)), 'w')
            print "[+] Switched to channel " + str(channel)
            time.sleep(.2)


if __name__ == "__main__":
        opts, args = getopt.getopt(sys.argv[1:], "i:")
        interface=None
        try:
            if opts[0]:
                for opt, parm in opts:
                    if opt in ("-i"):
                        interface = parm
                        switcher()
        except:
            help()



