from tkinter import *
import socket
import os
import time
from tkinter import messagebox
from tkinter import filedialog
import tkinter
from traceback import format_tb
root=Tk()
root.title("File Share")
root.geometry("300x300")
root.config(bg="#189AB4")
root.resizable(False,False)
Label(root,text="FILE TRANSFER",font=("montserrat",16,'bold'),bg="#f4f5f6").place(x=70,y=20)
def Send():
    b=Toplevel(root)
    b.title("SENDER")
    b.geometry("300x250")
    b.config(back="#7DF9FF")
    def open():
        global file
        file=filedialog.askopenfile(parent=b,mode='rb',title="Chose file")
        if file:
            tb=tkinter.Text(b,height=1,width=27)
            tb.insert(1.0,"LOADING COMPLETE")
            tb.place(x=50,y=150)
        else:
            tb=tkinter.Text(b,height=1,width=10)
            tb.insert(1.0,"ERROR WHILE LOADING")
            tb.place(x=50,y=150)
            print(file)
    def sent():
         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         sock.bind((socket.gethostname(), 22222))
         sock.listen(1)
         print("WAITING FOR CONNECTION")
         client,addr = sock.accept()
         data=file.read(4096)
         while data:
             client.send(data)
             data=file.read(4096)
         file.close()
         Label(root,text='File Transfer Complete',bg="#f4f5f4").place(x=90,y=350)
    o=Button(b,text="BROWSE",font=("monserrat",13,'bold'),bg="#7DF9FF",command=open)
    o.place(x=95,y=60)
    sen=Button(b, text="SEND",font=("monserrat",13,'bold'),bg="#7DF9FF",command=sent)
    sen.place(x=110,y=190)
    b.mainloop()
def Receive():
    b=Toplevel(root)
    b.title("RECEIVE")
    b.geometry("300x250")
    b.config(back="#7DF9FF")
    def receiver():
        id=sid.get()
        n=fid.get()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((id,22222))
        f=open( n, "wb")
        data = sock.recv(4096)
        while data:
            f.write(data)
            data=sock.recv(4096)
        f.close()
        tb=tkinter.Text(b,height=1,width=27)
        tb.insert(1.0,"FILE RECEIVED")
        tb.place(x=50,y=150)
    Label(b,text="SENDERS ID",font=("monserrat",12,'bold'),bg="#3AA8C1").place(x=20,y=0)
    sid=Entry(b,width=25,fg='Black',bg='White',font=('Arial',10))
    sid.place(x=20,y=28) 
    Label(b,text="FILE NAME",font=("monserrat",12,'bold'),bg="#3AA8C1").place(x=20,y=50)
    fid=Entry(b,width=25,fg='Black',bg='White',font=('Arial',10))
    fid.place(x=20,y=78)
    rr=Button(b,text="RECEIVE",compound=LEFT ,font=("monserrat",10),bg='#7DF9FF',command=receiver)
    rr.place(x=20,y=120)
    b.mainloop()
send=Button(root,text="SEND",font=("monserrat",13,'bold'),bg="#7DF9FF",command=Send).place(x=70,y=100)
recrive=Button(root,text="RECEIVE",font=("monserrat",13,'bold'),bg="#7DF9FF",command=Receive).place(x=150,y=100)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(),22222))
host=sock.getsockname()
sock.close()
Label(root,text=f'ID: {host}',bg="#f4f5f4").place(x=90,y=200)


root.mainloop()
