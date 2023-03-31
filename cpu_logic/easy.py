from random import randrange
import time

"""
Easy difficulty:
CPU does previous guesses, thus random mistakes
CPU placement is predictable pattern - start in top left and add pieces in-line from top to bottom
"""
class Easy:
    def __init__(self, board_length: int, board_width: int) -> None:
        self.board_length = board_length
        self.board_width = board_width
        self.ship_locations = []

    """
    Easy difficulty move method
    """
    def cpu_move(self) -> list:
        cpu_value = [randrange(self.board_length), randrange(self.board_width)]
        print('Thinking...')
        time.sleep(randrange(5))
        print('Let me try...')
        time.sleep(1)
        return cpu_value
    
    """
    Easy piece placement
    """
    def cpu_piece_placement(self, number_of_pieces: int) -> None:
        initial_spot = [0, 0]
        self.ship_locations.append(initial_spot)
        number_of_pieces_count = number_of_pieces - 1
        placement_x = 0
        placement_y = 1
        while number_of_pieces_count > 0:
            new_value = [placement_x, placement_y]
            if self.is_valid_placement(new_value):
                self.ship_locations.append(new_value)
                number_of_pieces_count = number_of_pieces_count - 1
                placement_y = placement_y + 1
            else:
                placement_x = placement_x + 1
                placement_y = 0

    """
    Check to see if valid placement on board
    """
    def is_valid_placement(self, placement: list) -> bool:
        if placement[0] < self.board_length and placement[1] < self.board_width:
            return True
        else:
            return False
        
    if __name__ == '__main__':
        pass