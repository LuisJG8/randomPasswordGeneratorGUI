from tkinter import *
from tkinter import messagebox
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

letters_password_list = [random.choice(letters) for char in range(nr_letters)]
symbols_password_list = [random.choice(symbols) for chars in range(nr_symbols)]
numbers_password_list = [random.choice(numbers) for charss in range(nr_numbers)]

new_pass = letters_password_list + symbols_password_list + numbers_password_list
random.shuffle(new_pass)

o_pass = "".join(new_pass)

print(o_pass)

def insert_password():
    password_text_box3.insert(0, f"{o_pass}")
    if len(password_text_box3.get()) > 0:
        password_text_box3.delete(0, END)
        password_text_box3.insert(0, f"{o_pass}")
        pyperclip.copy(o_pass)

def save_information():
    website = website_text_box.get()
    email = email_text_box2.get()
    password = password_text_box3.get()

    flag = True
    while flag:
        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Warning", message="Do not leave any fields empty!")
            break
        elif len(website) > 0 or len(password) > 0:
            flag = False

            ok_message = messagebox.askokcancel(title=website, message=f"Information \n\nEmail: {email}, \nPassword: {password} \nIs this ok to save?")
            if ok_message:
                with open("my_passwords.txt", 'a') as my_file:
                    my_file.write(f"{website} | {email} | {password}\n")
                website_text_box.delete(0, END)
                password_text_box3.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)

label1 = Label(text="Website:")
label1.grid(column=0, row=1)

label2 = Label(text="Email/Username:")
label2.grid(column=0, row=2)

label3 = Label(text="Password:")
label3.grid(column=0, row=3)

password_logo = PhotoImage(file="logo.png")
canvas.create_image(112, 112, image=password_logo)
canvas.grid(column=1, row=0)

website_text_box = Entry(width=44)
website_text_box.grid(column=1, row=1, columnspan=2)
website_text_box.focus()

email_text_box2 = Entry(width=44)
email_text_box2.grid(column=1, row=2, columnspan=2)

password_text_box3 = Entry(width=26)
password_text_box3.grid(column=1, row=3)

add_button1 = Button(text="Add", width=37, command=save_information)
add_button1.grid(column=1, row=4, columnspan=2)

label4 = Button(text="Generate Password", command=insert_password)
label4.grid(column=2, row=3)


window.mainloop()