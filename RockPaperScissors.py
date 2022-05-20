import random
thisdict =	{
  "c": "Scissor",
  "p": "Paper",
  "s": "Stone"
}
mylist = ['c', 'p', 's'] 
user_input, x = '', '' #initialize
while user_input != 'q' and x != '\n':
    x = input("S(c)issors, Pa(p)er, (S)tone, (Q)uit: ") #S(c)issors, Pa(p)er, (S)tone, (Quit)
    
    user_input = x.lower()
    if user_input in thisdict:
        print(f"You: {thisdict[user_input]}")
    
        machine = random.choice(mylist)
        if machine in thisdict:
            print(f"Machine: {thisdict[machine]}")
        if user_input == machine:
            print("Its a tie. Please try again\n")
        else:
            if user_input == 'c':
                if machine == 's':
                    print("you lose\n")
                else:
                    print("you win\n")
    
            if user_input == 'p':
                if machine == 'c':
                    print("you lose\n")
                else:
                    print("you win\n")
    
            if user_input == 's':
                if machine == 'p':
                    print("you lose\n")
                else:
                    print("you win\n")
    else:
        pass
