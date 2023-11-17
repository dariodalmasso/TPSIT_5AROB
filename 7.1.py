import math

def mia_radq(a):
    x = 4

    while True:
        #print(x)
        y = (x + a / x) / 2
        if y == x:
            break
        x = y

    return y

def main():
    a = 0
    print('------------')

    for _ in range(9):
        a = a + 1
        print(f'{a}.    {round(mia_radq(a), 8)}     {round(math.sqrt(a), 8)}    {mia_radq(a) - math.sqrt(a)}')

    print('------------')

if __name__ == '__main__':
    main()