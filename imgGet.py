import os

os.makedirs('./image/', exist_ok=True)
IMAGE_URL = "https://bet.hkjc.com/marksix/info/images/icon/no_01.gif?CV=L302R1ja"


def urllib_download():
    from urllib.request import urlretrieve
    for i in range(1,9):
        chang = str(i)
        url = "https://bet.hkjc.com/marksix/info/images/icon/no_0"+chang+".gif?CV=L302R1ja"
        print(url)
        urlretrieve(url, './image/img'+chang+'.gif')


def request_download():
    import requests
    r = requests.get(IMAGE_URL)
    with open('./image/img2.png', 'wb') as f:
        f.write(r.content)


def chunk_download():
    import requests
    r = requests.get(IMAGE_URL, stream=True)
    with open('./image/img3.png', 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)


urllib_download()
# print('download img1')
# request_download()
# print('download img2')
# chunk_download()
# print('download img3')
