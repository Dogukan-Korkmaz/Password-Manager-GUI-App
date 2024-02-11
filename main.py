from tkinter import *
from tkinter import messagebox
from gen_pass import generate_password
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def write_new_password():
    if len(entry_pass.get()) == 0:
        entry_pass.insert(0, generate_password())
    else:
        entry_pass.delete(0, END)
        entry_pass.insert(0, generate_password())

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():

    get_mail = entry_mail.get()
    get_web = entry_web.get()
    get_pass = entry_pass.get()

    if len(get_pass) == 0 or len(get_web) == 0:
        messagebox.showwarning(title="Missing İnput Error", message="You must fill all boxes !")
    else:
        is_ok = messagebox.askyesno(title=get_web, message=f"These are the the detailes entered: \nEmail: {get_mail}"
                                                   f"\nPassword: {get_pass}\nIs it ok to save ?")

        if is_ok and get_pass is not None and get_web is not None:
            with open("data.txt", "a") as file:
                file.write(f"\n{get_web} | {get_mail} | {get_pass}")
                entry_pass.delete(0, END)
                entry_web.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=False)
tomato = PhotoImage(file="logo.png")
canvas.create_image((100, 100), image=tomato)
canvas.grid(row=0, column=1)


label_web = Label(text="Website:")
label_web.grid(row=1, column=0)

entry_web = Entry(width=35)
entry_web.focus()
entry_web.grid(row=1, column=1, columnspan=2)

label_mail = Label(text="Email/Username:")
label_mail.grid(row=2, column=0)

entry_mail = Entry(width=35)
entry_mail.grid(row=2, column=1, columnspan=2)
entry_mail.insert(0, "dkorkmaz2000@hotmail.com")

label_pass = Label(text="Password:")
label_pass.grid(row=3, column=0)

entry_pass = Entry(width=27)
entry_pass.grid(row=3, column=1)

button_gpass = Button(text="Generate Password", command=write_new_password)
button_gpass.grid(row=3, column=2)

button_add = Button(width=29, text="Add", command=save_data)
button_add.grid(row=4, column=1, columnspan=2)



window.mainloop()
