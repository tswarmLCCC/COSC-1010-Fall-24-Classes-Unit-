class Team:

   def __init__(self):

       self.team_name = 'none'

       self.team_wins = 0

       self.team_losses = 0

   # TODO: Define        

   def get_win_percentage(self):

       return self.team_wins / (self.team_wins + self.team_losses)

   

if __name__ == "__main__":

   team = Team()

   team_name = input()

   team_wins = int(input())

   team_losses = int(input())

   team.team_name=team_name

   team.team_wins=team_wins

   team.team_losses=team_losses

   if team.get_win_percentage() >= 0.5:

       print('Congratulations, Team', team.team_name,'has a winning average!')

   else:

       print('Team', team.team_name, 'has a losing average.')
'''
Note that

def get_win_percentage(self):

The above defines the function

While

return self.team_wins / (self.team_wins + self.team_losses)

This calculates the win percentage and returns it to the main.

What is a  function?
A function is essentially a "chunk" of code that you may reuse instead of writing it out several times. Programmers can use functions to break down or breakdown an issue into smaller segments, each of which performs a specific purpose.

Instance methods are methods that require the creation of an object of the class before they may be invoked. To call an instance method, we must first construct an Object of the class that defines the method.

'''