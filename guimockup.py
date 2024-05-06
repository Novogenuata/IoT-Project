# made with PAGE

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

#everything here was generated with PAGE, not functional yet.
class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+660+210")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(0,  0)
        top.title("Waste Management")

        self.top = top
        #thresh label
        self.Thresh = tk.Label(self.top)
        self.Thresh.place(x=20, y=10, height=21, width=149)
        self.Thresh.configure(activebackground="#d9d9d9")
        self.Thresh.configure(anchor='w')
        self.Thresh.configure(compound='left')
        self.Thresh.configure(text='''Enter threshold level:''')
        #security button (have to add a new window)
        self.Securitybutton = tk.Button(self.top)
        self.Securitybutton.place(x=50, y=200, height=31, width=71)
        self.Securitybutton.configure(activebackground="#d9d9d9")
        self.Securitybutton.configure(text='''Unlock''')
        # telling the user if it is locked or unlocked
        self.SecurityVariable = tk.Label(self.top)
        self.SecurityVariable.place(x=130, y=170, height=21, width=39)
        self.SecurityVariable.configure(activebackground="#d9d9d9")
        self.SecurityVariable.configure(anchor='w')
        self.SecurityVariable.configure(compound='left')
        self.SecurityVariable.configure(text='''X/Y''')
        #security label, static
        self.SecuirtyLabel = tk.Label(self.top)
        self.SecuirtyLabel.place(x=50, y=170, height=21, width=69)
        self.SecuirtyLabel.configure(activebackground="#d9d9d9")
        self.SecuirtyLabel.configure(anchor='w')
        self.SecuirtyLabel.configure(compound='left')
        self.SecuirtyLabel.configure(text='''Security''')
        #entry for thresh, should be int
        self.Threshinput = tk.Entry(self.top)
        self.Threshinput.place(x=20, y=40, height=22, width=126)
        self.Threshinput.configure(background="white")
        self.Threshinput.configure(font="TkFixedFont")
        self.Threshinput.configure(selectbackground="#d9d9d9")
        #groove
        self.Frame2 = tk.Frame(self.top)
        self.Frame2.place(x=210, y=270, height=105, width=325)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        #second groove
        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(x=210, y=140, height=85, width=335)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        # placeholder
        self.WarningPlacehold = tk.Label(self.Frame1)
        self.WarningPlacehold.place(x=30, y=20, height=21, width=109)
        self.WarningPlacehold.configure(activebackground="#d9d9d9")
        self.WarningPlacehold.configure(anchor='w')
        self.WarningPlacehold.configure(compound='left')
        self.WarningPlacehold.configure(text='''Placeholder''')
        #waste level , static
        self.Wastelevellabel = tk.Label(self.top)
        self.Wastelevellabel.place(x=260, y=20, height=21, width=119)
        self.Wastelevellabel.configure(activebackground="#d9d9d9")
        self.Wastelevellabel.configure(anchor='w')
        self.Wastelevellabel.configure(compound='left')
        self.Wastelevellabel.configure(text='''Waste level:''')

        # New label next to the Waste level label
        self.NewLabel = tk.Label(self.top)
        self.NewLabel.place(x=400, y=20, height=21, width=119)
        self.NewLabel.configure(activebackground="#d9d9d9")
        self.NewLabel.configure(anchor='w')
        self.NewLabel.configure(compound='left')
        self.NewLabel.configure(text='''New Label''')
#mainloop for the gui
if __name__ == '__main__':
    root = tk.Tk()
    app = Toplevel1(root)
    root.mainloop()
