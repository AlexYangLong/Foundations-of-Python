
def file_copy(path, new_path):
    try:
        with open(path, 'r', encoding='utf-8') as fr:
            content = fr.read()
        with open(new_path, 'w', encoding='utf-8') as fw:
            fw.write(content)
        print('file拷贝到file_cp拷贝成功～～')
    except:
        print('file文件打开错误，拷贝失败～～')


def main():
    file_copy('file.txt', 'file_cp.txt')


if __name__ == '__main__':
    main()