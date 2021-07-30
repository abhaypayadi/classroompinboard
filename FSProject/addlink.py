from tkinter import *
import subprocess
root=Tk()
root.title("ClassRoom Pinboard")
root.geometry("1199x600+100+50")
root.resizable(False,False)
lbl_user=Label(root,text="Select Day to which you have to add event:",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=0,y=0)
my_menu=Menu(root)
root.config(menu=my_menu)
file_menu=Menu(my_menu)
def mondayfun():
    cmd="python3 add.py"
    subprocess.Popen(cmd,shell=True)
def tuesdayfun():
    cmd="python3 add1.py"
    subprocess.Popen(cmd,shell=True)
def wednesdayfun():
    cmd="python3 add2.py"
    subprocess.Popen(cmd,shell=True)
def thursdayfun():
    cmd="python3 add3.py"
    subprocess.Popen(cmd,shell=True)
def fridayfun():
    cmd="python3 add4.py"
    subprocess.Popen(cmd,shell=True)
def saturdayfun():
    cmd="python3 add5.py"
    subprocess.Popen(cmd,shell=True)                    
	
my_menu.add_cascade(label="Days",menu=file_menu)
file_menu.add_command(label="Monday",command=mondayfun)
file_menu.add_command(label="Tuesday",command=tuesdayfun)
file_menu.add_command(label="Wednesday",command=wednesdayfun)
file_menu.add_command(label="Thursday",command=thursdayfun)
file_menu.add_command(label="Friday",command=fridayfun)
file_menu.add_command(label="Saturday",command=saturdayfun)
root.mainloop()