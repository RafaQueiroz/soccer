from datetime import datetime


class OpResponse:
    """
    Encapsulate the operation reponses.
    """
    def __init__(self, ok, message='', data={}):
        self.ok = ok
        self.message = message
        self.data = data


class Game:

    def __init__(self, max_players=None, game_date=None):
        self.max_players = max_players
        self.teams = []
        self.date = game_date
        self.players = []

    def sort_teams(self):
        """
        sort teams for the game.
        """

        for team in self.teams:
            if len(self.players) <= 0:
                break
            
            team.append(self.players.pop())
            
    def add_team(self, team):
        if team is None:
            raise ValueError("The team can't be None")

        if self.find_team(team) is not None:
            raise Exception(
                "There is already a team named {}".format(team.names))

        self.teams.append(team)

    


    def add_player(self, player):

        if player is None:
            raise ValueError("the player can't be None. ")

        if player in self.players:
            raise Exception("Player already in the list")
        
        if self.max_players and len(self.players) >= self.max_players:
            raise Exception(
                "The number of player for this game reached it's maximun.")

        self.players.append(player)

    def remove_by_name(self, player_name):

        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)

        raise Exception(
            "There is no player named {} in the list".format(player_name))

    def scores(self, team, player):
        self.find_team(team).scores(player)


        
class Team:

    def __init__(self, name):
        self.name = name
        self.players = []
        self.score = 0
        self.rate = 0

    def scores(self, player):
        self.score += 1
        self.find_player(player).scores()
    
    def find_player(self, player_filter):
        for player in self.players:
            if player.name == player_filter.name:
                return player

        raise ValueError(
            "There isn'r any player named {} in this team.".format(
                player_filter.name))


class Player:
    
    def __init__(self, name, posicao):
        self.name = name
        self.posicao = posicao
        self.gols = 0
        self.rate = 0

    def scores(self):
        self.gols += 1


class App:
    """
    Manage to sort teams for a soccer game
    """
    def __init__(self):
        self.players = []


    def add_player(self, name):
        """
        Add a player to the participants list to be sorted later.

        Keywords arguments:
        name -- Name of the player

        """

        if not name:
            return OpResponse(False, 'The player name can\'t be empty.' )

        if name in self.players:
            return OpResponse(False, '{} already in the players list.'.format(name) )

        self.players.append(name)
        return OpResponse(True, '{} successfully added.'.format(name))

    def remove_player(self, name):
        
        if not name:
            return OpResponse(False, 'The player name can\'t be empty.' )

        try:
            self.players.remove(name)
        except ValueError as erro:
            return OpResponse(False, '{} not in the list'.format(name))

        return OpResponse(True, '{} was succesfully removed.'.format(name))

    def list_players(self):
        return OpResponse(True, data={'players' : self.players})


    def distribute_teams(self):
        
        pass
    

