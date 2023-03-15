from cobastack import Stack

def check_stack(string):
    # if len(string) % 2 == 1:
    #     print("invalid")
    #     return False
    stack = Stack()
    counter = 0
    for i in string:
        tambah = False
        if counter != 0:
            if kurung == "(":
                if i == ")":
                    stack.pop()
                    tambah = True

            elif kurung == "{":
                if i == "}":
                    stack.pop()
                    tambah = True
            elif kurung == "[":
                if i == "]":
                    stack.pop()
                    tambah = True

        if counter == 0:
            if i in ["]", "}", ")"] and stack.peek() is None:
                return False
        counter += 1
        if not tambah:
            stack.push(i)
        kurung = stack.peek()

    if not stack.is_empty():
        return False
    else:
        return True
    # if stack.top in ["(", "[", "{"]:
    #     print("invalid")
    #     return False

my_string = input("print tanda kurung matematika")
flag = check_stack(my_string)
if flag:
    print("valid")
else:
    print("invalid")



