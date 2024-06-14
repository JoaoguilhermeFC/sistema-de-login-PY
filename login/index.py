from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

jan = Tk()
jan.title("DP Systems - Jão")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)

logo = PhotoImage(file="login\icons\logo_anna.png") #carregarimagem dps

LeftFrame = Frame(jan, width=200, height=300, bg="BLACK", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="BLACK", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="BLACK")
LogoLabel.place(x=5, y=10)

UserLabel = Label(RightFrame, text="Username: ", font=("Century Gothic",20), bg="BLACK", fg="white")
UserLabel.place(x=5, y=99)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="Password : ", font=("Century Gothic",20), bg="BLACK", fg="white")
PassLabel.place(x=5, y=149)

PassEntry = ttk.Entry(RightFrame, width=30, show=".")
PassEntry.place(x=150, y=160)

def Login():
    User = UserEntry.get()
    Pass =  PassEntry.get()


    DataBaser.cursor.execute("""
    SELECT * FROM Users WHERE (User = ? and Passaword = ?)
    """, (User, Pass))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if(User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado. Bem Vindo!")
    except:
         messagebox.showinfo(title="Login Info", message="Acesso Negado. Verifique se esta cadastrado no sistema.")


LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y=225)

def Register():
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    NomeLabel = Label(RightFrame, text="Name :", font=("Century Gothic", 20), bg="BLACK", fg="white")
    NomeLabel.place(x=5, y=5)

    NomeEntry = Entry(RightFrame, width=30)
    NomeEntry.place(x=150, y=16)

    EmailLabel = Label(RightFrame, text="E-mail :", font=("Century Gothic", 20), bg="BLACK", fg="white")
    EmailLabel.place(x=5, y=50)

    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x=150, y=59)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if(Name == "" and Email == "" and User =="" and Pass=="" ):
            messagebox.showerror(title="Register error", message="Nõa deix nenhum campo vazio. Preencha todos os campos")
        else:
            DataBaser.cursor.execute("""
        INSERT INTO Users(Name, Email, User, Passaword) VALUES(?, ?, ?, ?)
        """, (Name, Email, User, Pass))
        DataBaser.conn.commit()
        messagebox.showinfo(title="Register Info", message="Conta Criada Com Sucesso")

        

    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDataBase)
    Register.place(x=125, y=230)

    def BackToLogin():
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)

        LoginButton.place(x=5000)
        RegisterButton.place(x=5000)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=155, y=260)

RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=125, y=260)

jan.mainloop()