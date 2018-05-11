import requests, json, urllib.parse


def main():
    dream_word = input('请输入您梦境的关键词：')
    url = 'http://api.tianapi.com/txapi/dream/?key=fab41aa3a9038dd3f43424a53a181b8c&word='
    url += urllib.parse.quote(dream_word)
    print(url)

    try:
        resp = requests.get(url)
        dict_data = json.loads(resp.text)
        res_dict = dict_data['newslist'][0]
        print('id:', res_dict['id'])
        print('type:', res_dict['type'])
        print('title:', res_dict['title'])
        print('result:', res_dict['result'])
    except:
        print('HTTP请求失败！请稍后重试')



if __name__ == '__main__':
    main()
