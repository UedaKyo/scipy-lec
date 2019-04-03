import numpy as np
import matplotlib.pyplot as plt

plt.axes([0.001, 0.001, 0.998, 0.998])

#データの読み込み
data = np.loadtxt("newpoint.txt", dtype="str")


#データを分ける
splited_data = np.hsplit(data[1:], [1])

#print(splited_detail)
#print(splited_data)

#入力を定義
detail = data[0]
name = splited_data[0].flatten()
result = splited_data[1].astype(np.float)
#print(len(name))
#print(splited_dataf)

#色の定義
colors = ['r', 'g', 'b', 'y', 'c', 'm', 'navy', 'pink', 'k']


#描画
for i in range(len(name)):
    plt.scatter(result[i][1], result[i][0], s=result[i][2]*3, alpha=.5, color = colors[i], edgecolors='black', label = name[i])

#時給千円の線
x = np.linspace(0, 10, 256, endpoint = True)
y = x * 1000 / 60
plt.plot(x, y, label = "Hourly wage 1000 yen")

#グラフの詳細設定
plt.xlim(0, 10)
plt.xlabel("needed time (min)")
plt.ylim(0, 40)
plt.ylabel("getting point")
plt.legend(loc = "upper right")

plt.show()