from socket import *
import struct
import itertools as itr

# import binascii

initVectors = []
IFACE = raw_input('!! >> type interface in monitor mode --> ')
PROBE_REQ = "40"  # "\x40"
PROBE_RESP = "50"
ASOC_REQ = "00"
ASOC_RESP = "10"
BEACON="80"
EAPOL="88"

HEADERLEN1=38
HEADERLEN2=44



sniff = socket(AF_PACKET, SOCK_RAW, 3)
sniff.bind((IFACE, 0x0003))

FIXED_PARAMETERS = 12
FIXED_PARAMETERS_ARESP = 6
FIXED_PARAMETERS_AREQ=4
FLAGS_END = 61-38-1
KEYPARAMS=21

def analyze(freq, pktType, pkt, advset):
    frequency_current = 2402
    FREQUENCY_WIDTH = 19#its 20 actually
    #http://niviuk.free.fr/wifi_band.php
    FREQUENCY_HOP_1 = 5
    FREQUENCY_HOP_2 = 20

    dur, dMac, sMac, bssidMac = struct.unpack("!H6s6s6s", pkt[2:FLAGS_END])
    for channel in itr.chain(range(1, 14), range(36, 68, 4), range(100, 148, 4), range(149, 169, 4)):
        if channel != 1:
            if channel < 14:
                frequency_current = frequency_current + FREQUENCY_HOP_1
            else:
                frequency_current = frequency_current + FREQUENCY_HOP_2
                if channel == 149:
                    frequency_current += 5
                elif channel == 100:
                    frequency_current += 160
                elif channel == 36:
                    frequency_current += 2688
        if freq in range(frequency_current, frequency_current + FREQUENCY_WIDTH):
            foundChannel = channel
            break
    print "=============================================\n" \
          "#%s#\nDEST. ADDR: %s\nSOURCE. ADDR: %s\nBSSID mac: %s" % \
          (pktType, dMac.encode('hex'), sMac.encode('hex'), bssidMac.encode('hex'))

    if pktType != "EAPOL":
        tagLenght = struct.unpack("!B", pkt[advset + 1])
        ssid = pkt[advset + 2:advset + 2 + tagLenght[0]]

        if pktType == "PREQ":
            if not ssid:
                ssid = "broadcast"
            print "%s is looking for %s on channel %d" % (sMac.encode('hex'), ssid, foundChannel)
    else:
        kbody = pkt[FLAGS_END:FLAGS_END + KEYPARAMS]
        print "key lenght %d"%int(kbody[-2:].encode('hex'), 16)




while 1:
    pkt = sniff.recv(800)[0:]
    hLenght = struct.unpack("h", pkt[2:4])[0]
    if hLenght==HEADERLEN1:
        freq = struct.unpack("h", pkt[26:28])[0]
    elif hLenght==HEADERLEN2:
        freq = struct.unpack("h", pkt[18:20])[0]
    pkt = pkt[hLenght:]
    type = pkt[:1].encode('hex')
    if type == PROBE_RESP:
        advset = FLAGS_END + FIXED_PARAMETERS + 2  # seq number
        analyze(freq, "PRESP", pkt, advset)

    elif type == PROBE_REQ:
        advset = FLAGS_END + 2
        analyze(freq, "PREQ", pkt, advset)

    elif type == ASOC_REQ:
        advset = FLAGS_END+FIXED_PARAMETERS_AREQ + 2
        analyze(freq, "AREQ", pkt, advset)

    elif type == ASOC_RESP:
        advset = FLAGS_END + FIXED_PARAMETERS_ARESP + 2
        analyze(freq, "ARESP", pkt, advset)
    elif type == EAPOL:
        advset = ""
        analyze(freq, "EAPOL", pkt, advset)
    elif type==BEACON:
        continue
    #else:
     #   print str(type)
