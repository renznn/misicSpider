import requests
import json
import re
import os


def get_song(x, num):
    if not os.path.exists('download'):
        os.makedirs('download')
    url = "http://songsearch.kugou.com/song_search_v2?callback=jQuery112407470964083509348_1534929985284&keyword={}&" \
          "page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filte" \
          "r=0&_=1534929985286".format(x)
    res = requests.get(url).text
    js = json.loads(res[res.index('(') + 1:-2])
    data = js['data']['lists']
    for i in range(num):
        print(str(i + 1) + ">>>" + str(data[i]['FileName']).replace('<em>', '').replace('</em>', ''))
        # number = int(input("\n请输入要下载的歌曲序号（输入-1退出程序）: "))
        # if number == -1:
        #     exit()
        # else:
        name = 'download/' + str(data[i]['FileName']).replace('<em>', '').replace('</em>', '')
        fhash = re.findall('"FileHash":"(.*?)"', res)[i]
        hash_url = "http://www.kugou.com/yy/index.php?r=play/getdata&hash=" + fhash
        hash_content = requests.get(hash_url)
        play_url = ''.join(re.findall('"play_url":"(.*?)"', hash_content.text))
        real_download_url = play_url.replace("\\", "")
        with open(name + ".mp3", "wb")as fp:
            fp.write(requests.get(real_download_url).content)
        print("歌曲已下载完成！")


if __name__ == '__main__':
    data = []
    for line in open("music.txt", "r", encoding='utf-8'):  # 设置文件对象并读取每一行文件
        line = line.strip('\n')
        obj = line.split('-')
        # data.append(line)
        print(obj.__len__())
        if obj.__len__() == 1:
            obj.append(1)
        get_song(obj[0], int(obj[1]) if int(obj[1]) > 0 else 1)
    # x =input("请输入歌名：")
    # get_song(x)
