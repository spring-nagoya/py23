print("hello world")
#文字列を表示させる場合は、""を必ずつける。
comment = "Hello World!"

print(comment)

value1=20
value2=30
total=value1 + value2
print(total)

#配列=>同じデータ型が複数入っている大きな箱
#リスト、辞書型
list=[10,20,30,40]
dic={"name1":"test1","name2":"test2"}
#json
#リスト型はデータの格納場所を番号で指定
#辞書型はデータの格納場所を名前で指定

#プログラムを形づける3つの構造
#1.順次構造：プログラムを上から下に向けて処理をする。
#2.分岐構造：プログラムに分かれ道を作る構造
#3.反復構造：プログラムに繰り返しを作る構造

#分岐構造(if~elif~else)
#==, !=, >, <, >=, <= :比較演算子
# ==:右辺と左辺が同一である
# !=:右辺と左辺は同一ではない
# > :左辺は右辺よりも大きい
# < :左辺は右辺よりも小さい
# >=:左辺は右辺以上である
# <=:左辺は右辺以下である
# bool値:条件を判定したときに得られる値
# True:正 False:偽
if total == 30:
    print(total)

if total == 40:
    print("正解です")
elif total == 50:
    print("正解です!!")

else:
    print("間違いです")

if total >= 40:
    if total <= 50:
        print("test")


#反復構造(for)
for value in range(1,10):
    print(value)


