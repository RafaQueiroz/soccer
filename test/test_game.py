import app
import unittest


class TestGame(unittest.TestCase):

    def test_game_sort(self):

        game = new game()

        game.add_team(Team('Yelow'))
        game.add_team(Team('Blue'))

        game.add_player(Player('Rafael Queiroz'))
        game.add_player(Player('Simão'))
        game.add_player(Player('Douglas'))
        game.add_player(Player('Eduardo'))
        game.add_player(Player('Sidney'))
        game.add_player(Player('Carlos Machado'))

        game.sort_teams()

        game.scores('Yellow', 'Rafael Queiroz')
        game.scores('Yellow', 'Rafael Queiroz')
        game.scores('Blue', 'Eduardo')

        game.end()
        self.assertEqual('Yellow', game.winner)