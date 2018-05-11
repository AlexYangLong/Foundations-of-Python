from time import time

import requests
from threading import Thread


def download_img(url):
    try:
        filename = url[url.rfind('/') + 1:]
        resp = requests.get(url)
        with open('./mntp/' + filename, 'wb') as fw:
            fw.write(resp.content)
        print('图片下载成功')
    except IOError as ex:
        print(ex)
        print('下载图片出错')


def main():
    try:
        start = time()
        thread_list = []
        url = 'http://api.tianapi.com/meinv/?key=fab41aa3a9038dd3f43424a53a181b8c&num=20'
        resp = requests.get(url)
        print(resp.text)
        data_dict = resp.json()  # resp.json() 将获取的json字符串转成字典
        for mn_dict in data_dict['newslist']:
            url = mn_dict['picUrl']
            t = Thread(target=download_img, args=(url, ))
            thread_list.append(t)
            t.start()
        for t in thread_list:
            t.join()
        end = time()
        print('总共耗时：%f s' % (end - start))
    except:
        print('出错了')


if __name__ == '__main__':
    main()
