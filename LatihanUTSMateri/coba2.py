# arr = [1, 3, 4, 5, 1, 3, 2, 7, 5, 7]
# counts = dict()
# for i in arr:
#     val = counts.get(i, 0) + 1
#     print(val)
#     counts[i] = val
#
#
# print(counts)
# print(sorted(counts.items()))

# x = [1, 2, 3, 4, 5]
# weight = [4, 5, 6, 7, 8]
# weightx = []
# for i in range(len(x)):
#     weightx.append(x[i] * weight[i])
# print(weightx)
# print(sum(weightx)/sum(weight))
# print()
import numpy as np
arr = np.array([[1,0,3],
                [4,8,6],
                [10,8,21]])

hasil = []
counter = 0
for i in range(3):
    counter = 0
    for j in range(3):
        counter += arr[j][i]
    print(counter)
    counter /= 3
    hasil.append(counter)

print(hasil)
print()

import math
a = [1,4]
b = [0,7]
c = [-2,3]


ab = math.sqrt(math.pow((b[0]-a[0]),2) + math.pow((b[1]-a[1]),2))
ac = math.sqrt(math.pow((c[0]-a[0]),2) + math.pow((c[1]-a[1]),2))
bc = math.sqrt(math.pow((c[0]-b[0]),2) + math.pow((c[1]-b[1]),2))
print(ab)
print(ac)
print(bc)

s = (ab+ac+bc)/2

L = math.sqrt(s*(s-ab)*(s-ac)*(s-bc))
print(L)


