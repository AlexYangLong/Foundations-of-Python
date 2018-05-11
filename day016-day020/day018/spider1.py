import re

import requests


def main():
    url = 'https://www.taobao.com/markets/mm/mm2017'
    resp = requests.get(url)
    print(resp.text)

    # with open('./mmtb/mmtb.html', 'w', encoding='utf-8') as fw:
    #     fw.write(resp.text)

    img_list = re.findall(r'', resp.text)


if __name__ == '__main__':
    main()
