from tkinter import *
import subprocess
root=Tk()
root.title("ClassRoom Pinboard")
root.geometry("1199x600+100+50")
root.resizable(False,False)
lbl_user=Label(root,text="Select Days of TimeTable to be displayed:",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=0,y=0)
my_menu=Menu(root)
root.config(menu=my_menu)
file_menu=Menu(my_menu)
def mondayfun():
    cmd="python3 show.py"
    subprocess.Popen(cmd,shell=True)
def tuesdayfun():
    cmd="python3 show1.py"
    subprocess.Popen(cmd,shell=True)
def wednesdayfun():
    cmd="python3 show2.py"
    subprocess.Popen(cmd,shell=True)
def thursdayfun():
    cmd="python3 show3.py"
    subprocess.Popen(cmd,shell=True)
def fridayfun():
    cmd="python3 show4.py"
    subprocess.Popen(cmd,shell=True)
def saturdayfun():
    cmd="python3 show5.py"
    subprocess.Popen(cmd,shell=True)                    
	
my_menu.add_cascade(label="Days",menu=file_menu)
file_menu.add_command(label="Monday",command=mondayfun)
file_menu.add_command(label="Tuesday",command=tuesdayfun)
file_menu.add_command(label="Wednesday",command=wednesdayfun)
file_menu.add_command(label="Thursday",command=thursdayfun)
file_menu.add_command(label="Friday",command=fridayfun)
file_menu.add_command(label="Saturday",command=saturdayfun)
root.mainloop()