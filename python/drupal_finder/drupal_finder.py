import threading
import mechanize
import cookielib
import Queue
from bs4 import BeautifulSoup
from urlparse import urlparse


# import dataset

def urlparser(url):
    parsedLink = urlparse(url)
    netloc = parsedLink.netloc
    if netloc.startswith('www'):
        netloc = netloc[4:]
    return parsedLink.scheme, '://', netloc


def do_work(tgt, choice2):
    domain = urlparser(tgt)[2]
    checked_links.append(domain)
    dd = False
    userAgent = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1')]
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.set_handle_equiv(True)
    browser.set_handle_referer(True)
    browser.set_handle_redirect(True)
    browser.addheaders = userAgent
    cookie_jar = cookielib.LWPCookieJar()
    browser.set_cookiejar(cookie_jar)
    try:
        page = browser.open(tgt)
        parsed_page = BeautifulSoup(page, 'html.parser')
    except:
        return
    if 'Sun, 19 Nov 1978 05:00:00 GMT' in page._headers.dict.viewvalues():
        if domain not in drupal_sites:
            drupal_sites.append(domain)
            dd = True
    for anchor in parsed_page.find_all('a'):
        startLink = anchor.get('href')
        if startLink:
            if startLink[:4] != "http":
                continue
            parsedLink = urlparser(startLink)
            new_link_domain = parsedLink[2]
            new_link = ''.join(parsedLink)
            if choice2 is not '':
                if choice2.startswith('.'):
                    choice2=choice2[1:]
                if not new_link_domain in checked_links and new_link_domain.endswith(choice2):
                    links.append(new_link)
                    domains.append(new_link_domain)
            else:
                if not new_link_domain in checked_links:
                    links.append(new_link)
                    domains.append(new_link_domain)
    if dd:
        print domain + ' DRUPAL'


def worker():
    while True:
        item = q.get()
        domain = urlparser(item)[2]
        if not domain in checked_links:
            do_work(item, choice2)
        q.task_done()


q = Queue.Queue()
links = []
domains = []
drupal_sites = []
checked_links = []
for i in range(666):
    # db = dataset.connect('sqlite:///domeny.db')
    # domains_table = db['all_domains']
    t = threading.Thread(target=worker, args=())
    t.daemon = True
    t.start()
print "[-] enter 1 for http, enter 2 for https: "
choice = raw_input("[>] ")
while 1:
    if choice == '1':
        prefx = 'http://'
        break
    elif choice == '2':
        prefx = 'https://'
        break
    else:
        print "[-] enter 1 for http webpage, enter 2 for https: "
        choice = raw_input("[>] ")
print "\n[-] enter domain name e.g. %sgoogle.com" % prefx
links.append(prefx + raw_input('[>] ' + prefx + ""))
print "[-] limit top level domains? enter top level domain e.g. ru\n[-] Leave blank for no filtering."
choice2 = raw_input("[>] ")
print '[+] OK'
while 1:
    for item in links:
        domain = urlparser(item)[2]
        if domain not in checked_links:
            q.put(item)
