from tkinter import *
import sqlite3

root = Tk()
root.geometry('800x800')
root.title("Registration Form")


Fullname=StringVar()
Email=StringVar()
var = IntVar()
c=StringVar()
var1= IntVar()
re=StringVar()
typ=StringVar()
skil=StringVar()
per=IntVar()
samples=StringVar()


def database():
   name1=Fullname.get()
   reg=re.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   prog=var1.get()
   toi=typ.get()
   skills=skil.get()
   work=samples.get()
   peroid=per.get()

   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,REGNO TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT,TYPE_OF_INTERNSHIP TEXT,SKILLS TEXT,WORK_SAMPLES TEXT,PEROID_OF_INTERNSHIP TEXT)')
   cursor.execute('INSERT INTO Student (FullName,REGNO,Email,Gender,country,Programming,TYPE_OF_INTERNSHIP,SKILLS,WORK_SAMPLES,PEROID_OF_INTERNSHIP) VALUES(?,?,?,?,?,?,?,?,?,?)',(name1,reg,email,gender,country,prog,toi,skills,work,peroid,))
   conn.commit()
   
   
             
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=60,y=90)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=90)

label_2 = Label(root, text="Registration Number",width=20,font=("bold", 10))
label_2.place(x=80,y=130)

entry_2 = Entry(root,textvar=re)
entry_2.place(x=240,y=130)

label_3 = Label(root, text="Email",width=20,font=("bold", 10))
label_3.place(x=68,y=180)

entry_3 = Entry(root,textvar=Email)
entry_3.place(x=240,y=180)

label_4 = Label(root, text="Gender",width=20,font=("bold", 10))
label_4.place(x=70,y=230)

Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_5 = Label(root, text="country",width=20,font=("bold", 10))
label_5.place(x=70,y=280)

list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your country') 
droplist.place(x=240,y=280)

label_6 = Label(root, text="Programming",width=20,font=("bold", 10))
label_6.place(x=85,y=330)
var2= IntVar()
Checkbutton(root, text="java", variable=var1).place(x=235,y=330)

Checkbutton(root, text="python", variable=var2).place(x=290,y=330)

label_7 = Label(root, text="Type of internship",width=20,font=("bold", 10))
label_7.place(x=92,y=380)

entry_7 = Entry(root,textvar=typ)
entry_7.place(x=240,y=380)

label_8 = Label(root, text="Skills",width=20,font=("bold", 10))
label_8.place(x=101,y=430)

entry_8 = Entry(root,textvar=skil)
entry_8.place(x=240,y=430)

label_9 = Label(root, text="Work Samples",width=20,font=("bold", 10))
label_9.place(x=110,y=480)

entry_9 = Entry(root,textvar=samples)
entry_9.place(x=240,y=480)

label_10= Label(root, text="Period of internship",width=20,font=("bold", 10))
label_10.place(x=125,y=530)

entry_10 = Entry(root,textvar=per)
entry_10.place(x=240,y=530)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=580)

root.mainloop()
