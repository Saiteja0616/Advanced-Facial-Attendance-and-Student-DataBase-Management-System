from tkinter import*   
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"College_Images\dev3.jpg")
        img_top=img_top.resize((1532,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1532,height=720)


        #===Frame===
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)


        img_1=Image.open(r"College_Images\lucky.jpeg")
        img_1=img_1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        f_lbl=Label(main_frame,image=self.photoimg_1)
        f_lbl.place(x=300,y=0,width=200,height=200)

        #Developer info
        dev_label=Label(main_frame,text="Hello my name is Sai Teja Punnam",font=("times new roman",15,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="Iam a Computer Science Student ",font=("times new roman",15,"bold"),fg="blue")
        dev_label.place(x=0,y=40)


        img_2=Image.open(r"College_Images\dev2.jpg")
        img_2=img_2.resize((500,390),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        f_lbl=Label(main_frame,image=self.photoimg_2)
        f_lbl.place(x=0,y=210,width=500,height=390)


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
    
