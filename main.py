from art import logo, vs
from game_data import data
import random

game_running = True
score = 0
print(logo)
compare_A = random.choice(data)
compare_B = random.choice(data)
while game_running:
    print(f"Your score is {score}")
    print(f"Compare A:{compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}")
    print(vs)
    print(f"Compare B:{compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}")
    is_choice = True
    while is_choice:
        choice = input("Who has more followers?Type A or B?").upper()
        if choice == "A":
            is_choice = False
            if compare_A['follower_count'] > compare_B['follower_count']:
                score += 1
            else:
                game_running = False
                print(f"Sorry that is wrong. Your final score is {score}")
        elif choice == "B":
            is_choice = False
            if compare_B['follower_count'] > compare_A['follower_count']:
                score += 1
            else:
                game_running = False
                print(f"Sorry that is wrong. Your final score is {score}")
        else:
            print("Please type again")
    compare_A = compare_B
    compare_B = random.choice(data)