import mechanize
import cookielib
from bs4 import BeautifulSoup
import threading
from urlparse import urlparse
import sys
import Queue
import time


def clear(itm):
    try:
        links.remove(itm)
    except:
        n = i = c = 1
    checked_links.append(itm)


def gatherLinks(tgt):
    userAgent = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1')]
    proxz = {}
    final_link = ""
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
        page = browser.open(tgt)
    except:
        clear(tgt)
        return
    if 'Sun, 19 Nov 1978 05:00:00 GMT' in page._headers.dict.viewvalues():
        unknown_domain_format = urlparse(tgt).netloc
        if unknown_domain_format.startswith('www.'):
            known_domain = unknown_domain_format[4:]
        else:
            known_domain = unknown_domain_format
        if known_domain not in drupal_sites:
            drupal_sites.append(known_domain)
            dumba = open("drupal_domains.txt", 'a')
            dumba.write(str(time.time() - start_time)+' '+known_domain.decode('utf-8', 'ignore') + '\n')
            dumba.close()
    parsed_page = BeautifulSoup(page, 'html.parser')
    for anchor in parsed_page.find_all('a'):
        startLink = anchor.get('href')
        if startLink:
            if startLink[:4] == "http":
                final_link = startLink
            elif startLink[:1] == "/":
                final_link = tgt + startLink
            parsedLink = urlparse(final_link)
            domain = parsedLink.netloc
            if not final_link in links and not final_link in checked_links and not domain in domains:
                links.append(final_link)
                domains.append(domain)
                blumba = open("domains.txt", 'a')
                blumba.write(domain.decode('utf-8', 'ignore') + '\n')
                blumba.close()
    clear(tgt)


def threadDist(q, tgt):
    q.put(gatherLinks(tgt))


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
links = []
domains = []
drupal_sites = []
checked_links = []
threads = []
links.append(prefx + raw_input('>' + prefx + ""))
start_time = time.time()
q = Queue.Queue()
while len(links):
    print str(len(threads))
    for link in links:
        t = threading.Thread(target=threadDist, args=(q, link))
        threads.append(t)
        t.start()

