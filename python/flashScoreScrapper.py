from selenium import webdriver
import time

chromedriver = "C:\compo"
f = open('flash3.html', 'w')
driver = webdriver.Chrome()
url = "http://www.flashscore.com"
zoznam = ['/basketball/usa/ncaa/results/', '/basketball/usa/nba/results/', '/nhl/results/']
driver.implicitly_wait(10)
for sport in zoznam:
    url2 = url + sport
    driver.get(url2)
    f.write(str(driver.find_element_by_class_name("stage-finished")))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    for x in range(1, 25):
        driver.find_element_by_xpath('//*[@id="tournament-page-results-more"]/tbody/tr/td/a').click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print (driver.find_element_by_xpath('//*[@id="fs-results"]/table/tbody'))
    time.sleep(20)
driver.close()
f.close()
