# from pertemuan3.cobastack import Stack
#
# list_stack = []
# for i in range(5):
#     newStack = Stack()
#     list_stack.append(newStack)
#
# list_stack[0].push(1)
# list_stack[0].push(2)
# list_stack[1].push(3)
# list_stack[1].push(4)
# list_stack[2].push(5)
# list_stack[2].push(6)
# list_stack[3].push(7)
# list_stack[4].push(8)
# print("selesai")
#
# list_stack[3].pop()
# list_stack.remove(list_stack[3])
# print("selesai")

# Python program to display the Fibonacci sequence
# from collections import defaultdict
# graph = defaultdict(list)
# print(graph)
# graph[0].append(1)
# print(graph)

import pandas as pd
import matplotlib.pyplot as plt

# data = {
#     'bulan': [1,2,3,4,5,6]
#     'A':[58,60,82,73,69,78],
#     'B':[78,52,76,80,66,90],
#     'C':[64,74,65,60,57,67],
#     'D':[80,47,56,67,51,80],
# }

df = pd.read_excel('test.xlsx')
print(df.info())
plt.figure(figsize=(30, 11))
# plt.plot(df['bulan'], df["rata-rata"], marker="o")
# plt.title("data total profit setiap bulan")
# plt.xlabel("bulan")
# plt.ylabel("total profit")

width = 0.15
x = df['bulan']
plt.bar(x, df["A"], width, label="Kelas A")
plt.bar(x+width, df["B"], width, label="Kelas B")
plt.bar(x+width*2, df["C"], width, label="Kelas C")
plt.bar(x+width*3, df["D"], width, label="Kelas D")
plt.xticks([x+width*1.5 for x in range(1, len(df['bulan']) + 1)], df['bulan'])
plt.legend()



plt.show()

