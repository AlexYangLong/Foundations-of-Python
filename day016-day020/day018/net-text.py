# 有多台独立自主的计算机互联而成的系统的总称就是计算机网络


import requests, json


def main():
    url = 'https://www.baidu.com/img/bd_logo1.png'
    url = 'http://api.tianapi.com/meinv/?key=fab41aa3a9038dd3f43424a53a181b8c&num=10'
    resp = requests.get(url)

    # dict_data = json.loads(resp.text, encoding='utf-8')
    # print(resp.text)
    try:
        with open('./mntp/mntp.json', 'w', encoding='utf-8') as fw:
            fw.write(resp.text)
    except:
        print('写文件出错！')


if __name__ == '__main__':
    main()






