import mechanize
import cookielib
from bs4 import BeautifulSoup
from socket import *


def getInfo(ipaddr, userAgent, proxz, hostname):
    WEBFORM_NAME = 'search'
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.set_handle_equiv(True)
    browser.set_handle_referer(True)
    browser.set_handle_redirect(True)
    browser.addheaders = userAgent
    # browser.set_proxies(proxz)
    cookie_jar = cookielib.LWPCookieJar()
    browser.set_cookiejar(cookie_jar)
    page = browser.open('https://apps.db.ripe.net/search/query.html')
    for form in browser.forms():
        if form.name == WEBFORM_NAME:
            browser.select_form(WEBFORM_NAME)
            browser.form['search:queryString'] = ipaddr
            browser.form['search:sources'][0] = 'GRS'
            submission = browser.submit().read()
            parsed_submission = BeautifulSoup(submission, 'html.parser')
            print ipaddr, '/',hostname
            for mainIndex in parsed_submission.find_all('ul', {'class': 'attrblock'}):
                for i, li in enumerate(mainIndex.findAll('li')):
                    if i in range(0, 2):
                        print '[+] ', li.text
            print '\n ########## \n'


import struct
import os

# os.popen("sudo ifconfig eth0 promisc")
userAgent = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1')]
proxz = {}
source_ips = []
s = socket(PF_PACKET, SOCK_RAW, ntohs(0x0800))
while 1:
    pkt = s.recvfrom(2048)
    eth_head = pkt[0][:14]
    ip_head = pkt[0][14:34]
    tcp_head = pkt[0][34:54]
    dest_mac, source_mac, seq_number = struct.unpack("!6s6s2s", eth_head)
    neco, source_ip, dest_ip = struct.unpack("!12s4s4s", ip_head)
    source_port, dest_port, neco2, flag, neco3 = struct.unpack("!HH9ss6s", tcp_head)
    source_ip = inet_ntoa(source_ip)
    if not source_ip in source_ips:
        source_ips.append(source_ip)
        try:
            hostname = gethostbyaddr(source_ip)[0]
        except:
            hostname = "err reaching hostname"
        getInfo(source_ip, userAgent, proxz, hostname)
