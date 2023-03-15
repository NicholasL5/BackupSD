from pertemuan5.cobaQ import Queue

def compare_AND(val1, val2):
    if val1 == 1 and val2 == 1:
        return str(1)
    else:
        return str(0)

def compare_XOR(val1, val2):
    if int(val1) == int(val2):
        return str(0)
    else:
        return str(1)


binary1 = input("input binary 1:")
binary2 = input("input binary 2:")

queue_bin1 = Queue()
queue_bin2 = Queue()

if len(binary1) > len(binary2):
    selisih = len(binary1) - len(binary2)
    for i in range(selisih):
        queue_bin2.enqueue(int(0))

else:
    selisih = len(binary2) - len(binary1)
    for i in range(selisih):
        queue_bin1.enqueue(int(0))

for i in binary1:
    queue_bin1.enqueue(int(i))
for i in binary2:
    queue_bin2.enqueue(int(i))

print("Que1")
queue_bin1.printQ()
print("Que2")
queue_bin2.printQ()

ans_AND = ans_XOR = ""
while not queue_bin1.isEmpty():
    ans_AND += compare_AND(queue_bin1.peek(), queue_bin2.peek())
    ans_XOR += compare_XOR(queue_bin1.peek(), queue_bin2.peek())
    queue_bin1.dequeue()
    queue_bin2.dequeue()

print("and:", ans_AND)
print("xor:", ans_XOR)


