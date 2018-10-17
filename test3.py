comp = str(1234)
user = str(2143)
print(comp)
print(user)
d = [0, 0]
for i in range(0, 4):
        if comp[i] == user[i]:
            print("BULL")
            d[0] += 1
            print(comp[i], user[i])
        else:
            for y in range(0, 4):
                print("i and y: ", i, y)
                if comp[i] == user[y]:
                    print("COW")
                    d[1] += 1
                    print(comp[i], user[y])
print(d)