from socket import *
import sys
import threading

WORKERS = 50
PORT_MAX = 1000
RAT = PORT_MAX / WORKERS
tgt = raw_input("--> ")
tgtIP = gethostbyname(tgt)


def probe(w):
    try:
        for port in range(RAT * w - RAT, RAT * w):
            s = socket(AF_INET, SOCK_STREAM)
            s.settimeout(10)
            r = s.connect_ex((tgtIP, port))
            if r == 0:
                print str(port) + " is ok"
    except:
        print "something went wrong"


for i in range(1, WORKERS + 1):
    t = threading.Thread(target=probe, args=(i,))
    t.start()
