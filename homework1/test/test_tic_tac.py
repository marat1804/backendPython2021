"""
Test for Tic Tac Toe Game
"""

from homework1.tic_tac import TicTacGame, PlayerWinException, IndexIsBusyException, \
    WrongInputException, NotDigitInputException
import pytest


class TestTicTac:
    """
    Test class for Tic Tac Toe
    """
    @staticmethod
    def test_turns():
        """
        Test for right placing user input
        """
        game = TicTacGame('', '')

        user_choice = '1'
        game.validate_input(user_choice)
        assert game.board[1] == 'x'

        user_choice = '0'
        game.validate_input(user_choice)
        assert game.board[0] == 'o'

    @staticmethod
    def test_names():
        """
        Test init with names
        """
        game = TicTacGame('', 'Name')

        assert game.player1 == 'Player 1'
        assert game.player2 == 'Name'

    @staticmethod
    def test_x_col_win():
        """
        Test x win column
        """
        game = TicTacGame('', '')

        game.validate_input('0')
        assert game.board[0] == 'x'
        game.validate_input('1')
        assert game.board[1] == 'o'
        game.validate_input('3')
        assert game.board[3] == 'x'
        game.validate_input('2')
        assert game.board[2] == 'o'
        with pytest.raises(PlayerWinException):
            game.validate_input('6')
        assert game.board[6] == 'x'

    @staticmethod
    def test_o_diag_win():
        """
        Test o win diagonal
        """
        game = TicTacGame('', '')

        game.validate_input('1')
        assert game.board[1] == 'x'
        game.validate_input('0')
        assert game.board[0] == 'o'
        game.validate_input('2')
        assert game.board[2] == 'x'
        game.validate_input('4')
        assert game.board[4] == 'o'
        game.validate_input('5')
        assert game.board[5] == 'x'
        with pytest.raises(PlayerWinException):
            game.validate_input('8')
        assert game.board[8] == 'o'

    @staticmethod
    def test_x_row_win():
        """
        Test x row win
        """
        game = TicTacGame('', '')

        game.validate_input('0')
        assert game.board[0] == 'x'
        game.validate_input('4')
        assert game.board[4] == 'o'
        game.validate_input('2')
        assert game.board[2] == 'x'
        game.validate_input('3')
        assert game.board[3] == 'o'
        with pytest.raises(PlayerWinException):
            game.validate_input('1')
        assert game.board[1] == 'x'

    @staticmethod
    def test_draw():
        """
        Test draw
        """
        game = TicTacGame('', '')

        game.validate_input('0')
        assert game.board[0] == 'x'
        game.validate_input('4')
        assert game.board[4] == 'o'
        game.validate_input('8')
        assert game.board[8] == 'x'
        game.validate_input('5')
        assert game.board[5] == 'o'
        game.validate_input('3')
        assert game.board[3] == 'x'
        game.validate_input('6')
        assert game.board[6] == 'o'
        game.validate_input('2')
        assert game.board[2] == 'x'
        game.validate_input('1')
        assert game.board[1] == 'o'
        assert game.is_not_ended()
        game.validate_input('7')
        assert game.board[7] == 'x'
        assert not game.is_not_ended()

    @staticmethod
    def test_wrong_input():
        """
        Test all exceptions with user input
        """
        game = TicTacGame('', '')

        game.validate_input('0')
        assert game.board[0] == 'x'

        with pytest.raises(IndexIsBusyException):
            game.validate_input('0')
        with pytest.raises(WrongInputException):
            game.validate_input('22')
        with pytest.raises(NotDigitInputException):
            game.validate_input('a')
