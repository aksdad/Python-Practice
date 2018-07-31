def sum2(a, x):
    map = dict()

    for i in range(len(a)):
        if a[i] in map.keys():
            map[a[i]] = 0
        else:
            map[a[i]] += 1

    for i in range(len(a)):
        complement = x - a[i]

        if complement in map.keys():
            temp = map[complement]
            map[complement] -= 1

if __name__ == '__main__':
