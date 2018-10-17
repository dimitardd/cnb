import random

maxtry = int(input("Please set how many tries will be the game!"))


def check_num(comp, user):
    cowandbull = [0, 0]
    for i in range(0, 4):
        if comp[i] == user[i]:
            cowandbull[0] += 1
        else:
            for y in range(0, 4):
                if comp[i] == user[y]:
                    cowandbull[1] += 1
    return cowandbull


if __name__=="__main__":
    playing = True
    comp = set()
    while len(comp) < 4:
        comp.add(random.randint(0, 9))
    comp = list(comp)
    comp = str(comp[0]) + str(comp[1]) + str(comp[2]) + str(comp[3])
    print(comp)
    guesses = 0

    while playing:
        user = input("Shoot now!\n ")
        if user == "exit":
            break
        elif guesses >= maxtry:
            print("You lost", guesses)
            break
        cowandbull = check_num(comp, user)
        guesses += 1

        print("You have " + str(cowandbull[0]) + " Bulls, and " + str(cowandbull[1]) + " Cows.")

        if cowandbull[0] == 4:
            playing = False
            print("You win the game after " + str(guesses) + "! The number was " + str(comp))
            break
        else:
            print("Your guess isn't quite right, try again.\n")
