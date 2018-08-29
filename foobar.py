
n = int(input ("Enter a maximum for the list: "))


def foobar(n):
    for i in range (n):
        if i % 15 == 0:
            print("FOOBAR!")
        elif i % 5 == 0:
            print("BAR!")
        elif i % 3 == 0:
            print("FOO!")
        else:
            print(i)

foobar(n)
