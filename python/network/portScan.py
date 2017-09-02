from socket import *
import sys
import threading
import time



WORKERS = 50
PORT_MAX = 1000
RAT = PORT_MAX / WORKERS
tgt = raw_input("--> ")
print "e.g. need.weed.global"
tgtIP = gethostbyname(tgt)
start_time = time.time()

def probe(w):
    try:
        for port in range(RAT * w - RAT, RAT * w):
            s = socket(AF_INET, SOCK_STREAM)
            s.settimeout(1)
            r = s.connect_ex((tgtIP, port))
            if r == 0:
                print str(port) + " is ok"
    except:
        print "something went wrong"


threads = []
for i in range(1, WORKERS + 1):
    t = threading.Thread(target=probe, args=(i,))
    threads.append(t)
    t.start()

for x in threads:
    x.join()
print("--- %s seconds ---" % (time.time() - start_time))
