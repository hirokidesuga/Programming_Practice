import random


while True:
    num = random.randint(1,100)
    count = 0
    a = ""
    print("1~100のランダムな整数を生成しました、正しい数字を当ててください。\n")
    while a != num:
        a = input("回答:")
        if a.isdigit() != True:
            print("0以上100以下の整数を入力してください\n")
            continue
        a = int(a)
        if a > 100 or a < 0 or type(a) != int:
            print("0以上100以下の整数を入力してください\n")
            continue
        if a == num:
            print("おめでとうございます、正解です!")
            count += 1
            break
        elif a > num:
            print("答えより大きいです、もう一度当ててみましょう！\n")
        else:
            print("答えより小さいです、もう一度当ててみましょう！\n")
        count += 1
    print("チャレンジ回数{}、次もがんばってください。".format(count))
    print("もう一度遊びますか？y/n")
    b = ""
    while b != "y" and b != "n":
        print("※y(yes)かn(no)を入力してください！\n")
        b = input()
    if b == "y":
        print("\n" * 100)
        continue
    else:
        break

print("遊んでいただいてありがとうございました、またのご利用お待ちしております！")
