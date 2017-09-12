import threading
import mechanize
import cookielib
import Queue
from bs4 import BeautifulSoup
from urlparse import urlparse


# import dataset



def do_work(tgt):
    parsedLink = urlparse(tgt)
    domain = parsedLink.scheme + '://' + parsedLink.netloc
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
            else:
                parsedLink = urlparse(startLink)
                new_link_domain = parsedLink.scheme + '://' + parsedLink.netloc
                if not new_link_domain in checked_links and new_link_domain.endswith('.cz'):
                    links.append(new_link_domain)
                    domains.append(new_link_domain)

    if dd:
        print domain + ', JE DRUPAL'


def worker():
    while True:
        item = q.get()
        if not item in checked_links:
            do_work(item)
            q.task_done()

        else:
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

links.append(prefx + raw_input('>' + prefx + ""))

while 1:
    for item in links:
        if item not in checked_links:
            q.put(item)
