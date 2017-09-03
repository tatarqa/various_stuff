import mechanize
import cookielib
from bs4 import BeautifulSoup
import threading


def gatherLinks(tgt):
    print tgt
    final_link = ""
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
    try:

        page = browser.open(tgt)
        parsed_page = BeautifulSoup(page, 'html.parser')
        for anchor in parsed_page.find_all('a'):
            startLink = anchor.get('href')
            try:
                if startLink[:4] == "http":
                    final_link = startLink
                elif startLink[:1] == "/":
                    final_link = tgt + startLink
                if not final_link in links and not final_link in checked_links:
                    links.append(final_link)
                links.remove(tgt)
            except:
                continue
    except:
        to = do = 'w'

    checked_links.append(tgt)


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
checked_links = []
links.append(prefx + raw_input('>' + prefx + ""))
while len(links):
    for link in links:
        t = threading.Thread(target=gatherLinks, args=(link,))
        t.start()
    t.join()
