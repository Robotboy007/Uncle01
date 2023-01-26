from tkinter import *
from tkinter import ttk
import pyautogui as pg 
import webbrowser


GUI =Tk()
GUI.title('ปฏิทินชาวปด')
GUI.geometry('500x300')

def Calerder():
    pg.click(1279,740)
    
def Google():
    webbrowser.open('https://www.google.com')

B1 = Button(GUI,text='Calender0',command=Calerder)
B1.pack(ipadx=20, ipady=10, pady=20)

B2 = ttk.Button(GUI,text='Calender1',command=Calerder)
B2.pack(ipadx=20, ipady=10, pady=20)

B3 = ttk.Button(GUI,text='Google',command=Google)
B3.pack(ipadx=20, ipady=10)

GUI.mainloop()