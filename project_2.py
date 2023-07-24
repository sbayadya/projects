import random
 
min_val = 1
max_val = 6
roll_again = "yes"
while roll_again == "yes":
    print("Rolling the dices...")
    val1 = random.randint(min_val, max_val)
    val2 = random.randint(min_val, max_val)
    print("The sum of dice is", val1 ,"+", val2, "=", val1+val2)
    if val1 + val2 == 7 or val1+val2 == 11:
        print("You won!!!!")
        exit()
    elif val1 + val2 == 2 or val1 + val2 == 3 or val1 + val2 == 12:
        print("Oooops, casino won((")
        exit()
    else:
        val1 + val2 == 4 or val1 + val2 == 5 or val1 + val2 == 6 or val1 + val2 == 8 or val1 + val2 == 9 or val1 + val2 ==10
        print("Now your goal number is ", val1 + val2)
        goal_number = val1 + val2
    roll_again = input("Type 'again' to continue rolling the dices: ")
 
while roll_again == "again":
    print("Rolling the dices...")
    val1 = random.randint(min_val, max_val)
    val2 = random.randint(min_val, max_val)
    print("The sum of dice is", val1, "+", val2, "=", val1 + val2)
    if val1 + val2 == 7:
        print("You lose")
        exit()
    elif val1 + val2 == goal_number:
        print("You won!!!!")
        exit()
    else:
        roll_again == input("Type 'again' to continue rolling the dices: ")
