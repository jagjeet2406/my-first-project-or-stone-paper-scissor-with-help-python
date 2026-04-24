import random 
choices=["stone","paper","scissors"]
def get_computer_choice():
    return random.choice(choices)
def decide_winner(user,computer):
    if user==computer:
        return "draw" 
    elif(user=="stone" and computer =="scissors") or \
         (user=="paper"and computer=="stone") or \
         ( user=="scissors"and computer=="paper"):
        return "user"
    else:
        return "computer"
        



                     

