import random
thisdict =	{
  "c": "Scissor",
  "p": "Paper",
  "s": "Stone"
}
mylist = ['c', 'p', 's'] 
user_input, x, y, it_is = '', '', '', True #initialize
user_score, machine_score = 0, 0

while it_is: #loop if user input has no value but encounter error if user enters string
    y = input("How many rounds: ")
    try:
        int(y)
        it_is = False
        sessions = int(y) #force code to take it as int
    except ValueError:
        it_is = True

while user_input != 'q' and x != '\n' and sessions != 0:
    x = input("S(c)issors, Pa(p)er, (S)tone, (Q)uit: ") #S(c)issors, Pa(p)er, (S)tone, (Quit)
    
    user_input = x.lower()
    if user_input in thisdict:
        print(f"You: {thisdict[user_input]}")
    
        machine = random.choice(mylist) #pick c, p or s from mylist
        if machine in thisdict:
            print(f"Machine: {thisdict[machine]}")
        if user_input == machine:
            print("\nIts a tie. Please try again\n")
        else:
            if user_input == 'c':
                if machine == 's':
                    print("you lose\n")
                    machine_score += 1
                else:
                    print("you win\n")
                    user_score += 1
    
            if user_input == 'p':
                if machine == 'c':
                    print("you lose\n")
                    machine_score += 1
                else:
                    print("you win\n")
                    user_score += 1
    
            if user_input == 's':
                if machine == 'p':
                    print("you lose\n")
                    machine_score += 1
                else:
                    print("you win\n")
                    user_score += 1
                    
        sessions -= 1 # sessions deduct by 1 each round
        if sessions == 0:
            if user_score > machine_score:
                print(f"You win after {user_score}")
            if user_score < machine_score:
                print(f"Machine win after {machine_score} round")
            else:
                print(f"\nYou: {user_score}, Machine: {machine_score}. It's a tie")
    else:
        pass #loops until user input define character
