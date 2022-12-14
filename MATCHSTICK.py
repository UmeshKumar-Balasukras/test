matchsticks=21
print("-----Hola! welcome to the game of matchsticks-----")
while True:
    option = int(input("\npress ------1:Instructions\n "
                       "     ------2:play --------"))
    if option == 1:
        print("*** THERE ARE 21 MATCHSTICKS IN THE GAME .FIRST THE USER PICKS NUMBER OF STICKE BETWEEEN 1-4 \n"
              "THEN THE COMPUITER PICKS THE MATCHSTICKS BETWEEN (1,4) .THE PLAYER WHO PICKS THE LAST STICKE LOOSES ..")
        continue
    elif option == 2:
        name=input(" PLEASE ENTER YOUR NAME :")
        while matchsticks>1:
            player = int(input("\nentere the no of matchsticks you wanna pick[1-4]:"))
            if player in range(1, 5):
                matchsticks -= player
                print("you picked ", player, "matchsticks\t")
                print("number of matchsticks remaining is :", matchsticks)
                computer = 5 - player
                print("\ncomputer picked ", computer, "matchsticks")
                matchsticks -= computer
                print("number of matchsticks remaining is :", matchsticks)
                if matchsticks == 1:
                    print("\n you picked the last matchstick and you lose the game ")
                    print("\n ************ 😓 BETTER LUCK NEXT TIME" ,name.upper()," ************ 😓 ")
                    break
            else:
                print("please pick valid number of sticke i.e min==1 and max ==4 ")
        break



    else:
        print("please select the valid option ")
        continue


