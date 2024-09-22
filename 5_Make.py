'''
Complete the Team class implementation. For the instance method get_win_percentage(), the formula is:
wins / (wins + losses). Note: Use floating-point division.

For instance method print_standing(), output the win percentage of the team with two digits after the 
decimal point and whether the team has a winning or losing average. A team has a winning average if the 
win percentage is 0.5 or greater.

Ex: If the input is:

Broncos
13
3 
where Ravens is the team's name, 13 is the number of team wins, and 3 is the number of team losses, 
the output is:

Win percentage: 0.81
Congratulations, Team Broncos has a winning average!
Ex: If the input is:

Chiefs
4
13
the output is:

Win percentage: 0.24
Team Chiefs has a losing average.


'''

class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    # TODO: Define get_win_percentage()
    
    # TODO: Define print_standing()


if __name__ == "__main__":
    team = Team()
   
    user_name = input()
    user_wins = int(input())
    user_losses = int(input())
    
    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses
    
    team.print_standing()