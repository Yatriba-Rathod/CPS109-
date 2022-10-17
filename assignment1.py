def assign1():
    name = input("Enter your name: ")
    print("Welcome", name,"to the adventure game!")
    conf= str(input("Are you ready to begin the adventure? "))
    if conf=="yes" or "Yes" or "YES":
        print("Great! Let's begin", name,"!")
        q1=input("You are walking through the woods and you come across two paths, left and right. Type 'left' for going left or 'right' for going right. ")
        if q1=="left":
            q2=input("Now you're on the left road of the jungle. After walking some distance, you see a lion. What would you do? Type 'run' to run away or 'climb' to climb a tree. ")
            if q2== "run":
                q33=input("Woah! You're fast! You escaped. Now you come across a group of tribes. Type 'talk' to get help to escape or 'run' to find your own way. ")
                if q33=="talk":
                    print("You were eaten by the tribe! You lose!")
                    qrr=input("Would you like to play again? ")
                    while qrr=="yes":
                        return(assign1())
                    while qrr=="no":
                        return(hi())
                elif q33=="run":
                    print("You're independent! You successfully escaped the jungle! You win!")
                else:
                    print("Invalid Input")
            elif q2=="climb":
                print("Surprise! There's an Anaconda up here.You lose!")
                qr=input("Would you like to play again? ")
                while qr=="yes":
                    return(assign1())
                while qr=="no":
                    return(hi())
            else:
                print("Invalid input")
        elif q1=="right":
            q3=input("You come across a river and you don't know if it's safe to cross. Type 'cross' to cross it by boat or 'back' to go back. ")
            if q3=="cross":
                q4=input("You crossed safely! Now you come across a stranger. Type 'ignore' to ignore the person or 'talk' to talk and ask for the way out of the jungle ")
                if q4=="Talk":
                    print("You asked him the way out and you escaped successfully! Thanks for playing this game", name,"!")
                elif q4=="ignore":
                    print("You missed the chance to escape and now you're stuck in jungle without any food or water. You're DEAD! ")
                else:
                    print("Invalid input")
            elif q3=="back":
                print("You lost the way and are now dying of hunger and thirst. You're DEAD!")
            else:
                print("Invalid input")
        else:
            print("Invalid input ")
    elif conf=="no" or "No" or"NO":
        return hi()
    else:
        print("Invalid input")
def hi():
    print ("Oops! You're not interested? Nvm, See you next time")
hi()
assign1()
