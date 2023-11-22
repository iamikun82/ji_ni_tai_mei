import random

def get_user_choice():
    choice = input("请选择（石头、剪刀、布）：")
    while choice.lower() not in ["石头", "剪刀", "布"]:
        print("输入无效，请重新选择！")
        choice = input("请选择（石头、剪刀、布）：")
    return choice.lower()

def get_computer_choice():
    choice = random.choice(["石头", "剪刀", "布"])
    return choice.lower()

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "平局"
    elif (user_choice == "石头" and computer_choice == "剪刀") or \
         (user_choice == "剪刀" and computer_choice == "布") or \
         (user_choice == "布" and computer_choice == "石头"):
        return "你赢了！"
    else:
        return "计算机赢了！"

def play_game():
    print("石头剪刀布游戏开始！")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"你选择了：{user_choice}，计算机选择了：{computer_choice}")
    winner = determine_winner(user_choice, computer_choice)
    print(f"结果：{winner}")

play_game()