#Exercise 2.2

def sortarray(xs):
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] > xs[j]:
                temp = xs[i]
                xs[i] = xs[j]
                xs[j] = temp
    return xs

data = [5, 2, 4, 1, 3, 0]
t = sortarray(data)
print(t)