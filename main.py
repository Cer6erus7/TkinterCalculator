import tkinter as tk


win = tk.Tk()
win.title("Calculator")
win.geometry("240x260+545+200")
win.config(bg="#153023")
win.resizable(False, False)
logo = tk.PhotoImage(file='img.png')
win.iconphoto(False, logo)

#153023  green color
#33ffe6  blue color


def calculating():
    value = str(enter.get())
    enter.delete(0, tk.END)
    try:
        enter.insert(tk.END, eval(value))
    except ZeroDivisionError:
        enter.insert(tk.END, "You cannot divide zeroes!")
    except SyntaxError:
        enter.insert(tk.END, "Syntax error, try again!")


def post_number(number):
    if enter.get()[0] == "0" and len(enter.get()) == 1:
        enter.delete(0)
    enter.insert(tk.END, number)


def make_number(symbol):
    return tk.Button(win, text=symbol, command=lambda: post_number(symbol), bd=4)


def post_operator(operator):
    if enter.get()[-1] in '*-/+':
        enter.delete(len(enter.get()) - 1)
    enter.insert(tk.END, operator)


def make_operator(symbol):
    return tk.Button(win, text=symbol, command=lambda: post_operator(symbol), bd=4)


def remover():
    enter.delete(0, tk.END)
    enter.insert(tk.END, "0")


enter = tk.Entry(win, borderwidth=4, relief=tk.RAISED, justify=tk.RIGHT, font=("Arial", 15))
enter.grid(row=0, columnspan=4, stick='wens', pady=5, padx=5)
enter.insert(tk.END, "0")

make_number("1").grid(row=1, column=0, stick='wens', pady=5, padx=5)
make_number("2").grid(row=1, column=1, stick='wens', pady=5, padx=5)
make_number("3").grid(row=1, column=2, stick='wens', pady=5, padx=5)
make_number("4").grid(row=2, column=0, stick='wens', pady=5, padx=5)
make_number("5").grid(row=2, column=1, stick='wens', pady=5, padx=5)
make_number("6").grid(row=2, column=2, stick='wens', pady=5, padx=5)
make_number("7").grid(row=3, column=0, stick='wens', pady=5, padx=5)
make_number("8").grid(row=3, column=1, stick='wens', pady=5, padx=5)
make_number("9").grid(row=3, column=2, stick='wens', pady=5, padx=5)
make_number("0").grid(row=4, column=1, stick='wens', pady=5, padx=5)

tk.Button(win, text="C", command=remover, bd=4).grid(row=4, column=0, stick='wens', pady=5, padx=5)

make_operator("+").grid(row=1, column=3, stick='wens', pady=5, padx=5)
make_operator("-").grid(row=2, column=3, stick='wens', pady=5, padx=5)
make_operator("/").grid(row=3, column=3, stick='wens', pady=5, padx=5)
make_operator("*").grid(row=4, column=3, stick='wens', pady=5, padx=5)
tk.Button(win, text="=", command=calculating, bd=4).grid(row=4, column=2, stick='wens', pady=5, padx=5)


win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(0, minsize=50)
win.grid_rowconfigure(1, minsize=50)
win.grid_rowconfigure(2, minsize=50)
win.grid_rowconfigure(3, minsize=50)
win.grid_rowconfigure(4, minsize=50)

if __name__ == '__main__':
    win.mainloop()