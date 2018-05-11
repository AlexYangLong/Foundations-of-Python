
def splitChar(str, chr=''):
    res_list = []
    while len(str) > 0:
        res_list.append(str[:str.index(chr)])
        str = str[str.index(chr) + 1:]
    return res_list


def main():
    print(splitChar('#name#yang#', '#'))


if __name__ == '__main__':
    main()
