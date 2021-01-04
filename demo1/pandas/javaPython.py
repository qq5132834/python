import sys


# java调用python代码

def func(a, b):
    print("func")
    return (a + b)


if __name__ == '__main__':
    a = []
    for i in range(1, len(sys.argv)):
        a.append((int(sys.argv[i])))
    print("__main__")
    print(func(a[0], a[1]))
