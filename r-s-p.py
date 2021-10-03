import random

def play():
    user = input('What is your choice ?! "r" for rock, "s" for scissor and "p" for paper\n ')
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "It is tie"

    if is_win(user,computer):
        return 'You won!'

    return "you lost!"   


def is_win(player, opponent):
    if (player =='s' and opponent == 'p') or (player == 'p'and opponent == 'r')\
        or (player == 'r' and opponent == 's'):
        return True 

instance = play()
print (instance)