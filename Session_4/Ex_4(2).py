import random


def set_game_value():
    dice_1 = 2#random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    sum = dice_1 + dice_2
    if sum == 5:
        print(f"\nThe result is {sum} - No hu!")
    else: print(f"\nThe result is {sum}")
    return 1 if sum > 5 else 3 if sum == 5 else 2

def game_engine(choice):
    is_win = False
    result = set_game_value()
    if result == 3:
        return "Nohu"
    if choice == result:
        is_win = True
        return is_win
    else:
        is_win = False
        return is_win

if __name__ == "__main__":
    player_money = 100
    bet = 0
    count_play = 0
    count_win = 0

    while player_money > 0:
        print("\n-----GAME TAI XIU-----")
        print("1. Tai")
        print("2. Xiu")
        print("3. No hu")
        print(f"Your money: {player_money}")
        while True:
            player_choice = int(input("\nEnter your game choice: "))
            if player_choice > 3:
                print("Please just enter those options above")
            else: break
        while True:
            bet = int(input("How much money do you want to bet?: "))
            if bet > player_money:
                print("Not enough money\n")
            else:
                break

        game = game_engine(player_choice)
        count_play += 1
        if player_choice == 3:
            if game != "Nohu":
                print(f"You lose {bet * 3}!!")
                player_money = player_money - bet * 3
        if game == "Nohu":
            if player_choice == 1:
                print(f"Poor! You lose {bet}")
                player_money -= bet
            elif player_choice == 2:
                print(f"Congratulations! You earn {bet}")
                player_money += bet
                count_win += 1
            elif player_choice == 3:
                print(f"Excellent! You earn {bet*3}")
                player_money = player_money + bet*3
                count_win += 1
        if game == True:
            print(f"Congratulations! You earn {bet}")
            player_money += bet
            count_win += 1
        elif game == False:
            print(f"Poor! You lose {bet}")
            player_money -= bet

        continue_playing = input("Do you want to continue(Y/N)?: ").lower()
        if continue_playing == "y":
            count_play += 1
        if continue_playing == "n":
            break

    print("\n---You've done the game---")
    print(f"Your money: {player_money}")
    print(f"Number of wins: {count_win}")
