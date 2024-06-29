import random
def hangman():
    word=random.choice(["plugger","tiger","manoj","anshuman","tatiya","amit","aman","negi"])
    validletter='abcdefghijklmnopqrstuvwxyz'
    turn=10
    guessmade=''
    while len(word)>0:
        main=""
        missed=0
        for letter in word:
            if letter in guessmade:
                main=main+letter
            else:
                main=main+"_"+""
        if main==word:
            print(main)
            print("you win!")
            break
        print("guess the word:",main)
        guess=input()
        if guess in validletter:
            guessmade=guessmade+guess
        else:
            print("enter valid character")
            guess=input()
        if guess not in word:
            turn=turn-1
            if turn==9:
                print("9 turn left")
                print("______")
            if turn==8:
                print("8 turn left")
                print("________")
                print("    O    ")
            if turn==7:
                print("7 turn left")
                print("________")
                print("    O    ")
                print("    |      ")
            if turn==6:
                print("6 turn left")
                print("________")
                print("    O    ")
                print("    |      ")
                print("   /      ")
            if turn==5:
                print("5 turn left")
                print("________")
                print("    O    ")
                print("    |      ")
                print("   / \     ")
            if turn==4:
                print("4 turn left")
                print("________")
                print("  \ O    ")
                print("    |      ")
                print("   / \     ")
            if turn==3:
                print("3 turn left")
                print("________")
                print("  \ O /   ")
                print("    |      ")
                print("   / \     ")
            if turn==2:
                print("2 turn left")
                print("________")
                print("  \ O /|   ")
                print("    |      ")
                print("   / \     ")
            if turn==1:
                print("1 turn left")
                print("last bredth counting")
                print("________")
                print("  \ O _|/   ")
                print("    |      ")
                print("   / \     ")
            if turn==0:
                print("you lose")
                print("you let a kind men die")
                print("________")
                print("    O _|   ")
                print("   /|\      ")
                print("   / \     ")
                break


    
name=input("Enter your Name\n")
print("welcome",name )
print("-----------")
print("guess the word in less than 10 attempts")
hangman()
print()