from tkinter import *
from tkinter.ttk import * 
 
root = Tk()
root.geometry("100x100")

style = Style() 

style.configure('W.TButton', font =
			('calibri', 10, 'bold', 'underline'), 
				foreground = 'red') 
 
button1 = Button(root, text = "Quit!",
                       style = 'W.TButton',
                    command = root.destroy)
button1.grid(row=0, column=0, padx = 100)

''' Button 2'''
btn2 = Button(root, text = 'Click me !', command = None) 
btn2.grid(row = 1, column = 3, pady = 10, padx = 100) 
 
root.mainloop()
