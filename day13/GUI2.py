# 放入視窗元件
import tkinter
'''
+-----------+
|   Label   |
| B1     B2 |
+-----------+
'''

win = tkinter.Tk()

win.title('我的小視窗')
win.geometry('400x300')

label = tkinter.Label(win,
                      text='Hello',
                      bg='orange',
                      font=('Arial', 20),
                      width=30,
                      height=5)
label.pack()

button1 = tkinter.Button(win, text="OK", width=10, height=2, font=('Arial', 20))
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(win, text="Cancel", width=10, height=2, font=('Arial', 20))
button2.pack(side=tkinter.RIGHT)

win.mainloop()
