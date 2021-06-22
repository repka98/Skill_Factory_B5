
board = list(range(1,10))

def draw_board(board):

   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")


def take_input(player_token):
    valid_input = False

    while not valid_input:
        player_answer = input(player_token)

        try:
            player_answer = int(player_answer)
        except:
            print("некорректно")
            continue


        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer - 1]) not in "X0"):
                board[player_answer - 1] = player_token
                valid_input = True
            else:
                print("уже занята")

        else:
            print("некоректный ввод")

def check_winner(board):
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_combinations:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False


def main(board):
    counter = 0

    win = False

    while not win:

        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("0")
        counter += 1

        if counter > 4:
            win_player = check_winner(board)
            if win_player:
                print("Победил!")
                win = True
                break

        if counter == 9:
            print("Ничья.")
            break

    draw_board(board)

main(board)

