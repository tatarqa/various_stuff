from socket import *
import struct
import itertools as itr
#import binascii

activeAps = []
IFACE = ""
PROBE_REQ = "40"#"\x40"
PROBE_RESP = "50"
ASOC_REQ = "0"
ASOC_RESP = "10"


sniff = socket(AF_PACKET, SOCK_RAW, 3)
sniff.bind((IFACE, 0x0003))

FIXED_PARAMETERS = 12
FLAGS_END = 22



def analyze(freq,pktType, pkt, advset):
    FREQUENCY_CURRENT = 2402
    FREQUENCY_WIDTH = 19
    FREQUENCY_HOP_1 = 5
    FREQUENCY_HOP_2 = 20

    dur, dMac, sMac, bssidMac = struct.unpack("!H6s6s6s", pkt[2:FLAGS_END])
    for channel in itr.chain(range(1, 14), range(36, 68, 4), range(100, 148, 4), range(149, 169, 4)):
        if channel != 1:
            if channel < 14:
                FREQUENCY_CURRENT = FREQUENCY_CURRENT + FREQUENCY_HOP_1
            else:
                FREQUENCY_CURRENT = FREQUENCY_CURRENT + FREQUENCY_HOP_2
                if channel == 149:
                    FREQUENCY_CURRENT += 5
                elif channel == 100:
                    FREQUENCY_CURRENT += 160
                elif channel == 36:
                    FREQUENCY_CURRENT += 2688
        if freq in range(FREQUENCY_CURRENT, FREQUENCY_CURRENT + FREQUENCY_WIDTH):
            foundChannel = channel
    print "=============================================\n" \
          "#%s#\nDEST. ADDR: %s\nSOURCE. ADDR: %s\nBSSID mac: %s" % \
          (pktType, dMac.encode('hex'), sMac.encode('hex'), bssidMac.encode('hex'))
    tagLenght = struct.unpack("!B", pkt[advset + 1])
    ssid = pkt[advset + 2:advset + 2 + tagLenght[0]]

    if pktType=="PREQ":
        if not ssid:
            ssid="broadcast"
        print "%s is looking for %s on channel %d"%(sMac.encode('hex'),ssid,foundChannel)

while 1:
    freq=struct.unpack("h", sniff.recv(100)[26:28])
    pkt = sniff.recv(1777)[38:]
    type=pkt[:1].encode('hex')
    if type == PROBE_RESP:
        advset = FLAGS_END + FIXED_PARAMETERS + 2  # seq number
        analyze(freq[0],"PRESP", pkt, advset)

    elif type == PROBE_REQ:
        advset = FLAGS_END + 2
        analyze(freq[0],"PREQ", pkt, advset)

    elif type == ASOC_REQ:
        advset = FLAGS_END + 2
        analyze(freq[0],"AREQ", pkt, advset)

    elif type == ASOC_RESP:
        advset = FLAGS_END + FIXED_PARAMETERS + 2
        analyze(freq[0],"ARESP", pkt, advset)
   # else:
        # print ':'.join(x.encode('hex') for x in pkt)
