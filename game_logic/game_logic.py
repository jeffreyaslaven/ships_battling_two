from game_board.game_board import GameBoard
from cpu_logic import easy
from cpu_logic import medium
from cpu_logic import hard

"""
Core logic for Ships Battling
"""
class GameLogic:
    def __init__(self) -> None:
        pass

    def play_game(self, restart=False) -> bool:
        if restart:
            print ('Welcome back!')
            name = input('Could you remind what your name is? ')
        else:
            name = input('Hello there, what is your name? ')
            print("Hello " + name)

        while True:
            play_game = input('Want to play a game of \"Ships Battling\"? Type \"Y\" for Yes and \"N\" for No: ')
            if play_game.lower() == 'n':
                print('Well okay, ' + name + ', bye for now!')
                break
            elif play_game.lower() == 'y':
                break
            else:
                print('Sorry, I do not understand your input.')

        """
        Creating the player board and gathering information from the user
        """
        if play_game.lower() == 'y':
            while True:
                how_tall = input('Great to hear! How tall do you want the board?: ')
                if how_tall.isdigit():
                    break
                else:
                    print('Not a valid height, please enter a valid number.')
            while True:
                how_wide = input('How wide do you want the board?: ')
                if how_wide.isdigit():
                    break
                else:
                    print('Not a valid width, please enter a valid number.')
            
            game = GameBoard(int(how_tall), int(how_wide))
            game.create_board()

            game_piece = input('Now it is time to add your game pieces. Please enter your pieces in coordinate format i.e. x, y: ')

            while True:
                try:
                    game_piece_val = game_piece.strip()
                    game_piece_val = game_piece_val.split(',')
                    x_val = int(game_piece_val[0]) - 1
                    y_val = int(game_piece_val[1]) - 1
                    game.add_piece(x_val, y_val)
                    game_piece = input('Please enter another piece in coordinate format i.e. x, y or type "start" to begin: ')
                except IndexError:
                    game_piece = input('You entered an location outside of the board. Please enter another piece in coordinate format i.e. x, y or type "start" to begin: ')
                except Exception as e:
                    if game_piece.lower() == 'start':
                        break
                    game_piece = input('That is not a valid input. Please enter your pieces in coordinate format i.e. x, y or type "start" to begin: ')

            """
            Gathering information on how many 'boats' the CPU player should have
            """
            while True:
                cpu_boats = input('How many boats do you want me to have?: ')
                if cpu_boats.isdigit():
                    if int(cpu_boats) > int(how_wide) * int(how_tall):
                        cpu_boats = input('Invalid value. You entered a number larger than what is possible on the board. How many boats do you want me to have?: ')
                    else:
                        break
                print('Invalid value. Please enter a valid number.')
            
            print('Great! I will have ' + cpu_boats + ' boats. Let me place them on my board.')

            """
            Selecting CPU difficulty
            """
            while True:
                cpu_difficulty = input('What difficulty do you want for your game? Valid options are "easy", "medium", "hard": ')
                if cpu_difficulty.lower() == 'easy':
                    cpu_player = easy.Easy(int(how_tall), int(how_wide))
                    cpu_player.cpu_piece_placement(int(cpu_boats))
                    break
                elif cpu_difficulty.lower() == 'medium':
                    cpu_player = medium.Medium(int(how_tall), int(how_wide))
                    cpu_player.cpu_piece_placement(int(cpu_boats))
                    break
                elif cpu_difficulty.lower() == 'hard':
                    cpu_player = hard.Hard(int(how_tall), int(how_wide))
                    cpu_player.cpu_piece_placement(int(cpu_boats))
                    break
                else:
                    print('Invalid input.')

            """
            Creating the CPU board
            """
            cpu_game = GameBoard(int(how_tall), int(how_wide))
            cpu_game.create_board(True)
            tracking_board_cpu = GameBoard(int(how_tall), int(how_wide))
            tracking_board_cpu.create_board(True, True)

            """
            Placing specified number of CPU boats on the board
            """
            for position in cpu_player.ship_locations:
                cpu_game.add_piece(position[0], position[1], True)
            

            print('Let the games begin!')
            print('Just a reminder, this your board:')
            game.print_game_board()

            print('__________________________________________________')
            print('\n')

            tracking_board = GameBoard(int(how_tall), int(how_wide))
            tracking_board.create_board(True, True)

            """
            Checks game state of both boards to see if the game is over
            """
            def check_if_game_over() -> bool:
                if game.is_game_over() is True:
                    print('You lose! Try again')
                    return True
                elif cpu_game.is_game_over() is True:
                    print('You win!')
                    return True
                else:
                    return False
            
            """
            Start the battle between the CPU and player
            """
            while True:
                if check_if_game_over():
                    break
                user_turn = input('Your turn - enter a coordinate in coordinate format i.e. x,y: ')
                try:
                    user_turn_val = user_turn.strip()
                    user_turn_val = user_turn_val.split(',')
                    x_val = int(user_turn_val[0]) - 1
                    y_val = int(user_turn_val[1]) - 1
                    cpu_game.attack_piece(x_val, y_val)
                    tracking_board.add_tracker(x_val, y_val)
                except IndexError:
                    print('You entered an location outside of the board. Lose a turn!') 
                except Exception:
                    print('You entered an invalid value. Lose a turn!') 
                print('__________________________________________________')
                if check_if_game_over():
                    break
                cpu_value = cpu_player.cpu_move()
                game.attack_piece(cpu_value[0], cpu_value[1], True)
                print('What I have tried:')
                tracking_board_cpu.add_tracker(cpu_value[0], cpu_value[1])
                print('__________________________________________________')
        
        """
        Check to see if the player wants restart the game
        """
        while True:
            player_decision = input('Do you want to play again? "Y" for yes, "N" for no: ')
            if player_decision.lower() != 'y' and player_decision.lower() != 'n':
                print('Invalid input. Please enter "Y" for yes or "N" for no.')
            elif player_decision.lower() == 'y':
                return True
            else:
                return False
        
if __name__ == '__main__':
    pass        