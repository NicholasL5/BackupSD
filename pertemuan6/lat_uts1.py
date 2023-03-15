from pertemuan3.cobastack import Stack

password = input("masukkan password")
counter_pass = 0

stack_angka = Stack()
stack_huruf = Stack()
stack_temp = Stack()
temp = 999
temp_huruf = 'a'

for i in password:
    if i.isnumeric():
        if stack_angka.is_empty():
            stack_angka.push(i)
        else:
            while not stack_angka.is_empty() and int(i) > int(stack_angka.peek()):
                stack_temp.push(stack_angka.pop())
            stack_angka.push(i)
            if not stack_temp.is_empty():
                while not stack_temp.is_empty() and stack_temp.peek().isnumeric():
                    stack_angka.push(stack_temp.pop())
    else:
        if stack_huruf.is_empty():
            stack_huruf.push(i)
        else:
            while not stack_huruf.is_empty() and ord(i) < ord(stack_huruf.peek()):
                stack_temp.push(stack_huruf.pop())
            stack_huruf.push(i)
            if not stack_temp.is_empty():
                while not stack_temp.is_empty() and not stack_temp.peek().isnumeric():
                    stack_huruf.push(stack_temp.pop())


stack_angka.show()
print()
stack_huruf.show()

def check_pass(stack1:Stack, stack2:Stack):
    # asumsi stack1 = angka, stack2 = huruf
    temp = stack1.top
    counter = 1
    flag_angka = False
    flag_huruf = False
    while temp.next is not None:

        if (int(temp.next.data) - int(temp.data)) <= 2:
            counter += 1
        else:
            if counter != 1:
                counter = 1
        temp = temp.next

    if counter >= 4:
        flag_angka = True

    temp = stack2.top
    counter = 1
    while temp.next is not None:

        if (ord(temp.next.data) - ord(temp.data)) <= 2:
            counter += 1
        else:
            if counter != 1:
                counter = 1
        temp = temp.next
    if counter >= 3:
        flag_huruf = True


    print(flag_angka)
    print(flag_huruf)
    if flag_angka and flag_huruf:
        return "pass kuat"
    elif flag_angka:
        # 4 angka urut
        return "pass agak kuat"
    else:
        return "pass lemah"


string = check_pass(stack_angka, stack_huruf)


print()
print(len(password), "- ",end="")
stack_huruf.show()
print(" - ",end="")
stack_angka.show()
print(" ", string)





