import random
import tkinter as tk

list_your_num = []
num = 0
hit = 0
blow = 0

while True:
    global ans_num
    ans_num = random.randint(0, 9000) + 1000
    list_num = list(str(ans_num))
    list_num_s =set(list_num)
    if len(list_num_s) == 4:
        if str(ans_num).startswith("0"):
            continue
        break
    else:
        continue

def do_judge():
    global list_num
    global list_your_num
    global hit
    global blow
    print(e.get())
    list_your_num = e.get()
    for i in range(4):
        if int(list_your_num[int(i)]) == int(list_num[int(i)]):
            hit += 1
        for j in range(4):
            if i != j and int(list_your_num[int(i)]) == int(list_num[int(j)]):
                blow += 1
    print("Hit:" + str(hit), "Blow:" + str(blow))
    label_f = tk.Label(root, text="Hit:" + str(hit) + "&" + "Blow:" + str(blow), font=("MSゴシック", "20", "bold"))
    label_h = tk.Label(root)
    label_b = tk.Label(root)
    label_success = tk.Label(root,text="正解です！\nおめでとうございます！",font=("","15","bold"))
    label_f.grid()
    label_h.grid()
    label_b.grid()
    label_f.place(x=320, y=0)
    if hit ==4:
        label_success.grid()
        label_success.place(x=320, y=80)
    hit = 0
    blow = 0
    clear()


def clear():
    global num
    num = 0
    show_number(num)

def key1():
    key(1)

def key2():
    key(2)

def key3():
    key(3)

def key4():
    key(4)

def key5():
    key(5)

def key6():
    key(6)

def key7():
    key(7)

def key8():
    key(8)

def key9():
    key(9)

def key0():
    key(0)

def key(n):
    global num
    num = num * 10 + n
    show_number(num)

def show_number(num):
    e.delete(0,tk.END)
    e.insert(0,str(num))

def close_window():
    root.destroy()

root = tk.Tk()
root.geometry("540x362")
root.title("Hit and Blow")
f = tk.Frame(root)
f.grid()

b1 = tk.Button(f,text="1",height=5,width=12,command=key1)
b2 = tk.Button(f,text="2",height=5,width=12,command=key2)
b3 = tk.Button(f,text="3",height=5,width=12,command=key3)
b4 = tk.Button(f,text="4",height=5,width=12,command=key4)
b5 = tk.Button(f,text="5",height=5,width=12,command=key5)
b6 = tk.Button(f,text="6",height=5,width=12,command=key6)
b7 = tk.Button(f,text="7",height=5,width=12,command=key7)
b8 = tk.Button(f,text="8",height=5,width=12,command=key8)
b9 = tk.Button(f,text="9",height=5,width=12,command=key9)
b0 = tk.Button(f,text="0",height=5,width=12,command=key0)
bc = tk.Button(f,text="Clear",height=5,width=12,command=clear)
bj = tk.Button(f,text="Judge",height=5,width=12,command=do_judge)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b0.grid(row=4, column=0)
bc.grid(row=4, column=1)
bj.grid(row=4, column=2)

e = tk.Entry(f,width=46)
e.grid(row=0, column=0, columnspan=10)

tk.mainloop()


