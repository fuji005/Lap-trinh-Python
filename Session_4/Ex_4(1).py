def game_level():
    print("\n-----GUESSING NUMBER-----")
    print("1. Easy - 9 times")
    print("2. Medium - 6 times")
    print("3. Hard - 4 times")
    level = 1
    while True:
        level = int(input("Your choice: "))
        if 1 <= level <= 3:
            break
        else: print("Please just enter one of the provided levels!")
    return 9 if level == 1 else 6 if level == 2 else 4

import random

def game():
    is_win = False
    guess_num = 0
    num = random.randint(1,100)
    level = game_level()
    x = 0
    for x in range(level):
        guess_num = int(input("Enter your number: "))
        if guess_num == num:
            print("Congratulation!! It's a correct number.")
            is_win = True
            break
        if guess_num > num:
            print("The answer is smaller")
        if guess_num < num:
            print("The answer is bigger")
    if x == level-1:
        print(f"\nPoor you. The correct answer is: {num}")
    return is_win

if __name__ == "__main__":
    count_play = 0
    win_count = 0

    while True:
        game_engine = game()
        count_play += 1
        if game_engine:
            win_count += 1
        continue_playing = input("Continue playing game?(Y/N): ").lower()
        if continue_playing == "n":
            break
    print(f"\nSo lan choi: {count_play}")
    print(f"So lan choi dung: {win_count}")

