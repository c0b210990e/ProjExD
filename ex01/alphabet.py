import random
global_alphabet = 26
global_taishou = 10
global_kesson = 2
global_chance = 2

def shutudai(alphabet):
    taishou = random.sample(alphabet,global_taishou)
    print("対象文字:",end="")
    for n in sorted(taishou):
        print(n,end="")
    print()

    kesson = random.sample(taishou,global_kesson)
    print("表示文字:",end="")
    for n in taishou:
        if n not in kesson:
            print(n,end="")
    print()
    ##print("デバッグ用欠損文字:",kesson)



def kaitou(kotae):
    a = int(input("欠損文字はいくつあるでしょうか？:"))
    if a != global_kesson:
        print("不正解です")
    else:
        print("正解です。それでは、具体的に欠損文字を一つずつ入力してください")
        for i in range(a):
            n = input(f"{i+1}つ目の文字を入力してください:")
            if n != kotae:
                print("不正解です。またチャレンジしてください")
            else:
                print("正解です")

    

alphabet = [chr(i+65) for i in range(global_alphabet)]
shutudai(alphabet)
kotae = shutudai(alphabet)
kaitou(kotae)

