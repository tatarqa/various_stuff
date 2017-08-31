#http://3564020356.org/ chall 1

scope=[]
full=[]
with open('1.txt', 'rb') as tx:
    for line in tx.readlines():
        for byte in line:
            byteHx = byte.encode("hex")
            full.append(byteHx)
            if byteHx not in scope:
                scope.append(byteHx)

    for itm in scope:
        print '[*]:%s (%s) %dx' % (itm, itm.decode("hex").encode("utf8"), full.count(itm))
print "##########################"


with open('0c.bmp', 'rb') as img:
    data = img.read()
    print data
    for byte in data:
        byteHx=byte.encode("hex")
        full.append(byteHx)
        if byteHx not in scope:
            scope.append(byteHx)

for itm in scope:
    print '[*]:%s %dx' % (itm, full.count(itm))

