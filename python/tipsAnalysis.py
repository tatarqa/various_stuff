import time
import re
import io
import datetime
import pickle


def separo(f, linesep):
    dts = ""
    while True:
        while linesep in dts:
            pos = dts.index(linesep)
            yield dts[:pos]
            dts = dts[pos + len(linesep):]
        cec = f.read()
        if not cec:
            yield dts
            break
        dts += cec


trimd6F = open('trimd6.html', 'w')
trimd6CSV = open('trimd6CSV.html', 'w')
with open('source.html', 'r') as f:
    data = {}
    data2 = {}
    data4 = {}
    data5 = {}

    date = {}
    betor = {}
    typy = {}
    komplet = ""
    kompletDict = {}
    rowIndex = 0
    tyypyList = ""

    trimd6F.write("<table><tbody>")
    for line in separo(f, "@"):
        for heda in re.finditer(
                '###########https://forum.thespread.com/basketball-discussion/(.*?)-free-picks-free-premium-service-plays-for-(.*)###########',
                line, re.S):
            data4 = ''.join(map(str, heda.group(2)))
            data4 = re.sub('\?start=25$', '', data4)
            if not (data4.endswith("2016") or data4.endswith("2017")):
                data4 = data4 + "-2016"
            data5 = ''.join(map(str, data4))
            print(data4)
            hlavaM = re.match('(.*?)-(.*?)-(.*?)(th-|st-|nd-|rd-|-)(.*?)$', data5)
            data5 = hlavaM.group(2) + "-" + hlavaM.group(3) + "-" + hlavaM.group(5)
        for match in re.finditer('<div class="kmsgtext">(.*?)</div>', line, re.S):
            rowIndex = rowIndex + 1
            cleanr = re.compile('\s*$<br/>')
            nobr = re.sub(cleanr, '', match.group())
            trimd6F.write("<tr>")
            data = ''.join(map(str, nobr))
            for match3 in re.finditer('<b>(.*?)</b>(.*)</div>', data, re.S):
                trimd6F.write("<td class='time'>" + data5 + "</td>")
                komplet = data5
                date['item' + str(rowIndex) + ''] = data5

                trimd6F.write("<td class='tiper'>" + match3.group(1) + "</td>")
                betor['item' + str(rowIndex) + ''] = match3.group(1)
                komplet = komplet + "@" + match3.group(1)
                trimd6CSV.write(data5 + ",")
                trimd6CSV.write(match3.group(1) + ",")
                data2 = ''.join(map(str, match3.group(2)))
                buf = io.StringIO(data2)
                for line in (line for line in buf if not line.startswith(' <')):
                    if line == '\n':
                        print("prazdno")
                    else:
                        trimd6F.write("<td class='typy'>" + line + "</td>")
                        trimd6CSV.write(line + ",")
                        komplet = komplet + "," + line
                        tyypyList = tyypyList + "," + line
                        print("<td class='typy'>" + line + "</td>")
                kompletDict['item' + str(rowIndex) + ''] = komplet
            if tyypyList:
                typy['item' + str(rowIndex) + ''] = tyypyList
                tyypyList = ""
            trimd6F.write("</tr>")
    trimd6F.write("</tbody></table>")
with open('date.pkl', 'wb') as handle:
    pickle.dump(date, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('all.pkl', 'wb') as handle:
    pickle.dump(kompletDict, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('betor.pkl', 'wb') as handle:
    pickle.dump(betor, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('typy.pkl', 'wb') as handle:
    pickle.dump(typy, handle, protocol=pickle.HIGHEST_PROTOCOL)

trimd6F.close()
trimd6CSV.close()


def separo(f, linesep):
    dts = ""
    while True:
        while linesep in dts:
            pos = dts.index(linesep)
            yield dts[:pos]
            dts = dts[pos + len(linesep):]
        cec = f.read()
        if not cec:
            yield dts
            break
        dts += cec


def is_odd(a):
    return bool(a - ((a >> 1) << 1))


trimd6F = open('done.html', 'w')
trimd6csv = open('done.csv', 'w')
with open('espnNBA1.html', 'r') as f:
    awayStr = {}
    homeStr = {}
    awayScore = {}
    rowIndex = 0
    tRurowIndex = 0
    matchDatesDict = {}
    homeTeamDict = {}
    awayTeamDict = {}
    winnerDict = {}
    skorecelkem = {}
    skorecelkemI = 0

    helper1 = {}
    helper2 = {}
    helper3 = {}
    helper4 = {}

    totalka = {}
    helper3.clear()
    awayB = True
    homeB = False
    longer = ""
    longerDict = {}
    vseckyDataStr = ""
    vseckyData = {}
    start_time = time.time()
    trimd6F.write("<table><tbody>")
    for line in separo(f, "@"):
        if re.match('<\/div><div>http:\/\/www.espn.com\/nba\/scoreboard\/_\/date\/(\d+)<\/div>\[<section', line):
            totalka = ''.join(map(str, line))
            for datum in re.finditer(
                    '<\/div><div>http:\/\/www.espn.com\/nba\/scoreboard\/_\/date\/(\d+)<\/div>\[<section', line, re.S):
                helper4 = ''.join(map(str, datum.group(1)))
                helper4 = datetime.datetime.strptime(helper4, "%Y%m%d")
                helper4 = helper4.strftime('%Y-%d-%m')
                longer = longer + helper4 + "@"
                rowIndex = rowIndex + 1
                matchDatesDict['item' + str(rowIndex) + ''] = helper4
            cDb = 0
            for homawhomeSc in re.finditer('<tr class="away">(?P<away>.*?)</tr>|<tr class="home">(?P<home>.*?)</tr>',
                                           line, re.S):
                cDb = cDb + 1
                if is_odd(cDb):
                    awayB = True
                    homeB = False
                else:
                    awayB = False
                    homeB = True

                if awayB is True:
                    awayStr = ''.join(map(str, homawhomeSc.group(1)))
                    trimd6F.write("<tr>")
                if homeB is True:
                    homeStr = ''.join(map(str, homawhomeSc.group(2)))

                trimd6F.write("<td class='datum'>" + helper4 + "</td>")
                trimd6csv.write(helper4 + ",")
                vseckyDataStr = vseckyDataStr + "@" + helper4
                if homeStr:
                    for homeTnm in re.finditer('<span class="sb-team-short">(.*?)</span>', homeStr):
                        homeTeam = homeTnm.group(1)
                        trimd6F.write("<td class='domaci'>" + homeTeam + "</td>")
                        homeTeamDict['item' + str(rowIndex) + ''] = homeTeam
                        trimd6csv.write(homeTeam + ",")
                    b = 0
                    for homeSc in re.finditer('<td class="score">(.*?)</td>', homeStr, re.S):
                        b = b + 1
                        trimd6F.write("<td class='domaciSkoreQ" + str(b) + "'>" + homeSc.group(1) + "</td>")
                        trimd6csv.write(homeSc.group(1) + ",")
                    if b == 4:
                        trimd6F.write("<td class=\"domaciSkoreQ5\">-</td>")
                        trimd6csv.write("-,")
                    b = 0
                    for homTt in re.finditer('<td class="total"><span>(.*?)</span>', homeStr):
                        homeScoreT = homTt.group(1)
                        trimd6F.write("<td class='domaciSkoreT" + str(b) + "'>" + homeScoreT + "</td>")
                        trimd6csv.write(homeScoreT + ",")
                        vseckyDataStr = vseckyDataStr + "@" + homeScoreT
                        # XXXXXXX
                homeStr = None

                if awayStr:
                    for awayTnm in re.finditer('<span class="sb-team-short">(.*?)</span>', awayStr):
                        awayTeam = awayTnm.group(1)
                        trimd6F.write("<td class='hoste'>" + awayTeam + "</td>")
                        trimd6csv.write(awayTeam + ",")
                        awayTeamDict['item' + str(rowIndex) + ''] = awayTeam
                    b = 0
                    for awaSc in re.finditer('<td class="score">(.*?)</td>', awayStr, re.S):
                        b = b + 1
                        trimd6F.write("<td class='hosteSkoreQ" + str(b) + "'>" + awaSc.group(1) + "</td>")
                        trimd6csv.write(awaSc.group(1) + ",")
                    if b == 4:
                        trimd6F.write("<td class=\"hosteSkoreQ5\">-</td>")
                        trimd6csv.write("-,")
                    b = 0
                    for awaTt in re.finditer('<td class="total"><span>(.*?)</span>', awayStr):
                        awaScoreT = awaTt.group(1)
                        trimd6F.write("<td class='hosteSkoreT" + str(b) + "'>" + awaScoreT + "</td>")
                        trimd6csv.write(awaScoreT + ",")
                        vseckyDataStr = vseckyDataStr + "@" + awaScoreT

                awayStr = None

                if awayB is True:
                    awayB = False
                if homeB is True:
                    if int(awaScoreT) > int(homeScoreT):
                        winnerDict['item' + str(rowIndex) + ''] = awayTeam
                        winnerStr = awayTeam
                    else:
                        winnerDict['item' + str(rowIndex) + ''] = homeTeam
                        winnerStr = homeTeam
                    skorecelkemI = int(awaScoreT) + int(homeScoreT)
                    skorecelkem['item' + str(rowIndex) + ''] = skorecelkemI
                    trimd6F.write("<td class='winner'>" + winnerStr + "</td>")
                    trimd6F.write("<td class='totalScore'>" + str(skorecelkemI) + "</td>")
                    trimd6F.write("</tr>")
                    trimd6csv.write(winnerStr + ",")
                    trimd6csv.write(str(skorecelkemI))
                    longer = longer + winnerStr
                    longerDict['item' + str(rowIndex) + ''] = longer
                    trimd6csv.write("\n")
                    vseckyDataStr = vseckyDataStr + "@" + winnerStr + "@" + str(skorecelkemI) + "\n"
                    tRurowIndex = tRurowIndex + 1
                    vseckyData['item' + str(tRurowIndex) + ''] = vseckyDataStr
                    longer = ""
                    vseckyDataStr = ""
                    homeB = False

    trimd6F.write("</tbody></table>")
trimd6F.close()
trimd6csv.close()

with open('results.pkl', 'wb') as handle:
    pickle.dump(longerDict, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('vsecko.pkl', 'wb') as handle:
    pickle.dump(vseckyData, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('matchDatesDict.pkl', 'wb') as handle:
    pickle.dump(matchDatesDict, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('homeTeamDict.pkl', 'wb') as handle:
    pickle.dump(homeTeamDict, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('awayTeamDict.pkl', 'wb') as handle:
    pickle.dump(awayTeamDict, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('winnerDict.pkl', 'wb') as handle:
    pickle.dump(winnerDict, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("--- %s seconds ---" % (time.time() - start_time))
# dates = [ datetime.datetime(2007, 1, 2, 0, 1),
#		datetime.datetime(2007, 1, 3, 0, 2),
#		datetime.datetime(2007, 1, 4, 0, 3),
#		datetime.datetime(2007, 1, 5, 0, 4),
#		datetime.datetime(2007, 1, 6, 0, 5),
#		datetime.datetime(2007, 1, 7, 0, 6) ]


# within = [date for date in dates if datetime.datetime(2007,1,3) < date < datetime.datetime(2007,1,6)]
# print(within)