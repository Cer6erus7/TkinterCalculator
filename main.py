import tkinter as tk
from tkinter import messagebox


def calculating():
    value = enter.get()
    if value[-1] in "-+/*":
        value = value[:-1] + value[-1] + value[:-1]
    enter.delete(0, tk.END)
    try:
        enter.insert(tk.END, eval(value))
    except NameError:
        messagebox.showinfo("Error!", "Incorrect input, try again!")
        remover()
    except SyntaxError:
        messagebox.showinfo("Error!", "Syntax error, try again!")
        remover()
    except ZeroDivisionError:
        messagebox.showinfo("Error!", "You cannot divide zeroes!")
        remover()


def add_number(number):
    if enter.get()[0] == "0" and len(enter.get()) == 1:
        enter.delete(0)
    enter.insert(tk.END, number)


def btn_number(symbol):
    return tk.Button(win, text=symbol, command=lambda: add_number(symbol), bd=4)


def add_operator(operator):
    value = enter.get()
    if value[-1] in '*-/+':
        enter.delete(len(value) - 1)
    if '+' in value or '-' in value or '/' in value or '*' in value:
        calculating()
    enter.insert(tk.END, operator)


def btn_operator(symbol):
    return tk.Button(win, text=symbol, command=lambda: add_operator(symbol), bd=4)


def remover():
    enter.delete(0, tk.END)
    enter.insert(tk.END, "0")


def press_key(event):
    print(event)
    if event.char.isdigit():
        add_number(event.char)
    if event.char in "+/-*":
        add_operator(event.char)
    if event.char == "=" or event.keysym == "Return":
        calculating()


win = tk.Tk()
win.title("Calculator")
win.geometry("240x260+545+200")
win.config(bg="#153023")
win.resizable(False, False)
logo = tk.PhotoImage(file='img.png')
win.iconphoto(False, logo)
win.bind("<Key>", press_key)

#153023  green color
#33ffe6  blue color

enter = tk.Entry(win, borderwidth=4, relief=tk.RAISED, justify=tk.RIGHT, font=("Arial", 15))
enter.grid(row=0, columnspan=4, stick='wens', pady=5, padx=5)
enter.insert(tk.END, "0")

btn_number("1").grid(row=1, column=0, stick='wens', pady=5, padx=5)
btn_number("2").grid(row=1, column=1, stick='wens', pady=5, padx=5)
btn_number("3").grid(row=1, column=2, stick='wens', pady=5, padx=5)
btn_number("4").grid(row=2, column=0, stick='wens', pady=5, padx=5)
btn_number("5").grid(row=2, column=1, stick='wens', pady=5, padx=5)
btn_number("6").grid(row=2, column=2, stick='wens', pady=5, padx=5)
btn_number("7").grid(row=3, column=0, stick='wens', pady=5, padx=5)
btn_number("8").grid(row=3, column=1, stick='wens', pady=5, padx=5)
btn_number("9").grid(row=3, column=2, stick='wens', pady=5, padx=5)
btn_number("0").grid(row=4, column=1, stick='wens', pady=5, padx=5)

tk.Button(win, text="C", command=remover, bd=4).grid(row=4, column=0, stick='wens', pady=5, padx=5)

btn_operator("+").grid(row=1, column=3, stick='wens', pady=5, padx=5)
btn_operator("-").grid(row=2, column=3, stick='wens', pady=5, padx=5)
btn_operator("/").grid(row=3, column=3, stick='wens', pady=5, padx=5)
btn_operator("*").grid(row=4, column=3, stick='wens', pady=5, padx=5)
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