from random import randint

def guess_number() -> None:
    num = randint(1, 100)
    count = 0
    print("1~100のランダムな整数を生成しました、正しい数字を当ててください。\n")
    while True:
        user_input = get_user_input()
        count += 1
        if user_input == num:
            print("おめでとうございます、正解です!")
            break
        elif user_input > num:
            print("答えより大きいです、もう一度当ててみましょう!\n")
        else:
            print("答えより小さいです、もう一度当ててみましょう!\n")

    print(f"チャレンジ回数{count}、次もがんばってください。\n")

def get_user_input() -> int:
    raw_input = input("回答: ")
    if raw_input.isdigit() and 1 <= (int(raw_input)) <= 100:
        return int(raw_input)
    print("1以上100以下の整数を入力してください\n")
    return get_user_input()

def main():
    while True:
        guess_number()
        b = input("もう一度遊びますか?y/n ")
        while b not in "yn":
            continue
        if b == "y":
            print("-" * 10)
        else:
            break

    print("遊んでいただいてありがとうございました、またのご利用お待ちしております!")

if __name__ == "__main__":
    main()
