from tkinter import *


def add():
    box.insert(END, entry.get())
    entry.delete(0, END)


def dele():
    select = list(box.curselection())
    select.reverse()
    for i in select:
        box.delete(i)


def save():
    f = open('blacklist.txt', 'w')
    f.writelines("\n".join(box.get(0, END)))
    f.close()


root = Tk()
root.title("Список имен:"
           "")
box = Listbox(selectmode=EXTENDED)
box.pack(side=LEFT)

scroll = Scrollbar(command=box.yview)
scroll.pack(side=LEFT, fill=Y)

box.config(yscrollcommand=scroll.set)

f = Frame()
f.pack(side=LEFT, padx=10)
Label(f, font='bold', fg='black', text="Введите имя:") \
    .pack(side=TOP)

entry = Entry(f) \

entry.pack(anchor=N)

Button(f, text="Добавить", command=add) \
    .pack(fill=X)
Button(f, text="Удалить", command=dele) \
    .pack(fill=X)
Button(f, text="Сохранить", command=save) \
    .pack(fill=X)

root.mainloop()
