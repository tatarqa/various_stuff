import mechanize
import cookielib
from socket import *
from bs4 import BeautifulSoup


def gatherLinks(tgt):
    print tgt
    final_link = ""
    links = []
    userAgent = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1')]
    proxz = {}
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.set_handle_equiv(True)
    browser.set_handle_referer(True)
    browser.set_handle_redirect(True)
    browser.addheaders = userAgent
    # browser.set_proxies(proxz)
    cookie_jar = cookielib.LWPCookieJar()
    browser.set_cookiejar(cookie_jar)
    page = browser.open(tgt)
    parsed_page = BeautifulSoup(page, 'html.parser')
    for anchor in parsed_page.find_all('a'):
        startLink = anchor.get('href')
        if startLink[:4] == "http":
            final_link = startLink
        elif startLink[:1] == "/":
            final_link = tgt + startLink
        if not final_link in links:
            links.append(final_link)
    print links


print "[-] enter 1 for http, enter 2 for https: "
choice = raw_input(">")
while 1:
    if choice == '1':
        prefx = 'http://www.'
        break
    elif choice == '2':
        prefx = 'https://www.'
        break
    else:
        print "[-] enter 1 for http webpage, enter 2 for https: "
        choice = raw_input(">")
print "\n[-] enter domain name e.g. %sgoogle.com" % prefx
target = prefx + raw_input('>' + prefx + "")

gatherLinks(target)
