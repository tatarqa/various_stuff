import mechanize
import cookielib
from bs4 import BeautifulSoup
from python.network.hyper import HTTPConnection


lajnasss=[]
blumba = open("dnd.xls", 'a')
def ano(qst):
    print qst
    if qst==True:
        return 'ANO'
    else:
        return ' '

with open('drupals.txt','r') as file:
    for lajna in file.readlines():
        userAgent = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1')]
        proxz = {}
        output = ""
        https=False
        http2=False
        drupal_version=''
        if not lajna in lajnasss:
            lajnasss.append(lajna)
            try:
                conn = HTTPConnection('www.'+lajna.strip( '\n' )+':443')
                if conn:
                    conn.request('GET', '/get')
                    resp = conn.get_response()
                    print type(resp)
                    if 'http20' in str(type(resp)):
                        https=http2=True
                    else:
                        https = True
            except:
                pass
            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.set_handle_equiv(True)
            browser.set_handle_referer(True)
            browser.set_handle_redirect(True)
            browser.addheaders = userAgent
            # browser.set_proxies(proxz)
            cookie_jar = cookielib.LWPCookieJar()
            browser.set_cookiejar(cookie_jar)
            try:
                page = browser.open("http://www."+lajna)
            except:
                continue
            if 'Drupal 8 (https://www.drupal.org)' in page._headers.dict.viewvalues():
                drupal_version='8'
            elif 'Drupal 7 (http://drupal.org)' in page._headers.dict.viewvalues():
                drupal_version = '7'
            elif 'Drupal 6 (http://drupal.org)' in page._headers.dict.viewvalues():
                drupal_version = '6'
            else:
                drupal_version = ' '
            # domain;version;owner;created by;https;http2;cdn;hosted by
            output+='<tr><td>'+lajna+'</td><td>'+drupal_version+'</td><td></td><td></td><td>'+ano(https)+'</td><td>'+ano(http2)+'</td><td></td><td></td></tr>'
            print output
            try:
                blumba.write(output)
            except:
                print 'neco went wrong'

blumba.close()
