from tkinter import *
from tkinter import messagebox
from gen_pass import generate_password
import json
# ---------------------------- Search ------------------------------- #


def search_website():
    website = entry_web.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
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
    new_data = {
        get_web: {
            "email": get_mail,
            "password": get_pass,
        }
    }

    if len(get_pass) == 0 or len(get_web) == 0:
        messagebox.showwarning(title="Missing İnput Error", message="You must fill all boxes !")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
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

entry_web = Entry(width=28)
entry_web.focus()
entry_web.grid(row=1, column=1)

button_web = Button(text="Search", command=search_website, width=12)
button_web.grid(row=1, column=2)

label_mail = Label(text="Email/Username:")
label_mail.grid(row=2, column=0)

entry_mail = Entry(width=45)
entry_mail.grid(row=2, column=1, columnspan=2)
entry_mail.insert(0, "dkorkmaz2000@hotmail.com")

label_pass = Label(text="Password:")
label_pass.grid(row=3, column=0)

entry_pass = Entry(width=27)
entry_pass.grid(row=3, column=1)

button_gpass = Button(text="Generate Password", command=write_new_password)
button_gpass.grid(row=3, column=2)

button_add = Button(width=37, text="Add", command=save_data)
button_add.grid(row=4, column=1, columnspan=2)



window.mainloop()
