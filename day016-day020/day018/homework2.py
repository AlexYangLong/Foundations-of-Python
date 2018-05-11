import requests, json, urllib.parse


def main():
    chengyu = input('请输入您要查询的成语：')
    url = 'http://api.tianapi.com/txapi/chengyu/?key=fab41aa3a9038dd3f43424a53a181b8c&word='
    url += urllib.parse.quote(chengyu)
    print(url)

    try:
        resp = requests.get(url)
        dict_data = json.loads(resp.text)
        res_dict = dict_data['newslist'][0]
        print('chengyu:', res_dict['chengyu'])
        print('pinyin:', res_dict['pinyin'])
        print('jiesi:', res_dict['diangu'])
        print('chuchu:', res_dict['chuchu'])
        print('fanli:', res_dict['fanli'])
    except:
        print('HTTP请求失败！请稍后重试')


if __name__ == '__main__':
    main()
