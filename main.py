from game_logic.game_logic import GameLogic
  
def main() -> None:
    play_ships_battling = GameLogic()
    keep_playing_game = True
    has_user_restart = False
    while True:
        if keep_playing_game:
            keep_playing_game = play_ships_battling.play_game(has_user_restart)
            has_user_restart = True
        else:
            break


if __name__ == '__main__':
    main()
    print('____________________')
    print('\n')
    print('Thanks for playing!')
    print('Created By: Jeffrey Slaven')
    print('\n')
    print('____________________')