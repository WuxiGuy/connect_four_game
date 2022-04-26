"""
Yuhao Hua
2022 Apr 8
CS5001, Spring 2022
Homework 7 - Connect Four

This program is to test all the functions
in class ConnectFour of connect_four.py.
"""


import unittest

import random

from connect_four import ConnectFour


class ConnectFourTest(unittest.TestCase):

    def test_init(self):
        expected = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        test_player = ConnectFour()
        actual = test_player.board
        self.assertEqual(actual, expected,
                         "The list of the positions is wrong.")

    def test_add_piece_wrong_number(self):
        try:
            test_player = ConnectFour()
            test_player.add_piece(8)
        except ValueError:
            pass

    def test_add_piece_full_column(self):
        try:
            test_player = ConnectFour()
            test_player.board = [['X', ' ', ' ', ' ', ' ', ' ', ' '],
                                 ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                                 ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                                 ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                                 ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                                 ['X', ' ', ' ', ' ', ' ', ' ', ' ']]
            test_player.add_piece(0)
        except ValueError:
            pass

    def test_add_piece_game_over(self):
        try:
            test_player = ConnectFour()
            test_player.board = [['X', 'O', 'X', 'X', 'X', 'O', 'X'],
                                 ['O', 'O', 'X', 'O', 'X', 'O', 'X'],
                                 ['X', 'O', 'X', 'O', 'O', 'X', 'O'],
                                 ['O', 'X', 'O', 'X', 'X', 'O', 'O'],
                                 ['X', 'X', 'O', 'O', 'O', 'X', 'X'],
                                 ['X', 'O', 'X', 'X', 'X', 'O', 'X']]
            test_player.add_piece(1)
        except ValueError:
            pass

    def test_add_piece_board(self):
        test_player = ConnectFour()
        test_player.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', ' ', ' ', ' ', ' ', ' ', ' ']]
        test_player.piece_type = ['O', 'X']
        test_player.piece = 'X'
        board, piece, piece_type, position = test_player.add_piece(2)
        expected = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['X', ' ', 'O', ' ', ' ', ' ', ' ']]
        actual = board
        self.assertEqual(actual, expected,
                         "The piece wasn't put on the right place.")

    def test_add_piece_piece(self):
        test_player = ConnectFour()
        test_player.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', ' ', ' ', ' ', ' ', ' ', ' ']]
        test_player.piece_type = ['O', 'X']
        test_player.piece = 'X'
        board, piece, piece_type, position = test_player.add_piece(2)
        expected = 'O'
        actual = piece
        self.assertEqual(actual, expected,
                         "Did not give right piece type.")

    def test_add_piece_piece_type(self):
        test_player = ConnectFour()
        test_player.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', ' ', ' ', ' ', ' ', ' ', ' ']]
        test_player.piece_type = ['O', 'X']
        test_player.piece = 'X'
        board, piece, piece_type, position = test_player.add_piece(2)
        expected = ['X', 'O']
        actual = piece_type
        self.assertEqual(actual, expected,
                         "Did not give right order of piece in a queue.")

    def test_add_piece_position(self):
        test_player = ConnectFour()
        test_player.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', ' ', ' ', ' ', ' ', ' ', ' ']]
        test_player.piece_type = ['O', 'X']
        test_player.piece = 'X'
        board, piece, piece_type, position = test_player.add_piece(2)
        expected = [5, 2]
        actual = position
        self.assertEqual(actual, expected,
                         "Did not give right coordinate of the position.")

    def test_is_game_over_get_winner(self):
        test_player = ConnectFour()
        test_player.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', 'X', 'X', 'X', 'O', ' ', ' ']]
        test_player.piece = 'X'
        test_player.position = [5, 3]
        test_player.get_winner()
        actual = test_player.is_game_over()
        self.assertTrue(actual, "Did not finish when get winner")

    def test_is_game_over_full_board(self):
        test_player = ConnectFour()
        test_player.board = [['X', 'O', 'X', 'X', 'X', 'O', 'X'],
                             ['O', 'O', 'X', 'O', 'X', 'O', 'X'],
                             ['X', 'O', 'X', 'O', 'O', 'X', 'O'],
                             ['O', 'X', 'O', 'X', 'X', 'O', 'O'],
                             ['X', 'X', 'O', 'O', 'O', 'X', 'X'],
                             ['X', 'O', 'X', 'X', 'X', 'O', 'X']]
        actual = test_player.is_game_over()
        self.assertTrue(actual, "Did not finish when get winner")

    def test_is_game_over_notfull(self):
        test_player = ConnectFour()
        test_player.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['O', 'O', 'O', 'O', ' ', ' ', ' '],
                             ['X', 'O', 'X', 'X', 'X', ' ', ' ']]
        actual = test_player.is_game_over()
        self.assertFalse(actual, "Did not finish when get winner")

    def test_get_winner_vertical_winnerX(self):
        test_player = ConnectFour()
        test_player.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', 'O', ' ', ' ', ' ', ' ', ' '],
                             ['X', 'O', 'X', 'O', ' ', ' ', ' '],
                             ['X', 'O', 'O', 'X', ' ', ' ', ' ']]
        test_player.piece = 'X'
        test_player.position = [2, 0]
        expected = 'X'
        actual = test_player.get_winner()
        self.assertEqual(actual, expected, "Did not get the right winner")

    def test_get_winner_horizontal_winnerO(self):
        test_player = ConnectFour()
        test_player.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', 'X', 'O', ' ', ' ', ' ', ' '],
                             ['X', 'O', 'O', 'O', 'O', ' ', ' '],
                             ['X', 'O', 'X', 'X', 'X', ' ', ' ']]
        test_player.piece = 'O'
        test_player.position = [4, 4]
        expected = 'O'
        actual = test_player.get_winner()
        self.assertEqual(actual, expected, "Did not get the right winner")

    def test_get_winner_leftupoblique_winnerX(self):
        test_player = ConnectFour()
        test_player.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                             ['X', 'X', 'O', ' ', ' ', ' ', ' '],
                             ['X', 'O', 'X', 'O', 'O', ' ', ' '],
                             ['X', 'O', 'O', 'X', 'O', ' ', ' ']]
        test_player.piece = 'X'
        test_player.position = [2, 0]
        expected = 'X'
        actual = test_player.get_winner()
        self.assertEqual(actual, expected, "Did not get the right winner")

    def test_get_winner_rightupoblique_winnerO(self):
        test_player = ConnectFour()
        test_player.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', 'O', ' ', ' ', ' '],
                             ['X', 'X', 'O', 'X', ' ', ' ', ' '],
                             ['X', 'O', 'X', 'O', ' ', ' ', ' '],
                             ['O', 'O', 'X', 'X', 'O', ' ', ' ']]
        test_player.piece = 'O'
        test_player.position = [2, 3]
        expected = 'O'
        actual = test_player.get_winner()
        self.assertEqual(actual, expected, "Did not get the right winner")

    def test_get_winner_no_winner(self):
        test_player = ConnectFour()
        test_player.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', 'O', ' ', ' ', ' '],
                             ['X', 'O', 'X', 'X', ' ', ' ', ' '],
                             ['X', 'O', 'X', 'O', ' ', ' ', ' '],
                             ['O', 'O', 'X', 'X', 'O', ' ', ' ']]
        test_player.piece = 'O'
        test_player.position = [2, 3]
        expected = None
        actual = test_player.get_winner()
        self.assertEqual(actual, expected, "Did not get the right winner")

    def test_undo_rboard(self):
        test_player = ConnectFour()
        test_player.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', 'O', ' ', ' ', ' '],
                             ['X', 'O', 'X', 'X', ' ', ' ', ' '],
                             ['X', 'O', 'X', 'O', ' ', ' ', ' '],
                             ['O', 'O', 'X', 'X', 'O', ' ', ' ']]
        test_player.piece = 'O'
        test_player.position = [2, 3]
        board, piece_type = test_player.undo()
        expected = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['X', 'O', 'X', 'X', ' ', ' ', ' '],
                    ['X', 'O', 'X', 'O', ' ', ' ', ' '],
                    ['O', 'O', 'X', 'X', 'O', ' ', ' ']]
        actual = board
        self.assertEqual(actual, expected,
                         "Did not return to previous board.")

    def test_undo_piece_type(self):
        test_player = ConnectFour()
        test_player.board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                             [' ', ' ', ' ', 'O', ' ', ' ', ' '],
                             ['X', 'O', 'X', 'X', ' ', ' ', ' '],
                             ['X', 'O', 'X', 'O', ' ', ' ', ' '],
                             ['O', 'O', 'X', 'X', 'O', ' ', ' ']]
        test_player.piece = 'O'
        test_player.position = [2, 3]
        board, piece_type = test_player.undo()
        expected = ['O', 'X']
        actual = piece_type
        self.assertEqual(actual, expected,
                         "Did not return to previous order of piece.")

    def test_undo_no_return(self):
        try:
            test_player = ConnectFour()
            test_player.undo()
        except ValueError:
            pass

    def test_str_(self):
        test_player = ConnectFour()
        expected = "| | | | | | | |\n---------------\n| | | | | | | |\n" \
                   "---------------\n| | | | | | | |\n---------------\n" \
                   "| | | | | | | |\n---------------\n| | | | | | | |\n" \
                   "---------------\n| | | | | | | |\n---------------\n"
        actual = test_player.__str__()
        self.assertEqual(actual, expected,
                         "Something wrong to print board.")
