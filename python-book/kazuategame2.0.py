import random
# import os

VAL_MIN = 1
VAL_MAX = 100


def ask_number():
    while True:
        n = 0
        s = input("回答:")
        if s.isdigit():
            n = int(s)
        if VAL_MIN <= n <= VAL_MAX:
            return n

        print("{}以上{}以下の整数を入力してください\n".format(VAL_MIN, VAL_MAX))


def ask_yes_no():
    print("もう一度遊びますか？y/n")
    while True:
        ans = input()
        if ans in ('y', 'n'):
            return ans

        print("※y(yes)かn(no)を入力してください！\n")


def play():
    print("{}~{}のランダムな整数を生成しました、正しい数字を当ててください。\n".format(VAL_MIN, VAL_MAX))
    num = random.randint(VAL_MIN, VAL_MAX)
    try_count = 0

    while True:
        n = ask_number()
        try_count += 1

        if n == num:
            print("おめでとうございます、正解です!")
            print("チャレンジ回数{}、次もがんばってください。".format(try_count))
            return

        if n > num:
            print("答えより大きいです、もう一度当ててみましょう！\n")
        else:
            print("答えより小さいです、もう一度当ててみましょう！\n")


def clear_screen():
    print("\033[2J")     # for ANSI terminal
    # # os.system('cls') # for windows


def game():
    while True:
        play()
        if ask_yes_no() == 'n':
            print("遊んでいただいてありがとうございました、またのご利用お待ちしております！")
            return
        clear_screen()


game()