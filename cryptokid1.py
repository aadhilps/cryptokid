# %%
import hashlib
import base64
from tkinter import *
from tkinter import messagebox
import os
from cryptography.fernet import Fernet

# %%


# %%

masterpassword = ""  # set the master password


def key_from_password(password):
    salt = b""  # give your own value for the salt
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 390000)
    return base64.urlsafe_b64encode(hashed)


def encrypt():
    password = code.get()

    if password == "":
        messagebox.showerror("ERROR", "input the password!")
        return
    elif password == masterpassword:

        enc_key = key_from_password(password)
        cipher = Fernet(enc_key)

        screen1 = Toplevel(screen)
        screen1.title("lacle")
        screen1.iconbitmap("lacle.ico")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END).strip().encode()
        encrypted = cipher.encrypt(message).decode()

        Label(text="encrypted text", fg="black", bg="white",
              font=("calibri", 13)).place(x=10, y=10)
        text2 = Text(screen1, font="robote 20", bg="white",
                     relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=50, height=100, width=340)
        text2.insert(END, encrypted)

    elif password != masterpassword:
        messagebox.showerror("ERROR", "wrong password!")


def decrypt():
    password = code.get()

    if password == "":
        messagebox.showerror("Error", "Enter a password")
        return

    elif password == masterpassword:
        enc_key = key_from_password(password)
        cipher = Fernet(enc_key)

        screen2 = Toplevel(screen)
        screen2.title("lacle")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")
        screen2.iconbitmap("lacle.ico")

        encrypted_message = text1.get(
            "1.0", "end-1c").encode().replace(b"\n", b"")

        try:
            decrypted = cipher.decrypt(encrypted_message).decode()
        except:
            decrypted = "INVALID PASSWORD OR CORRUPTED DATA"

        Label(screen2, text="Decrypted Text", bg="#00bd56",
              fg="white", font="Arial").place(x=10, y=0)
        text3 = Text(screen2, font="robote 10", bg="white",
                     relief=GROOVE, wrap=WORD, bd=0)
        text3.place(x=10, y=40, height=100, width=340)

        text3.insert(END, decrypted)


def main_screen():
    global text1
    global screen
    global code

    screen = Tk()
    screen.title("lacle")
    screen.geometry("375x398")
    screen.iconbitmap("lacle.ico")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Input the text for encryption or decryption",
          fg="black", font=("calbri", 13)).place(x=10, y=10)
    text1 = Text(font="robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Input password", fg="black",
          font=("calibri", 13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, bg="white",
          font="arial", show="*").place(x=10, y=200)

    Button(text="encrypt", fg="white", bg="red", height="2",
           width=23, bd=0, command=encrypt).place(x=10, y=250)
    Button(text="decrypt", fg="white", bg="green", height="2",
           width=23, bd=0, command=decrypt).place(x=200, y=250)
    Button(text="reset", fg="white", bg="blue", height="2",
           width=50, command=reset, bd=0).place(x=10, y=300)
    screen.mainloop()


main_screen()

# %%
