import random
import sys

#キーボードで入力された数値を取得
hand = int(input("0:グー,1:チョキ,2:パー"))

#相手の出す手をランダムで選択(0:グー,1:チョキ,2:パー)
enemy = random.randint(0,2)

score = (int(hand)-int(enemy) + 3) %3

#もし変数handの値が0~2の範囲であれば
if 0 <= int(hand) <= 2:
    
    #変数handの値が2であれば
    if int(hand) == 2:
        mhand = "パー"
        
    #変数handの値が1であれば
    elif int(hand) ==1:
        mhand = "チョキ"
        
    #変数handの値が0であれば
    elif int(hand) ==0:
        mhand = "グー"
        
    else:
        print("指定外の数字が入力されたので終了します。")
        sys.exit()
    print("あなたは"+mhand+"を出しました。")
    
    #相手が出した手が2(パー)であれば
    if int(enemy) ==2:
        yhand = "パー"
    
    #相手が出した手が1(チョキ)であれば
    if int(enemy) == 1:
        yhand = "チョキ"
        
    #相手が出した手が0(グー)であれば
    if int(enemy) == 0:
        yhand = "グー"
        
    else:
        print("指定外の数字が入力されたので終了します。")
        
    if score == 0 :
        result = "引き分けです"
    elif score == 1:
        result = "あなたの負けです"
    else:
        result = "あなたの勝ちです"
print(result)
    