

while True:
    print("\nVali tsükkel (1, 2, 3 või 0 väljumiseks):")
    valik = input("Sinu valik: ")

    if valik == "1":
        # Väljastame paaritud arvud kuni 30. #while tingimusega
        x = 0
        while x < 30:
            if x % 2 == 1:
                print(x, end=" ")
            x += 1
        print()

    elif valik == "2":
        # while True ja break
        print("Paaritud arvud kuni 30. Kasutame while True ja break")
        x = 0
        while True:
            if x % 2 == 1:
                print(x, end=" ")
            x += 1
            if x >= 30:
                break
        print()

    elif valik == "3":
        # for-tsükkel
        print("Paaritud arvud kuni 30 kasutame for-tsüklit")
        for x in range(30):
            if x % 2 == 1:
                print(x, end=" ")
    elif valik=="4":
        print("Väljun")
        break
    

    elif valik == "0":
        break
