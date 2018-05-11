
def print_triangle(n):
    for i in range(1, n + 1):
        for j in range(n-i):
            print(' ', end='')
        for x in range(2 * i - 1):
            print('*', end='')
        print()

def print_triangle2(n):
    for i in list(range(1, n+1))[::-1]:
        for j in range(n - i):
            print(' ', end='')
        for x in range(2*i-1):
            print('*', end='')
        print()

def print_yanghui(n):
    list1 = []
    for i in range(1, n + 1):
        list1.append([])
        for j in range(n-i):
            list1[i-1].append(0)
        if i == 1:
            list1[i-1].append(1)
        else:
            for x in list(range(n-i, n - i + 2 * i -1)[::2]):
                if x == n-i or x == n + i-2:
                    list1[i-1].append(1)
                    list1[i-1].append(0)
                else:
                    list1[i-1].append(list1[i-2][x-1] + list1[i-2][x+1])
                    list1[i - 1].append(0)
    for i in range(n):
        for j in range(len(list1[i])):
            if list1[i][j] == 0:
                print(' ', end='')
            else:
                print(list1[i][j], end='')
        print()


def main():
    print_triangle(7)
    print_triangle2(7)
    print_yanghui(7)
    # print(list(range(0,10)[::2]))


if __name__ == '__main__':
    main()
