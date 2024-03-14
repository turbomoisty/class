# def str_list_to_int_list(str_list):
#     n = 0
#     while n < len(str_list):
#         str_list[n] = int(str_list[n])
#         n += 1
#     return str_list
#
#
# results = ["1", "2", "3"]
#
# str_list_to_int_list(results)
# print(str_list_to_int_list(results))

n = 0
while n < 10:
    print("pen")
    n += 1

from random import randint

for _ in range(0,10):
    print(_ + 1)

def game():
    win_count = 0
    lose_count = 0
    draw_count = 0

    while True:
        print('%s wins, %s losses, %s draws' % (win_count, lose_count, draw_count))
        user_hand = input("Press 'r' for rock, 's' for scissor and 'p' for paper: ")
        cpu_hand = cpu_choice()
        if user_hand == 'r':
            print("Rock versus...", cpu_hand, "!")
            if cpu_hand == "Rock":
                print("Draw!")
                draw_count += 1
            elif cpu_hand == "Paper":
                print("you lose")
                lose_count += 1
            else:
                print("you win")
                win_count += 1

        elif user_hand == 's':
            print("Scissors versus...", cpu_hand, "!")
            if cpu_hand == "Scissor":
                print("Draw!")
                draw_count += 1
            elif cpu_hand == "Rock":
                print("you lose")
                lose_count += 1
            else:
                print("you win")
                win_count += 1

        else:
            print("Paper versus...", cpu_hand, "!")
            if cpu_hand == "Paper":
                print("Draw")
            elif cpu_hand == "Rock":
                print("you lose")
                lose_count += 1
            else:
                print("you win")
                win_count += 1


def cpu_choice():
    rps = randint(1, 3)
    if rps == 1:
        return "Rock"
    elif rps == 2:
        return "Scissor"
    else:
        return "Paper"


if __name__ == "__main__":
    game()
