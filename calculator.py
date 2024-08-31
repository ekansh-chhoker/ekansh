while True :
    num1 = int(input("enter the number 1 : "))
    num2 = int(input("enter the number 2 : "))

    print("enter 1 for addition \nenter 2 for subtraction\nenter 3 for multiplication\nenter 4 for divisoin")

    choice = int(input("enter the number between 1 to 4 : "))
    if choice == 1:
        print("the sum is :",num1 + num2)
    elif choice == 2:
        print("the answer is :",num1 - num2)
    elif choice == 3:
        print( "the answer is :",num1 * num2)
    elif choice == 4:
        print("the answer is ",num1 / num2)
    else :
        print("invalid choice")
    end = input("enter quit to exit\npress enter to continue  ")
    if end == "quit":
        break

        
