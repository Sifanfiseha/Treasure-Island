print("welcome to the treasure island.\nyour mission is to find the treasure.")
turn = input("welcome to the cross road where do ypu want to go? \ntype left or right :")
if(turn == "left"):
    print("you have come to a lake. there is an island in the middle of the lake.")
    lake = input("type 'wait' to waint for a boat or type 'swim' to swim across : ")
    if(lake == "wait"):
        print("you have arrived at the island unharmed.")
        color = input("There is a house with three doors one red, one yellow and one blue. which color do you choose? :")
        if(color == "yellow"):
            print("you won the game!!!")
        elif(color == "red" and color == "blue"):
            print("game over")
    else:
            print("game over!!!")
else:
    print("game over!!!")
