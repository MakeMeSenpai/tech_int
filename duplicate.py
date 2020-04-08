def dup(l):
    index = 0
    for n in range(len(l) - 1):
        print("l:" + str(l[index]))
        print("n:" + str(l[n+1]))
        if l[index] == l[n+1]:
            print("True")
            return True
        index += 1
    print("Flase")
    return False

lists = [[12, 3, 8, 8, 4], [1, 5, 6, 9, 10, 10], [2, 3, 6, 4, 8]]
for l in lists:
    dup(l)