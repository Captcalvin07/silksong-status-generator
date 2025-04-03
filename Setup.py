import tkinter as tk
from tkinter.filedialog import askopenfilename

window = tk.Tk()
window.title("Discord Status Generator Setup")

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

lbl_authtoken = tk.Label(master=frm_form, text="Discord AuthToken:")
ent_authtoken = tk.Entry(master=frm_form, width=100)
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

lbl_emoji = tk.Label(master=frm_form, text="Emoji Id:")
ent_emoji = tk.Entry(master=frm_form, width=100)
lbl_emoji.grid(row=3, column=0, sticky="e")
ent_emoji.grid(row=3, column=1)

btn_emoji_file = tk.Button(master=frm_form, text="Emoji Id Python File:")
lbl_emoji_file = tk.Label(master=frm_form, width=100)
btn_emoji_file.grid(row=4, column=0, sticky="e")
lbl_emoji_file.grid(row=4, column=1)

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

events = []

def submit_click(event):
    print(ent_authtoken.get())

    status = ent_status.get()
    if ent_status.get() == "":
        status = lbl_status_file['text']
    print(status)

    emoji = ent_emoji.get()
    if ent_emoji.get() == "":
        emoji = lbl_emoji_file['text']
    print(emoji)

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
