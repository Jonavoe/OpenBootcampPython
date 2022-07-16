import tkinter as tk

window = tk.Tk()
def clear(event):
    rb1.deselect()
    rb2.deselect()
    rb3.deselect()
    print('clear')
seleccionado = tk.StringVar()

rb1 = tk.Radiobutton(window, text='Belen', value=1, variable='seleccionado')
rb2 = tk.Radiobutton(window, text='Harry', value=2, variable='seleccionado')
rb3 = tk.Radiobutton(window, text='Negri', value=3,variable='seleccionado')
btnClear = tk.Button(window, text='Clear', command='clear')

rb1.pack(padx=10, pady=10)
rb2.pack(padx=10, pady=10)
rb3.pack(padx=10, pady=10)
btnClear.pack(padx=10, pady=10)


btnClear.bind('<Button-1>', clear)

tk.mainloop()

