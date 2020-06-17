import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="thing.gif")

w1 = tk.Label(root, image=logo).pack(side="right")
w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=explanation).pack(side="left")
root.mainloop()
