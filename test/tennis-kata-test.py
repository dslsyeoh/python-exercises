#  Author Steven Yeoh
#  Copyright (c) 2019. All rights reserved.

import unittest
from exercises import tennis_kata


class MyTestCase(unittest.TestCase):

    def test_initial(self):
        player_1 = tennis_kata.Player("Player 1", 0)
        player_2 = tennis_kata.Player("Player 2", 0)
        self.assertEqual("all-love", tennis_kata.announce_score(player_1, player_2))

    def test_player_1_fifteen_love(self):
        player_1 = tennis_kata.Player("Player 1", 0)
        player_2 = tennis_kata.Player("Player 2", 0)
        player_1.win_ball()
        self.assertEqual("fifteen-love", tennis_kata.announce_score(player_1, player_2))

    def test_player_2_love_fifteen(self):
        player_1 = tennis_kata.Player("Player 1", 0)
        player_2 = tennis_kata.Player("Player 2", 0)
        player_2.win_ball()
        self.assertEqual("love-fifteen", tennis_kata.announce_score(player_1, player_2))

    def test_player_2_thirty_all(self):
        player_1 = tennis_kata.Player("Player 1", 0)
        player_2 = tennis_kata.Player("Player 2", 0)
        for x in range(0, 2):
            player_1.win_ball()
            player_2.win_ball()
        self.assertEqual("thirty-all", tennis_kata.announce_score(player_1, player_2))

    def test_player_1_forty_thirty_game_point(self):
        player_1 = tennis_kata.Player("Player 1", 0)
        player_2 = tennis_kata.Player("Player 2", 0)
        for x in range(0, 2):
            player_1.win_ball()
            player_2.win_ball()
        player_1.win_ball()
        self.assertEqual("forty-thirty\nPlayer 1 game point", tennis_kata.announce_score(player_1, player_2))

    def test_player_1_game_point(self):
        player_1 = tennis_kata.Player("Player 1", 0)
        player_2 = tennis_kata.Player("Player 2", 0)
        for x in range(0, 3):
            player_1.win_ball()
        self.assertEqual("forty-love\nPlayer 1 game point", tennis_kata.announce_score(player_1, player_2))

    def test_player_2_game_point(self):
        player_1 = tennis_kata.Player("Player 1", 0)
        player_2 = tennis_kata.Player("Player 2", 0)
        player_1.win_ball()
        for x in range(0, 3):
            player_2.win_ball()
        self.assertEqual("fifteen-forty\nPlayer 2 game point", tennis_kata.announce_score(player_1, player_2))

    def test_player_1_game(self):
        player_1 = tennis_kata.Player("Player 1", 0)
        player_2 = tennis_kata.Player("Player 2", 0)

        for x in range(0, 4):
            player_1.win_ball()
        self.assertEqual("Player 1 game", tennis_kata.announce_score(player_1, player_2))

    def test_player_2_game(self):
        player_1 = tennis_kata.Player("Player 1", 0)
        player_2 = tennis_kata.Player("Player 2", 0)

        for x in range(0, 4):
            player_2.win_ball()
        self.assertEqual("Player 2 game", tennis_kata.announce_score(player_1, player_2))

    def test_deuce(self):
        player_1 = tennis_kata.Player("Player 1", 0)
        player_2 = tennis_kata.Player("Player 2", 0)
        for x in range(0, 3):
            player_1.win_ball()
            player_2.win_ball()
        self.assertEqual("Deuce", tennis_kata.announce_score(player_1, player_2))

    def test_player_1_advantage(self):
        player_1 = tennis_kata.Player("Player 1", 0)
        player_2 = tennis_kata.Player("Player 2", 0)
        for x in range(0, 3):
            player_1.win_ball()
            player_2.win_ball()
        player_1.win_ball()
        self.assertEqual("Player 1 advantage", tennis_kata.announce_score(player_1, player_2))

    def test_player_2_advantage(self):
        player_1 = tennis_kata.Player("Player 1", 0)
        player_2 = tennis_kata.Player("Player 2", 0)
        for x in range(0, 3):
            player_1.win_ball()
            player_2.win_ball()
        player_2.win_ball()
        self.assertEqual("Player 2 advantage", tennis_kata.announce_score(player_1, player_2))

    def test_player_1_win_after_advantage(self):
        player_1 = tennis_kata.Player("Player 1", 0)
        player_2 = tennis_kata.Player("Player 2", 0)
        for x in range(0, 3):
            player_1.win_ball()
            player_2.win_ball()
        player_1.win_ball()
        self.assertEqual("Player 1 advantage", tennis_kata.announce_score(player_1, player_2))
        player_1.win_ball()
        self.assertEqual("Player 1 game", tennis_kata.announce_score(player_1, player_2))

    def test_player_1_advantage_then_deuce(self):
        player_1 = tennis_kata.Player("Player 1", 0)
        player_2 = tennis_kata.Player("Player 2", 0)
        for x in range(0, 3):
            player_1.win_ball()
            player_2.win_ball()
        player_1.win_ball()
        self.assertEqual("Player 1 advantage", tennis_kata.announce_score(player_1, player_2))
        player_2.win_ball()
        self.assertEqual("Deuce", tennis_kata.announce_score(player_1, player_2))

    def test_player_2_game_after_player_1_advantage(self):
        player_1 = tennis_kata.Player("Player 1", 0)
        player_2 = tennis_kata.Player("Player 2", 0)
        for x in range(0, 3):
            player_1.win_ball()
            player_2.win_ball()
        player_1.win_ball()
        self.assertEqual("Player 1 advantage", tennis_kata.announce_score(player_1, player_2))
        player_2.win_ball()
        player_2.win_ball()
        player_2.win_ball()
        self.assertEqual("Player 2 game", tennis_kata.announce_score(player_1, player_2))


if __name__ == '__main__':
    unittest.main()
