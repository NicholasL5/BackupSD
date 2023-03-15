from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from Que import Queue
import file_compress

def get_filename():
    global path_queue
    temp_q = Queue()
    file = filedialog.askopenfilenames(initialdir="D:\\projects\\python_projects",
                                      title="Select A File",
                                      filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    # for i in file:
    #     index = i.rfind("/")
    #     Label(root, text=i[index+1:len(i)]).pack()
    #     temp_q.enqueue(i)

    try:
        to_table(temp_q)
    except TclError:
        print("item already exist")

    path_queue.add_all(temp_q)



def to_table(queue:Queue):
    global counter
    for i in queue.to_list():
        index = i.rfind("/")
        mytree.insert(parent='', index='end', iid=str(counter), text="", values=(counter+1, i[index+1:len(i)]))
        counter += 1

def start(args):
    args.printQ()



counter = 0
root = Tk()

add_frame = Frame(root)
add_frame.pack(pady=5)

Label(add_frame,text="Insert a File").grid(row=0, column=0)

path_queue = Queue()
root.geometry("500x500")
Button(root, text="Select Directory/Files", command=get_filename).pack()


mytree = ttk.Treeview(root)

# kolom
mytree['col'] = ("No.", "File")

# format kolom
mytree.column("#0", width=25, stretch=NO)
mytree.column("No.", anchor=W, width=50, minwidth=50)
mytree.column("File", anchor=CENTER, width=200)

mytree.heading("#0", text="", anchor=W)
mytree.heading("No.", text="No",anchor=W)
mytree.heading("File", text="Directory/Files", anchor=CENTER)

mytree.pack(pady=10)

name_frame = Frame(root)
name_frame.pack(pady=10)

compress_name = Label(name_frame, text="Input File Compress Name",)
compress_name.grid(row=0, column=0)

compress_name_box = Entry(name_frame, width=45)
compress_name_box.grid(row=1, column=0)

compress_program = file_compress.FileCompress()
Button(root, text="Compress", command=lambda: compress_program.compress(path_queue)).pack(pady=10)


Button(root, text="Decompress", command=lambda: start(path_queue)).pack(pady=10)



root.mainloop()

