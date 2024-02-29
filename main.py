def solution():
    x = input().split()
    y = []
    z = []
    for i in range(len(x)):
        if i + 1 < len(x):
            if x[i].isalpha() and x[i + 1].isalpha():
                y.append(x[i])
                y.append(x[i + 1])
            if len(y) == 2:
                z.extend(y)
                y.clear()
    if len(z) <= 1:
        print('Мало слов!')
    else:
        for i in range(0, len(z), 2):
            print(z[i], z[i + 1])


solution()
