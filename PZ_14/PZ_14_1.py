#В соответствии с номером варианта перейти по ссылке на прототип. Реализовать его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально приближенный к оригиналу.
from tkinter import *

def submit_form(event):
    print(e_user.get(), e_mail.get(), e_pass.get(), e_alam.get(), e_tgl.get(), e_usia.get(), var_gen.get(), var_chk.get())

def reset_form(event):
    for w in [e_user, e_mail, e_pass, e_alam, e_tgl, e_usia]:
        w.delete(0, END)
    var_gen.set(0)
    var_chk.set(0)
    set_ph(e_user, "username anda")
    set_ph(e_mail, "alamat email")
    set_ph(e_alam, "alamat rumah")
    set_ph(e_tgl, "mm/dd/yyyy")
    set_ph(e_usia, "usia anda")

def set_ph(ent, txt):
    ent.insert(0, txt)
    ent.config(fg="gray")
    ent.bind("<FocusIn>", lambda e: ent.delete(0, END) if ent.get() == txt and ent["fg"] == "gray" else None)
    ent.bind("<FocusOut>", lambda e: ent.insert(0, txt) if ent.get() == "" else None)

root = Tk()
root.title("Belajar Form")
root.geometry("550x330")

f1 = LabelFrame(root, text="User login info", bd=2)
f1.pack(fill=X, padx=10, pady=5)

Label(f1, text="Username:").grid(row=0, column=0, sticky=W, pady=2)
e_user = Entry(f1, width=25)
e_user.grid(row=0, column=1, sticky=W, pady=2)
set_ph(e_user, "username anda")

Label(f1, text="Email:").grid(row=1, column=0, sticky=W, pady=2)
e_mail = Entry(f1, width=25)
e_mail.grid(row=1, column=1, sticky=W, pady=2)
set_ph(e_mail, "alamat email")

Label(f1, text="Password:").grid(row=2, column=0, sticky=W, pady=2)
e_pass = Entry(f1, width=25)
e_pass.grid(row=2, column=1, sticky=W, pady=2)

f2 = LabelFrame(root, text="Data diri", bd=2)
f2.pack(fill=X, padx=10, pady=5)

Label(f2, text="Alamat:").grid(row=0, column=0, sticky=W, pady=2)
e_alam = Entry(f2, width=25)
e_alam.grid(row=0, column=1, sticky=W, pady=2)
set_ph(e_alam, "alamat rumah")

Label(f2, text="Tanggal lahir:").grid(row=1, column=0, sticky=W, pady=2)
e_tgl = Entry(f2, width=25)
e_tgl.grid(row=1, column=1, sticky=W, pady=2)
set_ph(e_tgl, "mm/dd/yyyy")

Label(f2, text="Usia:").grid(row=2, column=0, sticky=W, pady=2)
e_usia = Entry(f2, width=25)
e_usia.grid(row=2, column=1, sticky=W, pady=2)
set_ph(e_usia, "usia anda")

Label(f2, text="Jenis kelamin:").grid(row=3, column=0, sticky=W, pady=2)
var_gen = IntVar()
Radiobutton(f2, text="Pria", variable=var_gen, value=1).grid(row=3, column=1, sticky=W, padx=5)
Radiobutton(f2, text="Wanita", variable=var_gen, value=2).grid(row=3, column=1, sticky=W, padx=80)

f3 = LabelFrame(root, text="", bd=2)
f3.pack(fill=X, padx=10, pady=5)

var_chk = IntVar()
Checkbutton(f3, text="Saya bersedia mengikuti aturan forum", variable=var_chk).pack(anchor=W, padx=5, pady=5)

f4 = Frame(f3)
f4.pack(anchor=W, padx=5, pady=5)

btn_reset = Button(f4, text="Reset", width=10)
btn_reset.pack(side=LEFT, padx=2)
btn_reset.bind("<Button-1>", reset_form)

btn_submit = Button(f4, text="submit", width=10)
btn_submit.pack(side=LEFT, padx=2)
btn_submit.bind("<Button-1>", submit_form)

root.mainloop()
