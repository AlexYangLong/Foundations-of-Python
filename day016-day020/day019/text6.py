from functools import reduce


def add(x, y):
    return x + y


long = int(input('龙：'))
knight = int(input('骑士：'))

long_list = []
for i in range(long):
    long_list.append(int(input()))
long_list.sort()

knight_list = []
for i in range(knight):
    knight_list.append(int(input()))
knight_list.sort()

if long > knight:
    print('Loowater is doomed!')
elif long == knight:
    if long_list[0] > knight[0]:
        print('Loowater is doomed!')
    else:
        print(reduce(add, knight_list))
else:
    n = 20001
    for i in range(knight):
        if knight_list[i] >= long_list[0]:
            n = i
            break

    if n != 20001:
        if long > (knight - n):
            print('Loowater is doomed!')
        else:
            # print(knight_list[n:n+long])
            print(reduce(add, knight_list[n:n+long]))
    else:
        print('Loowater is doomed!')