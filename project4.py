import random
roll_dice = input("Write start to dice roll: ")
rolls = 1
trials = 0
while trials < 1000:
    if roll_dice == "start":
        possible_results = [1, 2, 3, 4, 5, 6]
    result = random.choice(possible_results)
    print(result)
    while result != 6:
        posiblle_results = [1, 2, 3, 4, 5, 6]
        result = random.choice(possible_results)
        rolls += 1
    trials += 1
print("Number of times you rolled a six:", trials)
print("Average number of rolls needed:", rolls/1000)