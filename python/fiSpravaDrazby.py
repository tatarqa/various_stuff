import re
import pickle
from urllib.request import urlopen
import urllib.request, urllib.error
from bs4 import BeautifulSoup


def reader(idson, dict):
	dictName=dict
	dict={}
	bPager=1
	basePath = "http://www.financnisprava.cz/cs/financni-sprava/drazby-financnich-uradu?page="+str(bPager)+"&stav="+str(idson)+"&druh=&urad=&from=&to=&minprice=&maxprice="
	bPager=0
	auctionIndex=0
	auctionIndexId={}
	fileIndex=0


	htmlO = urlopen(basePath).read().decode('utf-8')
	htmlP = BeautifulSoup(htmlO, 'html.parser')
	print("####"+str(basePath)+"####")
	for mainIndex in htmlP.find_all('ul', {'class': 'archive-years pageList multiline'}):
		for li in mainIndex.findAll('li'):
			bPager=bPager+1
			pagedPath = "http://www.financnisprava.cz/cs/financni-sprava/drazby-financnich-uradu?page="+str(bPager)+"&stav="+str(idson)+"&druh=&urad=&from=&to=&minprice=&maxprice="
			print(pagedPath)
			pagedHtmlO = urlopen(pagedPath).read().decode('utf-8')
			pagedHtmlP = BeautifulSoup(pagedHtmlO, 'html.parser')
			for a in pagedHtmlP.find_all("a", text=re.compile('(.)zemn(.) pracovi(.)t(.) (v|pro)(.*)')):
				detailLink = a['href']
				print(detailLink)
				for aucId in re.finditer('http:\/\/www\.financnisprava\.cz\/cs\/financni\-sprava\/drazby\-financnich\-uradu\/app\/detail\/(.*)', detailLink):
					aucId=aucId.group(1)
					auctionIndex=auctionIndex+1
					auctionIndexId['aukceIndex'+str(auctionIndex)] = aucId
					dict['aukce'+str(aucId)] = detailLink
				detailHtmlO = urlopen(detailLink).read().decode('utf-8')
				detailHtmlP = BeautifulSoup(detailHtmlO, 'html.parser')
				for a in detailHtmlP.find_all("a", href=re.compile('(.*).pdf(.*)')):
					fileIndex=fileIndex+1
					pdflink= a['href']
					try:
						conn = urllib.request.urlopen(pdflink)
					except urllib.error.HTTPError as e:
						print(e.code)
						pdflink="http://iwg-gti.org/common_up/iwg-new/document_1481208108.pdf"
					except urllib.error.URLError as e:
						print('URLError')
						pdflink="http://iwg-gti.org/common_up/iwg-new/document_1481208108.pdf"
					else:
						print('good')
					pdfO = urlopen(pdflink)
					k='aukceIndex'+str(auctionIndex)
					if auctionIndexId.get(k):
						auId= auctionIndexId.get(k)
					print(auId)
					if pdflink=="http://iwg-gti.org/common_up/iwg-new/document_1481208108.pdf":
						if fileIndex>1:
							pdfko = open('C:\\aukce\\6test\\''404_'+auId+'_'+str(fileIndex)+'.pdf', 'wb')
						else:
							pdfko = open('C:\\aukce\\6test\\''404_'+auId+'.pdf', 'wb')
					else:
						if fileIndex>1:
							pdfko = open('C:\\aukce\\6test\\'''+dictName+auId+'_'+str(fileIndex)+'.pdf', 'wb')
						else:
							pdfko = open('C:\\aukce\\6test\\'''+dictName+auId+'_.pdf', 'wb')
					fileIndex=0
					pdfko.write(pdfO.read())
					pdfko.close()
	with open(dictName+'.pkl', 'wb') as handle:
		pickle.dump(dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

def runit():
	reader(1,"aktualni")
	reader(3,"archiv")

runit()
