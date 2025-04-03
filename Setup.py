import tkinter as tk
from tkinter.filedialog import askopenfilename

f = open("Info.txt", "r")
text = f.read().splitlines()

window = tk.Tk()
window.title("Discord Status Generator Setup")

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

lbl_authtoken = tk.Label(master=frm_form, text="Discord AuthToken:")
ent_authtoken = tk.Entry(master=frm_form, width=100)
ent_authtoken.insert(0, text[0])
lbl_authtoken.grid(row=0, column=0, sticky="e")
ent_authtoken.grid(row=0, column=1)

lbl_status = tk.Label(master=frm_form, text="Status Message:")
ent_status = tk.Entry(master=frm_form, width=100)
lbl_status.grid(row=1, column=0, sticky="e")
ent_status.grid(row=1, column=1)

btn_status_file = tk.Button(master=frm_form, text="Status Python File:")
lbl_status_file = tk.Label(master=frm_form, width=100)
btn_status_file.grid(row=2, column=0, sticky="e")
lbl_status_file.grid(row=2, column=1)

if text[1][0] == "n":
    ent_status.insert(0, text[1][1:])
elif text[1][0] == "f":
    lbl_status_file.config(text=text[1][1:])

lbl_emoji = tk.Label(master=frm_form, text="Emoji Id:")
ent_emoji = tk.Entry(master=frm_form, width=100)
lbl_emoji.grid(row=3, column=0, sticky="e")
ent_emoji.grid(row=3, column=1)

btn_emoji_file = tk.Button(master=frm_form, text="Emoji Id Python File:")
lbl_emoji_file = tk.Label(master=frm_form, width=100)
btn_emoji_file.grid(row=4, column=0, sticky="e")
lbl_emoji_file.grid(row=4, column=1)

if text[2][0] == "n":
    ent_emoji.insert(0, text[2][1:])
elif text[2][0] == "f":
    lbl_emoji_file.config(text=text[2][1:])

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

events = []

def submit_click(event):
    text[0] = ent_authtoken.get()
    
    if ent_status.get() != "":
        text[1] = "n" + ent_status.get()
    else:
        text[1] = "f" + lbl_status_file['text']

    if ent_emoji.get() != "":
        text[2] = "n" + ent_emoji.get()
    else:
        text[2] = "f" + lbl_emoji_file['text']

    f = open("Info.txt", "w")
    f.write("\n".join(text))
    window.destroy()

def status_file_click(event):
    filename = askopenfilename()
    lbl_status_file.config(text=filename)

def emoji_file_click(event):
    filename = askopenfilename()
    lbl_emoji_file.config(text=filename)

btn_submit.bind("<Button-1>", submit_click)
btn_status_file.bind("<Button-1>", status_file_click)
btn_emoji_file.bind("<Button-1>", emoji_file_click)

window.mainloop()
