# tesseract required, code is in dev setting

import numpy as np
from PIL import Image
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colors import rgb, hex
import mimetypes
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def crack(cap_name):
    decoded = 0
    dlpath = 'C:\\pics\\dld\\'''
    im = Image.open('C:\\pics\\dld\\''' + cap_name + '.gif').convert('RGB')
    pixelMap = im.load()
    img = Image.new(im.mode, im.size)
    pixelsNew = img.load()
    start = str(rgb(250, 170, 4).hex)
    end = str(rgb(255, 180, 8).hex)
    start = int(start, 16)
    end = int(end, 16)
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            nakycislo = '%02x%02x%02x' % (pixelMap[i, j])
            nakycislo = int(nakycislo, 16)
            if nakycislo in range(start, end):
                pixelsNew[i, j] = pixelMap[i, j]
            else:
                pixelMap[i, j] = (255, 255, 255)
    ext = ".jpg"
    img.save("C:\\pics\\cerned\\""" + cap_name + ext)
    ims = Image.open('C:\\pics\\cerned\\''' + cap_name + '.jpg')
    ims = im.convert('RGBA')
    datas = np.array(ims)
    red, green, blue, alpha = datas.T
    white_areas = (red == 0) & (blue == 0) & (green == 0)
    datas[..., :-1][white_areas.T] = (255, 255, 255)
    ims = Image.fromarray(datas)
    ims.show()
    ext = ".tif"
    ims.save("C:\\pics\\clnd\\""" + cap_name + ext)
    command = "tesseract -psm 7 C:\\pics\\clnd\\""" + cap_name + ".tif " + "C:\\pics\\txt digits"
    os.system(command)
    time.sleep(1)
    Text = open("C:\\pics\\txt.txt", "r")
    decoded = Text.readline().strip(' ')


# main(2)
# sys.exit(0)

def walker(klk):
    chromedriver = "C:\compo"
    basePath = "https://www.mojedatovaschranka.cz/"
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "C:\\schranka\\prilohy\\"""}
    chromeOptions.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser.set_window_size(1024, 768)
    browser.get(basePath)
    catchThtCaptcha = browser.find_element_by_xpath('//*[@id="IDPLogin"]/table/tbody/tr[4]/td[1]/img')
    location = catchThtCaptcha.location
    size = catchThtCaptcha.size
    left = location.get("x", "none")
    top = location.get("y", "none")
    width = size.get("width", "none")
    height = size.get("height", "none")
    browser.save_screenshot('C:\\pics\\ssd\\''' + str(klk) + '.gif''')
    sshot = Image.open('C:\\pics\\ssd\\''' + str(klk) + '.gif''')
    sshot.show()
    box = (left, top, left + width, top + height)
    area = sshot.crop(box)
    area.save("C:\\pics\\dld\\""" + str(klk) + ".gif", quality=100)
    area.show()
    crack(str(klk))
    browser.maximize_window()
    browser.set_window_size(1024, 768)
    browser.set_window_position(0, 0)
    Text = open("C:\\pics\\txt.txt", "r")
    decoded = Text.readline().strip('\n')
    user = browser.find_element_by_css_selector("input[name='Ecom_User_ID']")
    user.send_keys("LOGIN")
    pw = browser.find_element_by_css_selector("input[name='Ecom_Password']")
    pw.send_keys("PW")
    cptchi = browser.find_element_by_css_selector("input[name='Ecom_Captcha']")
    decoded.rstrip(" ")
    cptchi.send_keys(decoded)
    browser.find_element_by_css_selector("#Ecom_Button_Login").click()
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".abs-panel-a"))
        )
    except:
        browser.quit()
        print("Nepodařilo se přečíst captchu, skript se pustí znovu.")
        main(2)
        sys.exit(0)
    stav = browser.find_element_by_css_selector(".home-confirmation-info-notice h2")
    if stav.text == "Nemáte žádné nové zprávy.":
        browser.find_element_by_xpath('//*[@id="main"]/div[3]/div[2]/div[1]/p/a').click()
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".content.line.clickable")))
        msGCont = browser.find_elements_by_css_selector('.messages .text .clickable')
        # msGCont = browser.find_elements_by_css_selector('.messages .text .clickable') v realu tam jeste prijde do selectoru classa "unread"
        msgsCount = len(browser.find_elements_by_css_selector('.messages .text .clickable'))
        msgsCount = msgsCount + 2
        msgCountList = range(1, msgsCount)
        iterMsgCounList = iter(msgCountList)
        next(iterMsgCounList, None)
        for idx, val in enumerate(iterMsgCounList):
            strInt = str(val)
            linkaMailCesta = '//*[@id="main"]/div[4]/table/tbody/tr[' + strInt + ']/td[2]/div'
            linkaMail = browser.find_element_by_xpath(linkaMailCesta)
            linkaMail.click()
            element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".subject")))
            title = browser.find_element_by_class_name('subject').text
            fromX = browser.find_element_by_xpath('//*[@id="main"]/div[2]/div[3]/div[1]/div[3]/p[1]/strong').text
            # unreadMails.append({'title': title, 'fromX': fromX})
            fajlC = browser.find_element_by_css_selector(".attachment a")
            fajlLink = fajlC.get_attribute('href')
            fajlC.click()
            directory = "C:\\schranka\\prilohy\\"""
            outer = MIMEMultipart()
            outer['Subject'] = 'DS msg' + title
            time.sleep(1)
            for filename in os.listdir(directory):
                path = os.path.join(directory, filename)
                if not os.path.isfile(path):
                    continue
                ctype, encoding = mimetypes.guess_type(path)
                if ctype is None or encoding is not None:
                    ctype = 'application/octet-stream'
                maintype, subtype = ctype.split('/', 1)
                if maintype == 'text':
                    with open(path) as fp:
                        msg = MIMEText(fp.read(), _subtype=subtype)
                elif maintype == 'image':
                    with open(path, 'rb') as fp:
                        msg = MIMEImage(fp.read(), _subtype=subtype)
                elif maintype == 'audio':
                    with open(path, 'rb') as fp:
                        msg = MIMEAudio(fp.read(), _subtype=subtype)
                else:
                    with open(path, 'rb') as fp:
                        msg = MIMEBase(maintype, subtype)
                        msg.set_payload(fp.read())
                    encoders.encode_base64(msg)
                msg.add_header('Content-Disposition', 'attachment', filename=filename)
                outer.attach(msg)
            composed = outer.as_string()
            with smtplib.SMTP('smtp.gmail.com', 587) as s:
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login('example@email.com', 'pw')
                s.sendmail("example@email.com", "recepient@email.com", composed)
            browser.execute_script("window.history.go(-1)")
            element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".content.line.clickable")))

    else:
        print("kks")


def main(klk):
    for klk in range(1, klk):
        walker(klk)
        print(klk)


main(2)
