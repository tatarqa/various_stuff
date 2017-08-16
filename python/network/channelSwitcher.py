#gnu/linux only
import os
import itertools as itr
import time
rootPw="xxx"
interface = 'xxx'

def suCmd(cmndo):
    os.popen("sudo -S %s" % (cmndo), 'w').write(rootPw)

while True:
    for channel in itr.chain(range(1, 13), range(36,60,4), range(100,144,4), range(149,165,4)):
        suCmd("iwconfig " + interface + " channel " + str(channel))
        print "[+] Switched to channel " + str(channel)
        time.sleep(5)