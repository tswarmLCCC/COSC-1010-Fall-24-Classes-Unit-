'''
Instructions  

Complete the Team class implementation. For the instance method get_win_percentage(), the formula is:
wins / (wins + losses). Note: Use floating-point division.

For instance method print_standing(), output the win percentage of the team with two digits after the decimal point and whether the team has a winning or losing average. A team has a winning average if the win percentage is 0.5 or greater.

Ex: If the input is:

Ravens
13
3 
where Ravens is the team's name, 13 is the number of team wins, and 3 is the number of team losses, the output is:

Win percentage: 0.81
Congratulations, Team Ravens has a winning average!
Ex: If the input is:

Angels
80
82
the output is:

Win percentage: 0.49
Team Angels has a losing average.

Then, Loop through at least 3 teams and have the user input their statistics
These should be stored (probably in a list)

Finally, loop through those collected teams and use their print method to display the standings
'''
class Team:

  def __init__(self):
    self.name = 'none'
    self.wins = 0
    self.losses = 0

  # Define get_win_percentage()
  def get_win_percentage(self):
    wins = float(self.wins)
    return wins / (wins + float(self.losses))

  # Define print_standing()
  def print_standing(self):
    win_percentage = self.get_win_percentage()
    print(f'Win percentage: {win_percentage:.2f}')
    if win_percentage >= 0.5:
      print(f'Congratulations, Team { self.name } has a winning average!')
    else:
      print(f'Team { self.name } has a losing average.')


if __name__ == "__main__":

  leagueTeams = []
  numberOfTeams = 5
  for i in range(numberOfTeams):

    team = Team()

    user_name = input(f"Input Team Name Number {i}: ")
    user_wins = int(input(f"Input the number of wins for {user_name}: "))
    user_losses = int(input(f"Input the number of losses for {user_name}: "))

    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses

    leagueTeams.append(team)

  for i in range(numberOfTeams):
    leagueTeams[i].print_standing()
