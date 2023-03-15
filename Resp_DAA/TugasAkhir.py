def check_overlap(li1, li2):
    return True if (li1[0]) <= (li2[1]) and (li2[0]) < (li1[1]) else False


def print_path(list_ujian, memo):
    memo.append(0)
    counter = 340
    path = []
    # counter - poin ujian dengan memo tertinggi
    index = memo.index(counter)
    counter -= list_ujian[index][2]
    path.append(list_ujian[index])
    for i in range(index, -1, -1):
        if memo[i] == counter and not check_overlap(list_ujian[i], list_ujian[index]) and (
                counter - list_ujian[i][2]) in memo:
            index = i
            counter -= list_ujian[i][2]
            path.insert(0, list_ujian[i])
            if counter == 0:
                return path


def find_max_profit(list_ujian):
    if not list_ujian:
        return 0

    for ujian in list_ujian:
        print(ujian[0], ", ", ujian[1], ", ", ujian[2])

    memo = [0 for _ in range(len(list_ujian))]
    memo[0] = list_ujian[0][2]
    n = len(list_ujian)
    for i in range(1, n):
        print(memo)
        for j in range(i):
            if not check_overlap(list_ujian[j], list_ujian[i]) and memo[i] < memo[j] + list_ujian[i][2]:
                memo[i] = memo[j] + list_ujian[i][2]

        if memo[i] == 0:
            memo[i] = list_ujian[i][2]

    return memo


if __name__ == '__main__':
    # list_ujian = [
    # 	(1,3,20), (7,9,30), (6,7,40), (2,8,100), (3,5,50), (5,7,30), (1,4,20)
    # ]

    # list_ujian = [
    #     (1, 2, 3), (1, 3, 2),
    #     (3, 5, 5), (4, 6, 5), (5, 9, 7), (6, 10, 3)
    # ]

    list_ujian = [
    	(6, 10, 80), (4, 6, 90), (1, 7, 250),
    	(1, 3, 90), (3, 8, 100), (5, 10, 120),
    	(9, 12, 90), (10, 11, 50), (11, 12, 50),
    	(6, 9, 70)
    ]
    list_ujian.sort(key=lambda x: x[1])

    memo = find_max_profit(list_ujian)
    print("memo:", memo)
    print("max:", max(memo))
    print("path:", print_path(list_ujian, memo))
