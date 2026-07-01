# text editor app.
#thinker module and library
#import tkinter for creating GUI app
# from tkinter.messagebox import showinfo
# from tkinter import font
# import tkinter as tick
# from tkinter import filedialog , messagebox

# root=tick.Tk()
# root.title('Editors Game')
# root.geometry('800x600')

# text=tick.Text(
#     root,
#     wrap=tick.WORD,
#     font=('Helvetica',12)
# )
# text.pack(expand=True,fill=tick.BOTH)

# def new():
#     text.delete(1.0,tick.END)

# def opn():
#     filepath=filedialog.askopenfilename(
#         defaultextension='.txt',
#         filetypes=[('Text Files','*.txt')]
#     )
#     if filepath:
#         with open(filepath,'r') as file:
#             text.delete(1.0,tick.END)
#             text.insert(tick.END,file.read())

# def savefile():
#     filepath=filedialog.asksaveasfilename(
#         defaultextension='.txt',
#         filetypes=[('Text Files','*.txt')]
#     )
#     if filepath:
#         with open(filepath,'w') as file:
#             file.write(text.get(1.0,tick.END))

#     messagebox.showinfo('info','file saved successfully')

# menu=tick.Menu(root)
# root.config(menu=menu)
# filemenu=tick.Menu(menu)

# menu.add_cascade(label='File',menu=filemenu)

# filemenu.add_command(label='new',command=new)
# filemenu.add_command(label='open',command=open)
# filemenu.add_command(label='save',command=savefile)
# filemenu.add_separator()
# filemenu.add_command(label='Exit',command=root.quite
# 
#  
# root.mainloop()