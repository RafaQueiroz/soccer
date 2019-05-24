import unittest
from src.app import App


class TestSortPlayer(unittest.TestCase):

    def test_add_player_succesfully(self):
        app = App()
        reponse = app.add_player('Rafael')

        self.assertTrue(reponse.ok)
        self.assertEqual('Rafael successfully added.', reponse.message)

        self.assertTrue('Rafael' in app.players)

    def test_add_None_player(self):
        app = App()
        response = app.add_player(None)

        self.assertFalse(response.ok)
        self.assertEqual('The player name can\'t be empty.', response.message)

    def test_add_player_duplicated(self):
        app = App()
        
        app.add_player('Rafael')
        reponse = app.add_player('Rafael')

        self.assertFalse(reponse.ok)
        self.assertEqual('Rafael already in the players list.', reponse.message)

    def test_remove_player_successfully(self):

        app = App()
        reponse = app.add_player('Rafael')
        response = app.remove_player('Rafael')

        self.assertTrue(reponse.ok)
        self.assertEqual('Rafael was succesfully removed.', response.message)

    def test_remove_empty_player(self):

        app = App()
        response = app.remove_player(None)

        self.assertFalse(response.ok)
        self.assertEqual('The player name can\'t be empty.', response.message)

    def test_remove_nonexistent_player(self):

        app = App()
        reponse = app.remove_player('Rafael')

        self.assertFalse(reponse.ok)
        self.assertEqual('Rafael not in the list', reponse.message)


    def test_list_three_players(self):
        app = App()

        app.add_player('Rafael')
        app.add_player('Simão')
        app.add_player('Rodrigo')

        response = app.list_players()

        self.assertTrue(response.ok)
        self.assertEqual(3, len(response.data['players']))

    def test_teams_distributions(self):
        app = App()

        app.add_player('Rafael')
        app.add_player('Simão')
        app.add_player('Rodrigo')
        app.add_player('Eduardo')

        response = app.distribute_teams()

        self.assertTrue(response.ok)
        self.assertEqual(2, len(response.data['teams'])