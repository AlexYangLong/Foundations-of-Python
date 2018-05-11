import json, os, requests


def main():
    try:
        with open('./mntp/mntp.json', 'r', encoding='utf-8') as fr:
            content = fr.read()

        dict_data = json.loads(content, encoding='utf-8')
        # print(type(dict_data))
        for temp_dict in dict_data['newslist']:
            title = temp_dict['title']
            pic_url = temp_dict['picUrl']
            pic_name = pic_url[pic_url.rfind('/')+1:]
            resp = requests.get(pic_url)
            with open(os.path.join('./mntp', pic_name), 'wb') as fw:
                fw.write(resp.content)

    except:
        print('打开文件出错！')


if __name__ == '__main__':
    main()