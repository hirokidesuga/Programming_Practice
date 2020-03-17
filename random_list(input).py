from random import randint

def get_user_input():
    while True:
        n = -1
        x = input("要素数が0以上50以下のリストを作れます(要素は0~100の間でランダムに生成します)\n、要素を何個にしますか:")
        if x.isdigit():
            n = int(x)
        if 0 <= n <= 50:
            return n
        print("0以上50以下の整数を入力してください！ロリコンが！\n\n")


def random_list():
    y = get_user_input()
    x = []
    for n in range(y):
        x.append(randint(0, 100))
    return x

def list(a):
    return a

def random_list_max(a):
    if not a:
        return "なし"
    max_value = a[0]
    for item in a:
        if item > max_value:
            max_value = item
    return max_value

def list_len(a):
    ko = len(a)
    return ko

def random_list_min(a):
    if not a:
        return "なし"
    min_value = a[0]
    for item in a:
        if item < min_value:
            min_value = item
    return min_value

def add(a):
    sum = 0
    for item in a:
        sum += item
    return sum

def play():
    l = random_list()
    print(list(l))
    print("要素は{}個".format(list_len(l)))
    print("合計は{}".format(add(l)))
    print("最大値は{}".format(random_list_max(l)))
    print("最小値は{}".format(random_list_min(l)))

if __name__ == "__main__":
    play()