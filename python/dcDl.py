from urllib.request import Request, urlopen
import json

with open("fileeeDcc.txt", 'w') as fin:
    for i in range(1, 597):
        q = Request("http://www.dccomics.com/proxy/search?page=" + str(i) + "&type=comic%7Cgraphic_novel")
        q.add_header('Accept', '*/*')
        q.add_header('Accept-Encoding', 'gzip, deflate')
        q.add_header('Accept-Language', 'cs-CZ,cs;q=0.8')
        q.add_header('Connection', 'keep-alive')
        q.add_header('Cookie',
                     'has_js=1; s_cc=true; s_fid=3A87CB9B2F4CBEE8-356FE9D52AE568CD; s_sq=dcdccomics%3D%2526c.%2526a.%2526activitymap.%2526page%253DComics%2526link%253D' + str(
                         i) + '%2526region%253Ddcbrowseapp%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DComics%2526pidt%253D1%2526oid%253Dhttp%25253A%25252F%25252Fwww.dccomics.com%25252Fcomics%25253Fall%25253D1%252523%2526ot%253DA')
        q.add_header('Host', 'www.dccomics.com')
        q.add_header('Referer', 'http://www.dccomics.com/comics?all=1')
        q.add_header('User-Agent',
                     'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
        data = json.loads(urlopen(q).read().decode())
        print(str(i))
        if data['results']:
            for key, value in data['results'].items():
                fin.write(data['results'][key]['fields']['url'] + "\r\n")
                print(key)

fin.close()
