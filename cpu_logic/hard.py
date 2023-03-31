from random import randrange
import time

"""
Hard difficulty:
CPU does not make a previous guess, CPU uses a method to finding player pieces
CPU placement is random
CPU has MUCH more confident responses to its guesses
"""
class Hard:
    def __init__(self, board_length: int, board_width: int) -> None:
        self.board_length = board_length
        self.board_width = board_width
        self.ship_locations = []
        self.columns_guessed = []
        self.prev_guess = []
        self.cpu_dialogue = ["Haha, I am getting closer.", "You won't last much longer.", "Something tells me you're bad at this game!", "Can you try harder?", "It is pointless for you to try, I AM GONNA WIN!"]

    """
    Hard difficulty move method
    """
    def cpu_move(self) -> list:
        print(self.generate_random_dialogue())
        time.sleep(randrange(5))
        print(self.generate_random_dialogue())
        time.sleep(1)
        if self.prev_guess == []:
            column_val = self.generate_random_col()
            self.prev_guess = [column_val, 0]
            self.columns_guessed.append(column_val)
            return self.prev_guess

        if self.prev_guess[1] + 1 > self.board_length - 1:
            while True:
                column_val = self.generate_random_col()
                if column_val not in self.columns_guessed:
                    self.prev_guess = [column_val, 0]
                    self.columns_guessed.append(column_val)
                    return self.prev_guess
        else:
            self.prev_guess = [self.prev_guess[0], self.prev_guess[1] + 1]
            return self.prev_guess

    """
    Hard piece placement
    """
    def cpu_piece_placement(self, number_of_pieces: int) -> None:
        number_of_pieces_count = number_of_pieces
        while number_of_pieces_count > 0:
            position = self.generate_coordinates()
            if position not in self.ship_locations:
                self.ship_locations.append(position)
                number_of_pieces_count = number_of_pieces_count - 1

    """
    Returns coordinates within the game board
    """
    def generate_coordinates(self) -> list:
        return [randrange(self.board_length), randrange(self.board_width)]

    """
    Generates a random dialogue for Hard mode
    """
    def generate_random_dialogue(self) -> str:
        return self.cpu_dialogue[randrange(len(self.cpu_dialogue) - 1)]
    
    """
    Generates a random columns to begin CPU guessing
    """
    def generate_random_col(self) -> int:
        return randrange(self.board_width - 1)
    
    if __name__ == '__main__':
        pass