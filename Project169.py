from tkinter import *
from tkinter import messagebox, ttk

root = Tk()
root.title('GUI Creator 2')
root.geometry('600x600')
root.configure(bg = 'snow')

btns = []
curY = 0.25

def makeParts():
        global curY
        if curPart.get() == 'Dropdown':
            drp = ttk.Combobox(root, state = 'readonly', values = ['Item A', 'Item B', 'Item C'])
            drp.place(relx = 0.5, rely = curY / 10, anchor = CENTER)
        elif curPart.get() == 'Button':
            global btns
            btn = Button(root, text = 'Click Me!', command = lambda: info(btns.index(btn)))
            btn.place(relx = 0.5, rely = curY / 10, anchor = CENTER)
            btns.append(btn)
        else:
            lbl = Label(root, text = 'Hello!', bg = 'light blue')
            lbl.place(relx = 0.5, rely = curY / 10, anchor = CENTER)
        curY += 0.5
    
def info(index):
    global btns
    curBtn = btns[index]
    colorNum = index % 4 + 1

    messagebox.showinfo('Info', f'The button you clicked on has an ID of { index }.\nIt will now change color!')
    curBtn['bg'] = f'salmon{colorNum}'
    if colorNum > 2:
        curBtn['fg'] = 'white'

curPart = StringVar()
drpPart = ttk.Combobox(root, state = 'readonly', values = ['Label', 'Button', 'Dropdown'], textvariable = curPart)
drpPart.place(relx = 0.25, rely = 0.5, anchor = CENTER)

btnMake = Button(root, text = 'Create New Parts', command = lambda: makeParts())
btnMake.place(relx = 0.75, rely = 0.5, anchor = CENTER)

root.mainloop()