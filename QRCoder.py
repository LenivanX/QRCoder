from tkinter import *
from tkinter import messagebox
import pyqrcode
import os

# ===|root|===
root = Tk()
root.geometry('500x400')
root.title('QR-Coder')
root.configure(bg='#f7f7f7')
root.wm_iconbitmap('img\\main_ico_3.ico')
root.resizable(False, False)

# ===|utils|===
# --font--
base_font = ('calibri', 13)
footer_font = ('verdana', 8)

# --colors--
label_bgcolor = '#f7f7f7'
button_bgcolor = '#cce4ed'
button_hover_color = '#c2eeff'
active_button_bgcolor = '#dbf5ff'
frame_color = '#f7f7f7'

# --sizes--
label_width = 10
entry_width = 35
button_width = 15

# ===|frames|===
frame_head = Frame(root, bg=frame_color)
frame_head.place(x=0, y=0, relwidth=1, height=50)

frame_main = Frame(root, bg=frame_color)
frame_main.place(x=0, y=50, relwidth=1, height=300)

frame_foot = Frame(root, bg=frame_color)
frame_foot.place(x=0, y=350, relwidth=1, height=50)


# ===|functions|===
# --hover-effects--
def button_generate_enter(x):
    button_generate['bg'] = button_hover_color


def button_generate_exit(x):
    button_generate['bg'] = button_bgcolor


def button_clear_enter(x):
    button_clear['bg'] = button_hover_color


def button_clear_exit(x):
    button_clear['bg'] = button_bgcolor


# --main-functions--
def clear():
    entry_id.delete(0, 'end')
    entry_name.delete(0, 'end')
    entry_msg.delete(0, 'end')


def generate():
    qr_id = entry_id.get()
    qr_name = entry_name.get()
    qr_msg = entry_msg.get()
    qr_data = 'ID:{}\nNAME:{}\nDATA:\n{}'.format(qr_id, qr_name, qr_msg)

    qr_filename = '{}_{}.png'.format(qr_id, qr_name)
    list_of_files = os.listdir()

    if qr_filename in list_of_files:
        messagebox.showinfo('Error', 'Filename already exists!')
    else:
        qr_file = pyqrcode.create(qr_data)
        qr_file.png(qr_filename, scale=10)
        messagebox.showinfo('Success', 'QR Code Generated!')


# ===|layouts|===
# --header--
label_head_msg = Label(frame_head, text='Generate QR Codes', bg=label_bgcolor, font=footer_font)
label_head_msg.place(x=10, y=10)

# --labels--
label_id = Label(frame_main, text='ID', bg=label_bgcolor, font=base_font, width=label_width, anchor=E)
label_id.place(x=40, y=20)

label_name = Label(frame_main, text='Name', bg=label_bgcolor, font=base_font, width=label_width, anchor=E)
label_name.place(x=40, y=80)

label_msg = Label(frame_main, text='Message', bg=label_bgcolor, font=base_font, width=label_width, anchor=E)
label_msg.place(x=40, y=140)

# --entry-boxes--
entry_id = Entry(frame_main, text='', font=base_font, width=entry_width)
entry_id.place(x=140, y=20)

entry_name = Entry(frame_main, text='', font=base_font, width=entry_width)
entry_name.place(x=140, y=80)

entry_msg = Entry(frame_main, text='', font=base_font, width=entry_width)
entry_msg.place(x=140, y=140)

# --buttons--
button_generate = Button(frame_main, text='Generate', font=base_font, width=button_width, bg=button_bgcolor,
                         activebackground=active_button_bgcolor, command=generate, bd=1)
button_generate.place(x=100, y=200)
button_generate.bind('<Enter>', button_generate_enter)  # hover effect
button_generate.bind('<Leave>', button_generate_exit)  # hover effect

button_clear = Button(frame_main, text='Clear', font=base_font, width=button_width, bg=button_bgcolor,
                      activebackground=active_button_bgcolor, command=clear, bd=1)
button_clear.place(x=300, y=200)
button_clear.bind('<Enter>', button_clear_enter)  # hover effect
button_clear.bind('<Leave>', button_clear_exit)  # hover effect

# --footer--
label_version = Label(frame_foot, text='Version: 1.0', width=20, font=footer_font, bg=label_bgcolor, anchor=E)
label_version.place(x=350, y=0)

label_creator = Label(frame_foot, text='Created by: Sayak Nath', width=20, font=footer_font, bg=label_bgcolor, anchor=E)
label_creator.place(x=350, y=15)

# ===|mainloop|===
root.mainloop()
