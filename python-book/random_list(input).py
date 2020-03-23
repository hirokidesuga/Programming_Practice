from random import randint

def get_user_input():
    input_message = ("要素数が0以上50以下のリストを作れます(要素は0~100の間でランダムに生成します)\n要素を何個にしますか:")
    val_min = 0
    val_max = 50
    while True:
        n = -1
        x = input(input_message)
        if x.isdigit():
            n = int(x)
            if val_min <= n <= val_max:
                return n
        print("0以上50以下の整数を入力してください！\n\n")


def random_list(l):
    range_min = 0
    range_max = 100
    x = []
    for i in range(l):
        x.append(randint(range_min, range_max))
    return x


def list_max(a):
    if not a:
        return "なし"
    max_value = a[0]
    for item in a:
        if item > max_value:
            max_value = item
    return max_value

def list_min(a):
    if not a:
        return "なし"
    min_value = a[0]
    for item in a:
        if item < min_value:
            min_value = item
    return min_value

def list_len(a):
    l = len(a)
    return l

def list_sum(a):
    sum = 0
    for item in a:
        sum += item
    return sum

def play():
    user_input = get_user_input()
    l = random_list(user_input)
    print(list(l))
    print("要素は{}個".format(list_len(l)))
    print("合計は{}".format(list_sum(l)))
    print("最大値は{}".format(list_max(l)))
    print("最小値は{}".format(list_min(l)))

def game():
    while True:
        play()
        get_user_request = input("もう一度生成しますか?y/n:")
        while get_user_request not in "yn":
            get_user_request = input("\n\nもう一度生成しますか？\nyかnを入力してください:")
            continue
        if get_user_request == "y":
            print("\n" * 10)
        else:
            break
    print("またのご利用をお待ちしております！")

if __name__ == "__main__":
    game()