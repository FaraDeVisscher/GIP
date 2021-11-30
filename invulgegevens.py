from tkinter import *
import mysql.connector
import re

root= Tk()

#canvas1 = Canvas(root, width = 400, height = 300)
#canvas1.pack()
uitleg = Label(root, text = "Vul u naam en e-mail adres in. Dan krijgt u een nummer")
uitleg.grid(row = 0, column = 0)

naam_invul = Label(root, text = "naam:")
naam_invul.grid(row = 500, column = 0)
gegevens_naam = Entry (root, bd = 5)
gegevens_naam.grid(row = 500, column = 1)

adress_invul = Label(root, text = "e-mail adress:")
adress_invul.grid(row = 501, column = 0)
gegevens_adress = Entry (root, bd = 5)
gegevens_adress.grid(row = 501, column = 1)

#e-mail requerements
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#connecteer met database
my_connect = mysql.connector.connect(
  host="localhost",
  user="root", 
  passwd="",
  database="test_2"
)
my_conn = my_connect.cursor()

    
#klaarbutton
def klbutton():
    naamin = gegevens_naam.get()
    adressin = gegevens_adress.get()

    emailfout = Label(root, text = "foute e-mail")
    ##### check e-mail

    if(re.fullmatch(regex, adressin)):

        print("Valid Email")
        
        emailfout.grid_forget()
        
        add =("INSERT INTO first_test_gip(naam, adress) VALUES(%s,%s)")
        val = (naamin, adressin)
        my_conn.execute(add,val)
        my_connect.commit()

        volgendebutton = Button(root, text='volgende', command=vlgndbutton)
        volgendebutton.grid(row = 503, column = 0)

        klaarbuttun.grid_forget()
    else:

        print("Invalid Email")
        emailfout.grid(row = 504, column = 0)
        
    ##### 

#volgendebutton
def vlgndbutton():
    adressin = gegevens_adress.get()
    my_conn.execute(("SELECT ID FROM first_test_gip WHERE adress = %s"),(adressin,))
    num = my_conn.fetchone()
    my_connect.commit()
    
    nummer = Label(root, text = "Uw nummer: "+ num)
    nummer.grid(row = 504, column = 0)

    okbutton = Button(root, text='Ok', command=kbutton)
    okbutton.grid(row = 505, column = 0)
  
#okbutton
#def kbutton:():
    #okbotton.grid_forget()

klaarbutton = Button(root, text='klaar', command=klbutton)
klaarbutton.grid(row = 502, column = 0)


####### end of connection ####
my_conn.execute("SELECT * FROM first_test_gip")
i=1 
for student in my_conn: 
    for j in range(len(student)):
        e = Entry(root, width=10, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, student[j])
    i=i+1

root.mainloop()
