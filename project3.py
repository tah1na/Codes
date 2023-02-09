def start():
    print("You just woke up and you're very hungry. You freshen up and decide to make lunch. You open the fridge but it's as empty as your stomach. But Allmart has 'all' you need. Get out for once and go to Allmart to get all the right ingredients! Spend your money wisely!\n\tYou have 50 currency.")
    home()

def home():
    print("You are in your home")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tallmart\n\tsnacks\n\tmovies\n")
    if move.lower() == "allmart":
        allmart()
    elif move.lower() == "snacks":
        snacks()
    elif move.lower() == "movies":
        movies()
    else:
        print("\nsorry, I don't understand your input. I'll assume you want to stay here")
        #TODO: what should happen if they type something else?

def allmart():
    print("You are at Allmart. There are many people shopping around. The ingredient aisle is right on the corner. But you see that one CUTE little Xiao plushie you've always wanted. You need 1 vegetable and 1 meat but you also need the plushie. Your choice!")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tingredient_aisle\n\tcute_stuff_aisle\n\thome\n")
    if move.lower() == "ingredient_aisle":
        ingredient_aisle()
    elif move.lower() == "cute_stuff_aisle":
        cute_stuff_aisle()
    elif move.lower() == "home":
        home()
    else:
        print("\nsorry, I don't understand your input. I'll assume you want to stay here")
        #TODO: what should happen if they type something else?
        
def ingredient_aisle():
    print("You're in the ingredient aisle. Oh, you're actually doing your job.You need 1 meat and 1 vegetable. 1 meat is 25 money and 1 vegetable is 25 money. ")
    ingredient = input("would you like to buy?\nSay yes or no")
    if ingredient == "yes":
        global money
        money =50-(25+25)
        print("Now you have",money,"money and 1 meat and 1 vegetable")
        print("Congrats! You have all the ingredients!! You can finally have a meal.\n\tGood Ending.")
        input("Press enter to go back")
        home()
    elif ingredient == "no":
        print("Okay then.")
        move = input("\nWhere would you like to go? Say one of these choices:\n\tcute_stuff_aisle\n")
        if move.lower() == "cute_stuff_aisle":
            cute_stuff_aisle()
def cute_stuff_aisle():
    print("Oh no you just couldn't not come here. Just look at XIAO (and that price tag). You want that plushie, no, you NEED it. Now.")
    global money
    money = 50 - 50
    print("\n\t...\n\tYou have",money,"money.\n\tOh.\n")
    print("Congrats(?) You have a huge Xiao but no money and no food. You might starve, but you'll starve happy.\n\tEnding.\n")
    input("Press enter to go back")
    home()


def movies():
    print("You are in the  movie theatre. You don't know why you're here? You should be getting groceries. Or you could watch a movie, why not?")
    move = input("\nWhere would you like to go? Say one of these choices:\n\thome\n\twatch a movie\n")
    if move.lower() == "home":
        home()
    elif move.lower() == "watch a movie":
        watch_movie()
    else:
        print("\nsorry, I don't understand your input. I'll assume you want to stay here")
        #TODO: what should happen if they type something else?
def watch_movie():
    print("'The Room' is airing right now. You had heard about this movie before, how good-bad it was. Worth a shot.")
    global money
    money = 50-50
    print("You spent all your money on the ticket.\n\tYou now have",money,"money\n")
    print("\n\t1 hour and 40 minutes later...\n")
    print("You don't know what you just witnessed. How was that a movie? Should've been left in the drafts. Good job you just wasted all your money on a terrible movie.\nAtleast you got some popcorn.\n\tBeware of bad movies Ending\n")
    input("Press enter to go back")
    home()

def snacks():
    print("You are at the snacks store. The food smells delicious. There are some people here too, eating rather messily. The owner looks at you.\n\tKeeps looking at you\n\tYou should buy all of those sweet baked potatoes, they look sooo good.\n\tWait what? You should go.\n")
    move = input("\nThings are getting real weird. You really should go. Say one of these choices:\n\thome\nsuccumb to sweet potatoes\n")
    if move.lower() == "home":
        home()
    elif move.lower() == "succumb to sweet potatoes":
        debt()
    else:
         print("\nsorry, I don't understand your input. I'll assume you want to stay here")
def debt():
    global money
    money = -50
    print("money",money)
    money = -100
    print("money",money)
    money = -250
    print("money",money)
    print("You just couldn't help it. You are overcome with this urgent sense to devour all the sweet potatoes. You pull out a stool and start eating them one by one. Again and again. Stuck in this endless loop, how are you ever going to pay this off?\n")
    print("\n\tEnding-Debt\n")
    input("Press enter to go back")
    home()
    

########
#main
#######
#TODO: Add some global variables
    money = int(50) 
start()