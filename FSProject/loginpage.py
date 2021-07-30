from tkinter import*
import subprocess
from PIL import ImageTk 
from tkinter import messagebox
root=Tk()
root.title("ClassRoom Pinboard")
root.geometry("1199x600+100+50")
root.resizable(False,False)
bg=ImageTk.PhotoImage(file="sample.png")
def link():
    cmd="python3 home.py"
    subprocess.Popen(cmd,shell=True)


bg_image=Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
Frame_name=Frame(root,bg="white")
Frame_name.place(x=150,y=50,height=30,width=210)
project_name=Label(Frame_name,text="ClassRoom Pinboard",font=("Lucida Calligraphy",20,"bold"),fg="#d77337").place(x=0,y=0)
Frame_login=Frame(root,bg="white")
Frame_login.place(x=150,y=150,height=340,width=500)
title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
desc=Label(Frame_login,text="JSSATE-B Student Database",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)
lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
txt_user.place(x=90,y=170,width=350,height=35)
lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
txt_pass.place(x=90,y=240,width=350,height=35)
forget_btn=Button(Frame_login,text="Forget Password?",cursor="hand2",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=280)
def login_function():
        if txt_pass.get()=="" or txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=root)
        elif txt_pass.get()!="123" or txt_user.get()!="1js18is001":
            messagebox.showerror("Error","Invalid Username/Password",parent=root)
        else:
            messagebox.showinfo("Welcome",f"Welcome {txt_user.get()}\nYour Password: {txt_pass.get()}",parent=root)
            Confirm_btn=Button(root,command=link,cursor="hand2",text="Continue",fg="black",bg="#d77337",font=("times new roman",20)).place(x=400,y=470,width=180,height=40)


Login_btn=Button(root,command=login_function,cursor="hand2",text="Login",fg="black",bg="#d77337",font=("times new roman",20)).place(x=200,y=470,width=180,height=40)





























root.mainloop()          
