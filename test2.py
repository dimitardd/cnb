import random
comp = set()
while len(comp) < 4:
    comp.add(random.randint(0, 9))
print(comp)
print(type(comp))
for i in range(0,4):
    comp = list(comp)
a = str(comp[0]) + str(comp[1]) + str(comp[2]) + str(comp[3])

print(a)
print(type(a))

comp = str(1234)
user = str(2134)
print(comp)
print(user)


cowandbull = [0, 0]

for i in range(0, 4):
    if comp[i] == user[i]:
        cowandbull[0] += 1
        print(comp[i], user[i])
        print("Bull {} in i {} ". format(cowandbull, i))
    elif comp[i] == user[0]:
        cowandbull[1] += 1
        print("Cow1 {} in i {} ".format(cowandbull, i))
    elif comp[i] == user[1]:
        cowandbull[1] += 1
        print("Cow1 {} in i {} ". format(cowandbull, i))
    elif comp[i] == user[2]:
        cowandbull[1] += 1
        print("Cow2 {} in i {} ". format(cowandbull, i))
    elif comp[i] == user[3]:
        cowandbull[1] += 1
        print("Cow3 {} in i {} ". format(cowandbull, i))

print(cowandbull)
