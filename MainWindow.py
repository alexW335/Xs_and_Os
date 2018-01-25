#!/usr/bin/env python3
 2 import tkinter as tk
 3 
 4 class Application(tk.Frame):
 5     def __init__(self, master=None):
 6         tk.Frame.__init__(self, master)
 7         self.grid()  
 8         self.createWidgets()
 9 
10     def createWidgets(self):
11         self.quitButton = tk.Button(self, text='Quit', command=self.quit)
12         self.quitButton.grid()
13 
14 app = Application()
15 app.master.title('Sample application')
16 app.mainloop()