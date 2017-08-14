import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

comLinky=[]
skipito=0
basePath = "http://marvel.com"
comicsPath = "/comics/series"
htmlO = urlopen(basePath+comicsPath).read().decode('utf-8')
htmlP = BeautifulSoup(htmlO, 'html.parser')
cntnt = htmlP.find('section', {'class': 'module moduColor_Light modu_AZ'})
with open("out.txt", 'w') as fin:
	for mainIndex in cntnt.find_all('div', {'class': 'JCAZList-list'}):
		for uls in cntnt.find_all('ul'):
				for li in uls.findAll('li'):
					for a in li.findAll('a'):
						linka=(a['href'])
						title=(a.text)
						comLinky.append((title,linka))
						detailIdMatch = re.match('/comics/series/(.*?)/', linka)
						if detailIdMatch:
							detailId=detailIdMatch.groups(0)
						try:
							detailOpener=urlopen(basePath+linka).read().decode('utf-8')
							detailParse=BeautifulSoup(detailOpener, 'html.parser')
							resultsSumNumberCont = detailParse.find('div', {'class': 'filterTabHeadItems filterResultsText'})
							if resultsSumNumberCont:
								resultsSumNumberMatch = re.match(r'Showing 10 of (\d*)', resultsSumNumberCont.text.strip())
								if resultsSumNumberMatch:
									resultsSumNumber=resultsSumNumberMatch.groups(0)
									print ("[*] ID:%s "%(detailId) +'rich link')
									fin.write("[*] ID:%s "%(detailId) + basePath+linka+"?byZone=marvel_site_zone&offset=0&byType=comic_series&dateStart=&dateEnd=&type=&orderBy=release_date+desc&byId=%s&limit=8&count=10&totalcount=%s" % (int(detailId[0]), int(resultsSumNumber[0]))+'\n')
								else:
									print ("[*] ID:%s solo link"%(detailId))
									fin.write("[*] ID:%s "%(detailId)+ basePath+linka+'\n')
						except:
							print ("[*] ID:%s vadnej link"%(detailId))
							continue
fin.close()