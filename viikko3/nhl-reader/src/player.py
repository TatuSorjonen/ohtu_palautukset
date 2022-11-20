import requests

class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.pisteet = goals + assists
    
    def __str__(self):
        return f'{self.name:20} {self.team} {self.goals} + {self.assists} = {self.pisteet}'
        
        
class PlayerReader:
    def __init__(self, url):
        self.reader = requests.get(url).json()
        
    def get_players(self):
        return self.reader


class PlayerStats:
    def __init__(self, player_list):
        self.player_list = player_list.get_players()

    def top_scorers_by_nationality(self, nationality):

        players = []

        for player_dict in self.player_list:
            player = Player(
                player_dict['name'], player_dict['team'], player_dict['goals'], player_dict['assists']
            )
            if player_dict['nationality'] == nationality:
                players.append(player)
                
        players = sorted(players, key=lambda players: players.pisteet, reverse = True)

        return players
