import random 
def shutudai():
    qa = random.choice(qa_list)
    print("問題:"+qa["q"])
    return qa["a"]


def kaitou(seikai):
    a = input("回答:")
    if a in seikai:
        print("正解です")
    else:
        print("不正解です")

    pa_list = [
        {"q":"サザエの旦那の名前は？","a":["マスオ","ますお"]},
        {"q":"カツオの妹の名前は？","a":["ワカメ","わかめ"]},
        {"q":"タラオはカツオから見てどんな関係？","a":["甥","おい","甥っ子"]},

    ]
    seikai = shutudai(qa_list)
    kaitou(seikai)





    