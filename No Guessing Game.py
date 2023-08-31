import random
num=random.randint(0,100)
print("Ans is ",num)
guess=[]
while len(guess)<5:
    all_guess=int(input("Enter  the number  " ))
    guess.append(all_guess)
    if all_guess >99 or all_guess<0:
        print("invalid range Plese enter no b/w 0 to 100")
    elif all_guess==num:
        print("You are Winner")
        print(f"Congrats !!! you guess  is {all_guess} ")
        print(f"You reached the correct guess in  {len(guess)} tries" )
        break
    elif len(guess)==5:
        print(" You are looser and Limit over please try again ")

    elif all_guess>num:
        print("Please enter lower number")
    elif all_guess<num:
        print("please enter higher Number")

