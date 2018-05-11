from math import sqrt


def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True if num != 1 else False


def save_prime(num, mode, path):
    with open(path, mode, encoding='utf-8') as fw:
        fw.write(str(num)+'\n')


def main(path):
    for i in range(1, 1001):
        if i == 1 or i == 2 or i == 3:
            save_prime(i, 'w', path)
        else:
            if is_prime(i):
                save_prime(i, 'w', path)


def main2(path):
    with open(path, 'w', encoding='utf-8') as fw:
        for i in range(1, 1001):
            if is_prime(i):
                fw.write(str(i) + '\n')


if __name__ == '__main__':
    path = 'prime.txt'
    main2(path)
