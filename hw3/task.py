import random


class Player:

    def __init__(self, letter):
        self.letter = letter


class ComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        while not valid_square:
            if self.letter == "O":
                player = "Computer"
            else:
                player = "Human"

            square = input(player + " turn. Input move (0-8):")

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("The place is already occupied! Try again!")
        return val


class GameField:

    def __init__(self):
        self.board = [" " for i in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def print_num_board():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)]
                        for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_spots(self):
        return " " in self.board

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[(row_ind * 3):(row_ind * 3) + 3]
        print(row)
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        col = [self.board[col_ind + i * 3] for i in range(3)]
        print(col)
        if all([spot == letter for spot in col]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False


class Play:

    def play(game, player_1, player_2, print_game=True):
        letter = "X"
        while game.empty_spots():

            if letter == "O":
                square = player_2.get_move(game)
            else:
                square = player_1.get_move(game)

            if game.make_move(square, letter):
                if letter == "O":
                    player = "Computer"
                else:
                    player = "Human"

                if print_game:
                    print(player + f" makes a move to square{square}")
                    game.print_board()
                    print("")

                if game.current_winner:
                    if print_game:
                        print(player + " wins")
                    return letter

                letter = "O" if letter == "X" else "X"


if __name__ == "__main__":
    print(GameField.print_num_board())
    player_1 = HumanPlayer("X")
    player_2 = ComputerPlayer("O")
    game_field = GameField()
    Play.play(game_field, player_1=player_1, player_2=player_2)
    