from socket import *
import struct
import binascii

#shows wanted SSIDs of nearby devices

IFACE = ""
PROBE_REQ = 4
PROBE_RESP = 5
ASOC_REQ = 0
ASOC_RESP = 1
FIXED_PARAMETERS = 12
FLAGS_END = 22

sniff = socket(AF_PACKET, SOCK_RAW, 3)
sniff.bind((IFACE, 0x0003))


def analyze(pktType, pkt, advset):
    dur, dMac, sMac, bssidMac = struct.unpack("!H6s6s6s", pkt[2:FLAGS_END])
    tagLenght = struct.unpack("!B", pkt[advset + 1])
    ssid = pkt[advset + 2:advset + 2 + tagLenght[0]]
    if pktType=="PREQ" and ssid:
        if binascii.hexlify(bssidMac)=="ffffffffffff":
            print "%s is looking for %s"%(binascii.hexlify(sMac),ssid)
            #todo show channel


while 1:
    pkt = sniff.recv(6000)[38:]
    type, ordr = struct.unpack("!BB", pkt[:2])
    type = type / 16
    if type == PROBE_RESP:
        advset = FLAGS_END + FIXED_PARAMETERS + 2  # seq number
        analyze("PRESP", pkt, advset)

    elif type == PROBE_REQ:
        advset = FLAGS_END + 2
        analyze("PREQ", pkt, advset)

    elif type == ASOC_REQ:
        advset = FLAGS_END + 2
        analyze("AREQ", pkt, advset)

    elif type == ASOC_RESP:
        advset = FLAGS_END + FIXED_PARAMETERS + 2
        analyze("ARESP", pkt, advset)
    #else:
        # print ':'.join(x.encode('hex') for x in pkt)
