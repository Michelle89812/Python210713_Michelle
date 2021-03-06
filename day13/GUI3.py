# 放入視窗元件
import tkinter
import time
import threading  # 執行緒
from datetime import datetime
'''
+-----------+
|    10     |
| 加     減　|
|  dt...    |
+-----------+
若減到 0 則視窗離開 !
dt... = 現在時刻 2021/8/24 20:36:30
'''
def update_time():
    while True:
        try:
            now = datetime.today()
            dt.set(str(now).split('.')[0])
            time.sleep(1)
        except:
            break


def win_exit():
    time.sleep(0.5)
    win.quit()


def add():
    value = ans.get()
    value = value + 1
    ans.set(value)

def sub():
    value = ans.get()
    value = value - 1
    ans.set(value)

    if value == 0:
        t = threading.Thread(target=win_exit)  # 建立一個子執行緒
        t.start()  # 子執行緒運作

# -------------------------------------------------------
win = tkinter.Tk()
win.title('我的小視窗3')
win.geometry('400x300')

# ------------------------------------------------------
dt = tkinter.StringVar()
timelabel = tkinter.Label(win, textvariable=dt)
timelabel.pack()
t = threading.Thread(target=update_time)
t.start()
# ------------------------------------------------------

ans = tkinter.IntVar()
ans.set(10)
label = tkinter.Label(win,
                      textvariable=ans,
                      bg='orange',
                      font=('Arial', 50),
                      width=20,
                      height=2)
label.pack()

button1 = tkinter.Button(win, text="加", width=10, height=2, font=('Arial', 20),
                         command=add)
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(win, text="減", width=10, height=2, font=('Arial', 20),
                         command=sub)
button2.pack(side=tkinter.RIGHT)


win.mainloop()



