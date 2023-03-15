from pertemuan3.cobastack import Stack

equation = input("Masukkan input: ")
stack = Stack()
pasangan = ""
counter = 0
cek = True


def cek_pasangan(val):
    if val == "(":
        return ")"

    elif val == "{":
        return "}"

    elif val == "[":
        return "]"


for i in equation:
    if i == "(" or i == "{" or i == "[":
        pasangan = cek_pasangan(i)
        stack.push(i)

    elif i == ")" or i == "}" or i == "]":
        if i == pasangan:
            stack.pop()
            counter += 1
            pasangan = cek_pasangan(stack.peek())
        elif pasangan == "":
            print("langsung kurung tutup")
            break
        else:
            print("salah pasangan seharusnya", pasangan)
            print("tapi malah ", i)
            break

if counter >= 2:
    print("True")
else:
    print("False")
