import numpy as np
import matplotlib.pyplot as plt

#データの読み込み
data = np.loadtxt('pointex.txt', dtype='str')

#print(data)

#データを日付と収入と支出に分ける
splited_detail = np.hsplit(data[0],[1,3])
splited_data = np.hsplit(data[1:],[1,3])

#print(splited_data)

#入力をそれぞれ定義
dayname = splited_detail[0]
indetail = splited_detail[1]
exdetail = splited_detail[2]
date = splited_data[0].flatten()
income = splited_data[1].astype(np.int)
expense = splited_data[2].astype(np.int)

#色の定義
incolors = ['r','g']
excolors = ['b']

#x軸
X = np.arange(len(date))

#収入を描画
bottoms = np.zeros(income.shape[0])

for i in range(income.shape[1]):
    plt.bar(
        X,                      #x軸(日付)
        income[:, i],           #y軸(収入)
        bottom = bottoms,       #バーが始まる高さ(積み上げ用)
        color = incolors[i],    #色
        alpha = .5,            #色の薄さ
        edgecolor = 'white',    #枠の色
        label = indetail[i]     #ラベル
    )
    #積み上げのための足場
    bottoms += income[:, i]


#支出を描画
bottoms = np.zeros(expense.shape[0])

for i in range(expense.shape[1]):
    plt.bar(
        X,                      #x軸(日付)
        -expense[:, i],         #y軸(支出)
        bottom = -bottoms,      #バーが始まる高さ(積み上げ用)
        color = excolors[i],    #色
        alpha = .5,            #色の薄さ
        edgecolor = 'white',    #枠の色
        label = exdetail[i]     #ラベル
    )
    #積み上げのための足場
    bottoms -= expense[:, i]

#ラベル付け
income_sum = income.sum(axis=1)     #各日にちの収入合計
expense_sum = expense.sum(axis=1)   #各日にちの支出合計
for x, y1, y2 in zip(X, income_sum, expense_sum): 
    if y1 != 0:
        plt.text(x, y1 + 0.05, '%d' %y1, ha='center', va='bottom')
    if y2 != 0:
        plt.text(x, -y2 - 0.05, '%d' %y2, ha='center', va='top')

#グラフの詳細設定
plt.xlim(-.5, len(date))
plt.xticks(X, date)
plt.ylim(-max(expense.sum(axis=0))*1.1, max(income.sum(axis=0))*1.1)
plt.yticks(())

#x軸の作成
ax = plt.gca() 
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))

plt.legend(loc="upper right")


plt.show()