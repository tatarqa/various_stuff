import pickle
import datetime
import re
import os
import time

start_time = time.time()
slozkaNba = 'C:\\sprt\\nba\\'''
fIndex = 0
dataDict = {}
dataDictFixdDate = {}
datumS = ""
matchedKeys = {}
mayhem = {}
rest = ""
matchIndex = 0
zomh = ""
kleeeh = ""

dateRangeSource = {}
chcito = True
if chcito:
    jjj = open(slozkaNba + 'nakejprogres.html', 'w')
    jjj.write("<table>")
    for f in os.listdir(slozkaNba):
        if f.startswith("all"):
            fIndex = fIndex + 1
            pkl_file = open(slozkaNba + f, 'rb')
            data = pickle.load(pkl_file)
            dataDict = data
            pkl_file.close()
    prevdate = "2200-01-01"
    lowestDate = "2200-01-01"
    for k, v in dataDict.items():
        datetums = v[0]  # i.e february-8-2017
        date = datetime.datetime.strptime(datetums, "%B-%d-%Y").strftime('%Y-%d-%m')
        if (time.strptime(date, "%Y-%d-%m") < time.strptime(prevdate, "%Y-%d-%m") and time.strptime(date,
                                                                                                    "%Y-%d-%m") < time.strptime(
                lowestDate, "%Y-%d-%m")):
            lowestDate = date
        prevdate = date
    print(lowestDate)
    datesRslts = open(slozkaNba + "vsecko.pkl", 'rb')
    datesRsltsData = pickle.load(datesRslts)
    for k, v in datesRsltsData.items():
        rsltsKey = k
        rsltsTx = v
        for datum in re.finditer('@(.*?)@(.*)', v, re.S):
            datumS = datum.group(1)
            if time.strptime(datumS, "%Y-%d-%m") > time.strptime(lowestDate, "%Y-%d-%m"):
                for k, v in dataDict.items():
                    # print(datumS)
                    betorsKey = k[1]
                    betorsTx = v
                    datetums = v[0]
                    date = datetime.datetime.strptime(datetums, "%B-%d-%Y").strftime('%Y-%d-%m')
                    # print(date)
                    if datumS in date:
                        matchIndex = matchIndex + 1
                        zomh = rsltsKey + ":" + betorsKey
                        print("shoda" + zomh)
                        matchedKeys['espn:betos' + str(matchIndex) + ''] = zomh

                        kleeeh = "<tr><td>" + str(rsltsTx) + "</td>" + "<td>" + str(betorsTx) + "</td></tr>"
                        mayhem['datum', 'itm' + str(matchIndex)] = datumS, kleeeh
                        jjj.write(kleeeh)
                        break
    jjj.write("</table>")
    jjj.close()
    with open(slozkaNba + 'matchedKeys.pkl', 'wb') as handle:
        pickle.dump(matchedKeys, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open(slozkaNba + 'rsltsmtchdrld.pkl', 'wb') as handle:
        pickle.dump(mayhem, handle, protocol=pickle.HIGHEST_PROTOCOL)

finalNoway = open(slozkaNba + "rsltsmtchdrld.pkl", 'rb')
finalNowayD = pickle.load(finalNoway)
# ordered = OrderedDict(sorted(finalNowayD.items(), key=lambda t: t[0]))
nnn = open(slozkaNba + 'nakejprogres2.html', 'w')
nnn.write("<table><tbody>")

for uznevim in (sorted(finalNowayD.values(), key=lambda x: datetime.datetime.strptime(x[0], '%Y-%d-%m'))):
    uznevim = str(uznevim)
    for omnomn in re.finditer("\('\d\d\d\d-\d\d-\d\d'\,.'(.*)'\)", uznevim, re.S):
        print(omnomn.group(1))
        nnn.write(omnomn.group(1))
# for k, v in finalNowayD.items():
#	nnn.write(v)
nnn.write("</tbody></table>")
nnn.close()
print("--- %s seconds ---" % (time.time() - start_time))
