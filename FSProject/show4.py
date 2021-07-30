from tkinter import *
from tkinter import filedialog, messagebox, ttk
import pandas as pd

root = Tk()
root.geometry("1199x600+100+50") 
root.title("Friday TimeTable")
root.resizable(0, 0)
frame=Frame(root,bg="white")
frame.pack()
tv = ttk.Treeview(frame)
df=pd.read_excel("/Users/abhaypayadi/Desktop/FSProject/dataset/friday.xlsx")
tv["column"]=list(df.columns)
tv["show"]="headings"
for column in tv["column"]:
	tv.heading(column,text=column)
df_rows=df.to_numpy().tolist()
for row in df_rows:
	tv.insert("","end",values=row)
tv.pack()	



















root.mainloop()	