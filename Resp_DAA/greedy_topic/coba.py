data = [[1,3], [1,2], [2,4], [4,8]]

def check_overlap(item, pekerjaan):

    for p in pekerjaan:
        if item[0] > p[0] and item[0] < p[1]:
            return True
        if item[1] > p[0] and item[1] < p[1]:
            return True
    return False

pekerjaan =[]
pekerjaan.append(data[0])
for i in data[1:]:
    if not check_overlap(i, pekerjaan):
        pekerjaan.append(i)

print(pekerjaan)
