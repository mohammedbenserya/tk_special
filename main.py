
from datetime import datetime
from tkinter import *
from tkinter import ttk
from tkinter.tix import NoteBook
from tkcalendar import *
import sqlite3,re
from turtle import width
import tkinter.ttk as ttk
from fpdf import FPDF
from tkinter import messagebox,filedialog
root =Tk()
root.title('PDF Generator')

root.geometry('700x850')


def submit_emp():

    conn=sqlite3.connect('database.db')
# Create cursor
    c = conn.cursor ()
    c.execute('INSERT INTO employe VALUES(:nom,:prenom)',{
        'nom': nom.get(),
        'prenom':prenom.get()
    })
    nom.delete(0,END)
    prenom.delete(0,END)
    conn.commit()
    c.execute('SELECT * FROM employe')

    result=c.fetchall()
    if len(result)>0:
        
        
        ce = StringVar()

        ce.set(result[0])

        notebook1= ttk.Notebook(root)
        notebook1.grid(row=1,pady=20,padx=20,sticky = W)
        my_frame1 = Frame(notebook1)

        my_frame1.pack(fill="both", expand=1)

        notebook1.add (my_frame1)
        cb = OptionMenu(my_frame1,ce,*result)
        cb.grid(row=0,column=1,padx=20)
        cb.configure(width=20)

        cb_lab= Label(my_frame1,text = 'Choisir un Employe :')
        cb_lab.grid(row = 0, column= 0,padx=20,pady=20,sticky = W)
    conn.close()
def submit_lieu():
    
    conn=sqlite3.connect('database.db')
    c = conn.cursor ()
    c.execute('INSERT INTO lieu VALUES(:ville,:adress)',{
        'ville': lieu.get(),
        'adress': adress.get(),
    })
    conn.commit()
    lieu.delete(0,END)
    adress.delete(0,END)
    cursor.execute('SELECT * FROM lieu')

    result=cursor.fetchall()
    cb1(result)

    cb2(result)
    conn.close()
    
notebook0= ttk.Notebook(root)
notebook0.grid(row=0,pady=20,padx=20,sticky = W)
my_frame1 = Frame(notebook0, width=900, height=200)
my_frame2=Frame(notebook0, width=900, height=200)
my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)
notebook0.add (my_frame1, text="Ajouter employe")
notebook0.add(my_frame2, text="Ajouter Lieu")
nom = Entry(my_frame1,width=30)
nom.grid(row=0,column=1,sticky = W)
prenom = Entry(my_frame1,width=30)
prenom.grid(row=0,column=3,padx=20)
nom_lab= Label(my_frame1,text = 'Nom :')
nom_lab.grid(row = 0, column= 0,sticky = W,padx=20,pady=20)
prenom_lab= Label(my_frame1,text = 'Prenom :')
prenom_lab.grid(row = 0, column= 2)
submit_btn = Button(my_frame1 ,text='Ajouter employe',command=submit_emp)
submit_btn.grid(row=1,column=2,padx=20,pady=20) 
lieu = Entry(my_frame2,width=30)
lieu.grid(row=0,column=1,padx=20,pady=20)
lieu_lab= Label(my_frame2,text = 'Ville :')
lieu_lab.grid(row = 0, column= 0,padx=20,sticky = W)
adress = Entry(my_frame2,width=50)
adress.grid(row=1,column=1,padx=20)
adress_lab= Label(my_frame2,text = 'Adresse :')
adress_lab.grid(row =1, column= 0,padx=20,sticky = W)
submit_lieu = Button(my_frame2 ,text='Ajouter Lieu',command=submit_lieu)
submit_lieu.grid(row=2,column=3,pady=20) 
db = sqlite3.connect('database.db')
cursor=db.cursor()
cursor.execute('SELECT * FROM employe')

result=cursor.fetchall()

if len(result)>0:
        
        
        ce = StringVar()

        ce.set(result[0])

        notebook1= ttk.Notebook(root)
        notebook1.grid(row=1,pady=20,padx=20,sticky = W)
        my_frame1 = Frame(notebook1)

        my_frame1.pack(fill="both", expand=1)

        notebook1.add (my_frame1)
        cb = OptionMenu(my_frame1,ce,*result)
        cb.grid(row=0,column=1,padx=20)
        cb.configure(width=20)

        cb_lab= Label(my_frame1,text = 'Choisir un Employe :')
        cb_lab.grid(row = 0, column= 0,padx=20,pady=20,sticky = W)

notebook= ttk.Notebook(root)
notebook.grid(row=2,padx=20,sticky = W)
my_frame1 = Frame(notebook)
my_frame2=Frame(notebook)
my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)
notebook.add (my_frame1, text="Depart/Arrive")
notebook.add(my_frame2, text="Jour De Travail")

def submit_da(c1,c2,t1,t2,cal):
    listBox.insert("end", datetime.strptime(cal.get(),"%d/%m/%Y").strftime('%d %B')+' :')
    listBox.insert("end",c1.get()+' - '+c2.get()+' ('+t1.get()+' - '+t2.get()+')')

cursor.execute('SELECT * FROM lieu')

result=cursor.fetchall()


def cb2(result):
    if len(result)>0:
        data=[]
        for row in result:
                data.append(row[0])
        c1 = StringVar()

        c1.set(data[0])
        cb2 = OptionMenu(my_frame1,c1,*data)
        cb2.grid(row=1,column=1,pady=20,columnspan=1)
        cb2.configure(width=20)
        cb_lab2= Label(my_frame1,text = "Choisir Ville d'arrive :")
        cb_lab2.grid(row = 1, column= 0,padx=20,pady=20,sticky = W)
        time_picker1 = Entry(my_frame1,width=20)
        time_picker1.grid(row=0,column=3,pady=20,padx=20)
        cb_lab2= Label(my_frame1,text = "Date depart :")
        cb_lab2.grid(row = 0, column=2,pady=20,sticky = W,padx=20)
        data=[]
        for row in result:
                data.append(row[0])
        c2 = StringVar()

        c2.set(data[0])
        cb1 = OptionMenu(my_frame1,c2,*data)
        cb1.configure(width=20)
        cb1.grid(row=0,column=1,pady=20)
        cb_lab1= Label(my_frame1,text = 'Choisir Ville depart :')
        cb_lab1.grid(row = 0, column= 0,padx=20,pady=20,sticky = W)
        time_picker2 = Entry(my_frame1,width=20)
        time_picker2.grid(row=1,column=3,pady=20,padx=20)
        cb_lab2= Label(my_frame1,text = "Date d'arrive :")
        cb_lab2.grid(row = 1, column=2,pady=20,padx=20,sticky = W)

        cal_lab2= Label(my_frame1,text = "Jour depart :")
        cal_lab2.grid(row = 2, column=0,padx=20,sticky = W)
        cal=DateEntry(my_frame1,selectmode='day') 
        cal.grid(row = 2, column=1,pady=20,sticky = W)

        da_btn = Button(my_frame1 ,text='Ajouter Depart/Arrive',command=lambda: submit_da(c1,c2,time_picker1,time_picker2,cal))
        da_btn.grid(row=2,column=2,pady=20)
cb2(result)
    # Create table

# theme = AnalogThemes(time_picker)
# theme.setDracula()
list=[]
def submit_jt(cal,clicked):
        
        listBox.insert("end", datetime.strptime(cal.get(),"%d/%m/%Y").strftime('%d %B')+' : JOUR DE TRAVAIL '+clicked.get().split(':')[0])
        list.append(clicked.get())
cursor.execute('SELECT * FROM lieu')

result=cursor.fetchall()
def cb1(result):
    if len(result)>0:
        data=[]
        for row in result:
                data.append(row[1])
        clicked = StringVar()
        clicked.set(data[0])
        cb1 = OptionMenu(my_frame2,clicked,*data)
        cb1.configure(width=20)
        cb1.grid(row=0,column=1,pady=20)
        cb_lab1= Label(my_frame2,text = 'Choisir Ville De travaill :')
        cb_lab1.grid(row = 0, column= 0,padx=20,pady=20,sticky = W)
        cal_lab2= Label(my_frame2,text = "Date De travail :")
        cal_lab2.grid(row = 1, column=0,padx=20,sticky = W)
        cal=DateEntry(my_frame2,selectmode='day') 
        cal.grid(row = 1, column=1,pady=20,sticky = W)
        jt_btn = Button(my_frame2 ,text='Ajouter Jour de Travail',command=lambda: submit_jt(cal,clicked))
        jt_btn.grid(row=2,column=2,pady=20)
cb1(result)






def gen_pdf():
    res=(listBox.get(0,"end"))
    pdf = FPDF()
  
# Add a page
    pdf.add_page()
    print("DR"+ce.get())
    # set style and size of font 
    # that you want in the pdf
    pdf.set_font("Arial", size = 14)
    pdf.set_text_color(255,0,0)
    pdf.cell(200, 10, txt = "Programme Dr. "+re.sub("[^a-zA-Z]+", " ", ce.get()), 
                    ln = 0, align = 'C')
    pdf.cell(200, 10,   ln=1,align = 'L')
    pdf.cell(200, 10,   ln=2,align = 'L')
    i=3
    for item in res:
    # create a cell
        
        first = item.split(' : ')
        
        if item[-1]==':':
            
            pdf.set_text_color(255,0,0)
            pdf.cell(200, 10, txt = item, 
                    ln = i, align = 'L')
            i+=1
        elif len(first)>1:

            
            pdf.set_text_color(255,0,0)
            pdf.cell(200, 10, txt = first[0]+' :', 
                    ln = i, align = 'L')
            print(first[0])
            pdf.set_text_color(3, 4, 94)
            pdf.cell(200, 10, txt = first[1], 
                    ln = i, align = 'L')
            print(first[1])
            i+=1 
        else:
            pdf.set_text_color(3, 4, 94)
            pdf.cell(200, 10, txt = item, 
                    ln = i, align = 'L')
            i+=1 
    pdf.cell(200, 10,   ln=i,align = 'L')
    pdf.cell(200, 10,   ln=i,align = 'L')
    pdf.cell(200, 10,   ln=i,align = 'L')
    pdf.cell(200, 10,   ln=i,align = 'L')
    pdf.set_font("Arial", size = 10)
    for line in list:
        pdf.set_text_color(3, 4, 94)
        pdf.cell(200, 10,  "Adresse : "+line,0,   ln=i,align = 'L')
        i+=1 
        # add another cell

    
    # save the pdf with name .pdf
    pdf.output("GFG.pdf")
notebook3= ttk.Notebook(root)
notebook3.grid(row=3,padx=20,sticky = W)
my_frame1 = Frame(notebook3, width=650, height=200)

my_frame1.pack(fill="both", expand=1)

notebook3.add (my_frame1)

listBox = Listbox(my_frame1,width = 100, 
                                      height = 10)
listBox.grid(row=0,column=0)
gen_btn = Button(my_frame1 ,text='gen pdf',command=gen_pdf)
gen_btn.grid(row=1,column=0,pady=20)
"""pdf = FPDF()
  
# Add a page
pdf.add_page()
  
# set style and size of font 
# that you want in the pdf
pdf.set_font("Arial", size = 15)
  
# create a cell
pdf.cell(200, 10, txt = "GeeksforGeeks", 
         ln = 1, align = 'C')
  
# add another cell
pdf.cell(200, 10, txt = "A Computer Science portal for geeks.",
         ln = 2, align = 'C')
  
# save the pdf with name .pdf
pdf.output("GFG.pdf")"""
'''c.execute("""CREATE TABLE employe (
 nom text,
 prenom text
 )""")
c.execute("""CREATE TABLE lieu (
 lieu text
 )""")
#Commit Changes
conn.commit()'''
# Close Connection

root.mainloop()