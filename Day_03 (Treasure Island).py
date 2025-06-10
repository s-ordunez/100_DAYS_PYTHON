print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#level 1
print("You come to a fork in the jungle.") 
next_level = input("Do you go left or right? l or r: ")

if next_level != "l":
    print("You fell into a hole, GAME OVER!")
else:
    print("You come to a river filled with pirahnas!")
    next_level = input("Do you swim across or wait? s or w: ")

    if next_level != "w":
        ("The pirahnas ate you, GAME OVER!")

    else:
        print("Three magical doors appear.")
        print("They are red, blue and yellow.")
        next_level = input("Which door do you go through? r,b,y: ")

        if next_level == "r":
            print("You are burned up by fire, GAME OVER")
        elif next_level == "b":
            print("You are eaten by a zombie, GAME OVER!")
        elif next_level == "y":
            print("Congratulations you found the treasure!")
        else:
            print("GAME OVER!")
