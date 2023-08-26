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


enter = tk.Entry(win, borderwidth=4, relief=tk.RAISED, justify=tk.RIGHT, font=("Arial", 15))
enter.grid(row=0, columnspan=4, stick='wens', pady=5, padx=5)

tk.Button(win, text="1", command=lambda: enter.insert(tk.END, '1'), bd=4).grid(row=1, column=0, stick='wens', pady=5, padx=5)
tk.Button(win, text="2", command=lambda: enter.insert(tk.END, "2"), bd=4).grid(row=1, column=1, stick='wens', pady=5, padx=5)
tk.Button(win, text="3", command=lambda: enter.insert(tk.END, "3"), bd=4).grid(row=1, column=2, stick='wens', pady=5, padx=5)
tk.Button(win, text="+", command=lambda: enter.insert(tk.END, "+"), bd=4).grid(row=1, column=3, stick='wens', pady=5, padx=5)
tk.Button(win, text="4", command=lambda: enter.insert(tk.END, "4"), bd=4).grid(row=2, column=0, stick='wens', pady=5, padx=5)
tk.Button(win, text="5", command=lambda: enter.insert(tk.END, "5"), bd=4).grid(row=2, column=1, stick='wens', pady=5, padx=5)
tk.Button(win, text="6", command=lambda: enter.insert(tk.END, "6"), bd=4).grid(row=2, column=2, stick='wens', pady=5, padx=5)
tk.Button(win, text="-", command=lambda: enter.insert(tk.END, "-"), bd=4).grid(row=2, column=3, stick='wens', pady=5, padx=5)
tk.Button(win, text="7", command=lambda: enter.insert(tk.END, "7"), bd=4).grid(row=3, column=0, stick='wens', pady=5, padx=5)
tk.Button(win, text="8", command=lambda: enter.insert(tk.END, "8"), bd=4).grid(row=3, column=1, stick='wens', pady=5, padx=5)
tk.Button(win, text="9", command=lambda: enter.insert(tk.END, "9"), bd=4).grid(row=3, column=2, stick='wens', pady=5, padx=5)
tk.Button(win, text="/", command=lambda: enter.insert(tk.END, "/"), bd=4).grid(row=3, column=3, stick='wens', pady=5, padx=5)
tk.Button(win, text="C", command=lambda: enter.delete(0, tk.END), bd=4).grid(row=4, column=0, stick='wens', pady=5, padx=5)
tk.Button(win, text="0", command=lambda: enter.insert(tk.END, "0"), bd=4).grid(row=4, column=1, stick='wens', pady=5, padx=5)
tk.Button(win, text="=", command=calculating, bd=4).grid(row=4, column=2, stick='wens', pady=5, padx=5)
tk.Button(win, text="*", command=lambda: enter.insert(tk.END, "*"), bd=4).grid(row=4, column=3, stick='wens', pady=5, padx=5)


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