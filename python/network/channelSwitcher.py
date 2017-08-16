#gnu/linux only
import os
import itertools as itr
import time
import getopt
import sys

def help():
    print "[X] not enough parameters\n[*] -i for interface\n[*] -p for root password"
    sys.exit(0)
def suCmd(cmndo):
    os.popen("sudo -S %s" % (cmndo), 'w').write(rootPw)

def switcher():
    while True:
        for channel in itr.chain(range(1, 13), range(36,60,4), range(100,144,4), range(149,165,4)):
            suCmd("iwconfig " + interface + " channel " + str(channel))
            print "[+] Switched to channel " + str(channel)
            time.sleep(5)


if __name__ == "__main__":
        opts, args = getopt.getopt(sys.argv[1:], "p:i:")
        interface=None
        rootPw=None
        try:
            if opts[0] and opts[1]:
                for opt, parm in opts:
                    if opt in ("-p"):
                        rootPw = parm
                    elif opt in ("-i"):
                        interface = parm
                    if rootPw and interface:
                        switcher()
        except:
            help()



