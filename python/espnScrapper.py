from bs4 import BeautifulSoup
import time
from random import randint
from selenium import webdriver
from datetime import timedelta, date


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


start_date = date(1992, 1, 1)
end_date = date(2017, 3, 12)

f = open('espnNBA.html', 'w')
for single_date in daterange(start_date, end_date):
    basePath = "http://www.espn.com/nba/scoreboard/_/date/" + single_date.strftime("%Y%m%d")
    time.sleep(randint(1, 3))
    browser = webdriver.PhantomJS(executable_path=r'C:\compo\phantomjs\bin\phantomjs.exe')
    browser.get(basePath)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    soup.prettify()
    igry = soup.find_all('section', {'class': 'sb-score'})
    print(basePath)
    f.write("<div>" + basePath + "</div>")
    f.write(str(igry))
    f.write(
        "<div>###############################################################################################################</div>")
    browser.refresh()
    browser.quit()
f.close()
