"""
This program is to call class ConnectFour in connect_four.py.
"""


from connect_four import ConnectFour


def main():
    print("Let's start the game.")
    player = ConnectFour()
    print(player)
    while player.is_game_over() is False:
        print("Please choose a selection below:.")
        print("Number of column(1-7) to play")
        print("U -- Undo")
        print("Q -- Quit")
        command = input("->")
        while command not in ['Q', 'U', '1', '2', '3', '4', '5', '6', '0']:
            print(ValueError, "Please enter a valid command:")
            command = input()
        if command == 'Q':
            break
        elif command == 'U':
            player.undo()
            print(player)
        elif int(command) in [1, 2, 3, 4, 5, 6, 0]:
            player.add_piece(int(command))
            print(player)
        winner = player.get_winner()

    print("Game Over")
    print("Winner is", winner)


if __name__ == '__main__':
    main()
