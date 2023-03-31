from random import randrange
import time

"""
Medium difficulty:
CPU does not make a previous guess
CPU placement is random
"""
class Medium:
    def __init__(self, board_length, board_width) -> None:
        self.board_length = board_length
        self.board_width = board_width
        self.guesses_made = []
        self.ship_locations = []
    
    """
    Medium difficulty move method
    """
    def cpu_move(self) -> list:
        while True:
            cpu_guess = self.generate_coordinates()
            if not self.is_previous_guess(cpu_guess):
                self.guesses_made.append(cpu_guess)
                break
        print('Thinking...')
        time.sleep(randrange(5))
        print('Let me try...')
        time.sleep(1)
        return cpu_guess
    
    """
    Medium piece placement
    """
    def cpu_piece_placement(self, number_of_pieces: int) -> None:
        number_of_pieces_count = number_of_pieces
        while number_of_pieces_count > 0:
            position = self.generate_coordinates()
            if position not in self.ship_locations:
                self.ship_locations.append(position)
                number_of_pieces_count = number_of_pieces_count - 1

    """
    Checks if random CPU choice was already made
    """
    def is_previous_guess(self, coordinates: list) -> bool:
        return coordinates in self.guesses_made

    """
    Returns coordinates within the game board
    """
    def generate_coordinates(self) -> list:
        return [randrange(self.board_length), randrange(self.board_width)]
    
    if __name__ == '__main__':
        pass