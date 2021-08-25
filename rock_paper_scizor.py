import random
import math

def play():
    user=input("Whats ur choice? 'r'for rock,'p' for paper, 's' for scissors\n ")
    user=user.lower()

    computer =random.choice(['r','p','s'])

    if user==computer:
        #return 'You and the computer have both chosen {} ,Its a tie'.format(computer)
        return (0,user,computer)
    #r > s, p > r, s > p
    if is_win(user,computer):
        #return "You have chosen {} and computer has chosen {}. You won".format(user,computer)
        return (1,user,computer)
    #return 'You have chosen {} and computer has chosen {}. You Lost'.format(user,computer)
    return (-1,user,computer)
def is_win(player,opponent):
    #return true if player wins against the opponent
    #Wining conditon r > s, p > r, s > p
    if (player =='r' and opponent == 's') or (player =='p'and opponent =='r') or (player == 's' and opponent == 'p'):
        return True
    return False

def play_best_of(n):
    #play against the computer untill someone wins best of n games
    player_wins=0
    computer_win=0
    wins_necessary=math.ceil(n/2)
    while player_wins < wins_necessary and computer_win < wins_necessary:
        result,user,computer= play()
        if result==0:
            print('Its a tie.You and the computer has both chosen {}. \n'.format(user))
        elif result==1:
            player_wins+=1
            print('You Won .You chose {} and computer chose {}. \n'.format(user,computer))
        else:
            computer_win+=1
            print('You Lost.You chose {} and computer chose {}. \n'.format(user,computer))
        
    
    if player_wins > computer_win:
        print('You have won the best of {}  games!'.format(n))
    else:
        print('You Lost.Computer wins the best of {}'.format(n))


if __name__=='__main__':
   play_best_of(3)