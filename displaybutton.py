# button formation with python module tkinter.
import tkinter as tk

root=tk.Tk()
root.geometry("400x500")
# pack wise button formation.
b1=tk.Button(root,text= "widget 1",bg= "green")
b2=tk.Button(root,text= "widget 2",bg="blue")
b3=tk.Button(root,text= "widget 3",bg="red")

b1.pack(side=tk.TOP,fill=tk.X,padx=6,pady=6)
b2.pack(side=tk.TOP,fill=tk.X,padx=6,pady=6)
b3.pack(side=tk.TOP,fill=tk.X,padx=6,pady=6)

b1.pack(side=tk.BOTTOM,fill=tk.X,padx=6,pady=6)
b2.pack(side=tk.BOTTOM,fill=tk.X,padx=6,pady=6)
b3.pack(side=tk.BOTTOM,fill=tk.X,padx=6,pady=6)

b1.pack(side=tk.LEFT,fill=tk.Y,padx=6,pady=6)
b2.pack(side=tk.LEFT,fill=tk.Y,padx=6,pady=6)
b3.pack(side=tk.LEFT,fill=tk.Y,padx=6,pady=6)

b1.pack(side=tk.RIGHT,fill=tk.Y,padx=6,pady=6)
b2.pack(side=tk.RIGHT,fill=tk.Y,padx=6,pady=6)
b3.pack(side=tk.RIGHT,fill=tk.Y,padx=6,pady=6)

#grid wise button formation.
# types to represent:-  
# 1) stacks (rows & columns):- top button , left button
# 2) 2x2 layout with span:- bottom button
# 3) offset matrix:- right button

b1=tk.Button(root,text= "widget 1",bg= "green")
b2=tk.Button(root,text= "widget 2",bg="blue")
b3=tk.Button(root,text= "widget 3",bg="red")
# TOP
 b1.grid(row=0,column=0,sticky="ew",padx=6,pady=6)
 b2.grid(row=1,column=0,sticky="ew",padx=6,pady=6)
 b3.grid(row=2,column=0,sticky="ew",padx=6,pady=6)
root.grid_columnconfigure(0,weight=1)
# BOTTOM
 b1.grid(row=0,column=0,sticky="nsew",padx=6,pady=6)
 b2.grid(row=0,column=1,sticky="nsew",padx=6,pady=6)
 b3.grid(row=1,column=0,columnspan=2,sticky="nsew",padx=6,pady=6)
 root.grid_rowconfigure((0,1),weight=1)
 root.grid_columnconfigure((0,1),weight=1)
#LEFT
b1.grid(row=0,column=0,sticky="ns",padx=6,pady=6)
b2.grid(row=0,column=1,sticky="ns",padx=6,pady=6)
b3.grid(row=0,column=2,sticky="ns",padx=6,pady=6)
root.grid_rowconfigure(0,weight=1)
#RIGHT
b1.grid(row=0,column=0,sticky="nsew",padx=6,pady=6)
b2.grid(row=1,column=1,sticky="nsew",padx=6,pady=6)
b3.grid(row=2,column=2,sticky="nsew",padx=6,pady=6)
#root.grid_rowconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)
root.mainloop()
