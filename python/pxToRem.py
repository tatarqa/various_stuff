import os
import re

cssIn = 'C:\\CSS\\IN\\'''
cssOut = 'C:\\CSS\\OUT\\'''
cssMod = 'C:\\CSS\\MODED\\'''
cssFinal = 'C:\\CSS\\FINAL\\'''
styles = [
    "margin",
    "margin-left",
    "margin-right",
    "margin-top",
    "margin-bottom",
    "padding",
    "padding-left",
    "padding-right",
    "padding-top",
    "padding-bottom",
    "line-height",
    "font-size",
    "line-height"
]
dvojtecka = ":"
values = []
modifiedStyles = []
skippedContent = ""
htmlFontSize = 16
pepper = "xzlt"
fileEncoding = 'Windows-1252'
mediaQueryEnded = re.compile(r'(}[ \t\n\r\f\v]+})')  # todo
mediaQueyIsEmpty = re.compile(r'@.*({[ \t\n\r\f\v]+})')
currentCssIsUnderMediaQuery = False
currentCssIsUnderComment = False

for f in os.listdir(cssIn):
    fnm = str(f)
    try:
        with open(cssIn + fnm, 'r', encoding=fileEncoding, errors='ignore') as fp:
            dumm = open(cssMod + fnm, 'w', encoding=fileEncoding)
            linky = fp.readlines()
            for line in linky:
                helpMeOut = line.find('}')
                radek = line[:helpMeOut] + pepper + '\n' + line[helpMeOut:]
                dumm.write(radek)
    except IOError:
        raise Exception('ERR ' + fnm)

for f in os.listdir(cssMod):
    fnm = str(f)
    try:
        with open(cssMod + fnm, 'r', encoding=fileEncoding, errors='ignore') as fp:
            dumm = open(cssOut + fnm, 'w', encoding=fileEncoding)
            linky = fp.readlines()
            for line in linky:
                line = re.sub(pepper + '\n', '', line)
                if line.find('/*') != -1:
                    currentCssIsUnderComment = True
                if currentCssIsUnderComment is False:
                    radek = line
                    if line.find('@media') != -1:
                        currentCssIsUnderMediaQuery = True
                    if currentCssIsUnderMediaQuery is False:
                        for i, value in enumerate(styles):
                            nojo = ''
                            for wantedStyle in re.finditer(value + dvojtecka + '(.*);', line, re.S):
                                wantedStyleValue = (wantedStyle.group(1))
                                wantedStyleValue = re.sub(r'(\d+)px', lambda maaaaaatch: str(
                                    int(re.sub("[^0-9]", "", maaaaaatch.group(0))) / htmlFontSize) + "rem",
                                                          wantedStyleValue)
                                wantedStyleTx = value + dvojtecka
                                wantedStyleTx += wantedStyleValue + ";"
                                radek = radek + wantedStyleTx
                    else:
                        skippedContent += radek + '\n'
                        if mediaQueryEnded.search(skippedContent) or mediaQueyIsEmpty.search(skippedContent):
                            currentCssIsUnderMediaQuery = False
                            skippedContent = ""
                    dumm.write(radek)
                else:
                    dumm.write(line)
                    if line.find('*/') != -1:
                        currentCssIsUnderComment = False
    except IOError:
        raise Exception('ERR ' + fnm)
