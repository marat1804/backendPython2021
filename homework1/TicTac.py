class NotDigitInputException(Exception):
    pass


class WrongInputException(Exception):
    pass


class PlayerWinException(Exception):
    pass


class IndexIsBusyException(Exception):
    pass


class TicTacGame:
    def __init__(self, name_1, name_2):
        self.player1 = name_1 if name_1 != '' else 'Player 1'
        self.player2 = name_2 if name_2 != '' else 'Player 2'
        self.board = [' ' for _ in range(9)]
        self.turn = 0

    def get_user_move(self):
        name = self.player2 if self.turn else self.player1
        place = 'o' if self.turn else 'x'
        print(f'Your turn, {name} - {place} -> ', end='')
        return input()

    def is_player_win(self):
        search = 'o' if self.turn else 'x'
        if self.board[:3].count(search) == 3:
            raise PlayerWinException
        elif self.board[3:6].count(search) == 3:
            raise PlayerWinException
        elif self.board[6:].count(search) == 3:
            raise PlayerWinException
        elif self.board[0] == self.board[3] == self.board[6] == search:
            raise PlayerWinException
        elif self.board[1] == self.board[4] == self.board[7] == search:
            raise PlayerWinException
        elif self.board[2] == self.board[5] == self.board[8] == search:
            raise PlayerWinException
        elif self.board[0] == self.board[4] == self.board[8] == search:
            raise PlayerWinException
        elif self.board[2] == self.board[4] == self.board[6] == search:
            raise PlayerWinException

    def make_turn(self, index):
        self.board[index] = 'o' if self.turn else 'x'
        self.is_player_win()
        self.turn = not self.turn

    def is_not_ended(self):
        if self.board.count(' ') == 0:
            return 0
        return 1

    def print_board(self):
        for i in range(9):
            place = self.board[i] if self.board[i] != ' ' else i
            if i % 3 != 2:
                print(' ', place, ' |', end='')
            else:
                print(' ', place, end='\n')
                if i != 8:
                    print('------------------')

    def start_game(self):
        while self.is_not_ended():
            self.print_board()
            user_input = self.get_user_move()
            try:
                if not user_input.isdigit():
                    raise NotDigitInputException
                index = int(user_input)
                if index > 9 or index < 0:
                    raise WrongInputException
                if self.board[index] != ' ':
                    raise IndexIsBusyException
                self.make_turn(index)
            except NotDigitInputException:
                print('Your input is not a digit, please enter 0 to 8')
                continue
            except WrongInputException:
                print('Your input is wrong')
                continue
            except IndexIsBusyException:
                print("This cell is busy!")
                continue
            except PlayerWinException:
                name = self.player2 if self.turn else self.player1
                place = 'o' if self.turn else 'x'
                print(f'{name} - {place} wins!')
                self.print_board()
                return
        print("It's a draw!")


if __name__ == '__main__':
    name1 = input('Player 1 enter a name, if default press enter -> ')
    name2 = input('Player 2 enter a name, if default press enter -> ')
    game = TicTacGame(name1, name2)
    game.start_game()
