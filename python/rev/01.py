#http://3564020356.org/ 
txt1="MAL TIRRUEZF CR MAL RKZYIOL EX MAL OIY UAE RICF MAL ACWALRM DYEUPLFWL CR ME DYEU MAIM UL IZL RKZZEKYFLF GH OHRMLZH"
knoiwnSHit={"a":"h","m":"t","l":"e","c":"i","r":"s","w":"g","i":"a","f":"d","k":"u","z":"r","e":"o","y":"n","t":"p","u":"w","o":"m","x":"f","d":"k","p":"l",}
rslt=""
modedChar="*"
found=False

for char in txt1.lower():
    for k,v in knoiwnSHit.iteritems():
        if found is False:
            if char==" ":
                modedChar=" "
            if char==k:
                found=True
                modedChar=v
    found = False
    rslt += modedChar
    modedChar = "*"
print rslt
print txt1