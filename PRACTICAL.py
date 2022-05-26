from tkinter import *
from math import sqrt


def callback(event):
    clicked()


def clicked():
    value = 0
    u1 = float(uncertainty1_textbox.get())
    v1 = float(value1_textbox.get())
    u2 = float(uncertainty2_textbox.get())
    v2 = float(value2_textbox.get())
    a = float(answer_textbox.get())

    temp1 = (u1 / v1) ** 2
    temp2 = (u2 / v2) ** 2
    temp = sqrt(temp1 + temp2)
    value = a * temp

    rtn.configure(text=f'Uncertainty is:     {value}')


window = Tk()
window.title("Uncertainty Calculator")
# lbl = Label(window, text='Hello', font=('Arial', 12))
# lbl.grid(column=0, row=0)  # without this it wouldn't show up

main1 = Label(window, text='First variable', font=('Arial', 12))
main1.grid(column=0, row=0)

uncertainty1 = Label(window, text='Uncertainty', font=('Arial', 10))
uncertainty1.grid(column=0, row=1)

uncertainty1_textbox = Entry(window, width=10)
uncertainty1_textbox.grid(column=1, row=1)
uncertainty1_textbox.insert(0, '0')

uncertainty1_textbox.focus_set()

value1 = Label(window, text='Value', font=('Arial', 10))
value1.grid(column=2, row=1)

value1_textbox = Entry(window, width=10)
value1_textbox.grid(column=3, row=1)
value1_textbox.insert(0, '1')

main2 = Label(window, text='Second variable', font=('Arial', 12))
main2.grid(column=0, row=5)

uncertainty2 = Label(window, text='Uncertainty', font=('Arial', 10))
uncertainty2.grid(column=0, row=6)

uncertainty2_textbox = Entry(window, width=10)
uncertainty2_textbox.grid(column=1, row=6)
uncertainty2_textbox.insert(0, '0')

value2 = Label(window, text='Value', font=('Arial', 10))
value2.grid(column=2, row=6)

value2_textbox = Entry(window, width=10)
value2_textbox.grid(column=3, row=6)
value2_textbox.insert(0, '1')

main3 = Label(window, text='Answer Variable', font=('Arial', 12))
main3.grid(column=0, row=7)

answer = Label(window, text='Answer:', font=('Arial', 10))
answer.grid(column=2, row=8)

answer_textbox = Entry(window, width=10)
answer_textbox.grid(column=3, row=8)
answer_textbox.insert(0, '0')

rtn = Label(window, text='Uncertainty is:', font=('Arial', 12))
rtn.grid(column=5, row=11)

btn = Button(window, text='Calculate', command=clicked)

btn.grid(column=0, row=10)

window.geometry('800x300')
window.bind('<Return>', callback)

# txt = Entry(window, width=10)
# txt.grid(column=10, row=10)

window.mainloop()  # waits for any user interaction, else closes
