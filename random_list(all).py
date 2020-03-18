from random import randint


def get_user_input():
    val_min = 0
    val_max = 1000000
    val_error = "0以上の整数を入力してください。(上限1000000)\n"
    print("要素数の個数、要素の最小、最大値を入力し、ランダムにリストを生成します。(半角数字で入力してください)")
    while True:
        n = -1
        x = input("要素数:")
        if x.isdecimal():
            n = int(x)
            if val_min <= n <= val_max:
                return n
        print(val_error)

def random_list(b):
    range_error = "最小値<最大値となるような整数を入力してください。半角数字で入力してください\n"
    while True:
        range_min = input("要素の最小値:")
        range_max = input("要素の最大値:")
        if (range_min[0] == "-" and range_min[1:].isdecimal() or range_min.isdecimal()) and (
                range_max[0] == "-" and range_max[1:].isdecimal() or range_max.isdecimal()):
            range_min = int(range_min)
            range_max = int(range_max)
            if range_min < range_max:
                break
        print(range_error)
    x = []
    for i in range(b):
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
    return len(a)


def list_sum(a):
    val_sum = 0
    for item in a:
        val_sum += item
    return val_sum


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
            get_user_request = input("\nもう一度生成しますか？\nyかnを入力してください:")
            continue
        if get_user_request == "y":
            print("\n" * 10)
        else:
            break
    print("またのご利用をお待ちしております！")


if __name__ == "__main__":
    game()
