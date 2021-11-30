from PIL import *
from tkinter import *
from datetime import *
import mysql.connector
import os

root= Tk()
#maak fullscreen
root.attributes('-fullscreen', True)

IDin = 0

#loginbutton
def lgnbutton():
    global naam, score, IDin
    #onthoud login
    IDin = login.get()
    #haal alleen naam/score van login
    my_conn.execute(("SELECT naam FROM first_test_gip WHERE ID = %s"),(IDin,))
    naam = my_conn.fetchone()
    my_connect.commit()
    my_conn.execute(("SELECT score FROM first_test_gip WHERE ID = %s"),(IDin,))
    score = my_conn.fetchone()
    my_connect.commit()
    #zorg ervoor dat nummer en naam correct geprint wordt
    naam = str(naam).replace(',','').replace('(','').replace(')','').replace("'",'')
    score = str(score).replace(',','').replace('(','').replace(')','').replace("'",'')

    #date + uur
    vandaag = str(date.today().day) + "-" + str(date.today().month) + "-" + str(date.today().year) + "-"

    #configure label zodat de zin tevoorschijn komt
    hallo.configure(text = f"hallo {naam} , \n Je hebt {score}/100 gescoord \n \n -{vandaag}")
    hallo.place(relx=0.5, rely=0.5, anchor=CENTER)

    okbutton.place(relx=0.6, rely=0.5, anchor=CENTER)

    #vergeet benoodigtheden voor login
    log.place_forget()
    login.place_forget()
    loginbutton.place_forget()
    
#okbutton
def kbutton():
    hallo.place_forget()
    okbutton.place_forget()

    log.place(relx=0.39, rely=0.5, anchor=CENTER)
    login.place(relx=0.5, rely=0.5, anchor=CENTER)
    loginbutton.place(relx=0.6, rely=0.5, anchor=CENTER)

#login
log = Label(root, text = "Geef hier je nummer in:",font = "Times")
log.place(relx=0.39, rely=0.5, anchor=CENTER)
login = Entry (root, bd = 5)
login.place(relx=0.5, rely=0.5, anchor=CENTER)
loginbutton = Button(root, text='login',font = "Times",bg = "#7FDBFF", command=lgnbutton)
loginbutton.place(relx=0.6, rely=0.5, anchor=CENTER)

#maak label en ok button en plaats ze later
hallo = Label(root,font = "Times")
okbutton = Button(root, text='OK', command=kbutton)

#connecteer met database
my_connect = mysql.connector.connect(
  host="localhost",
  user="root", 
  passwd="",
  database="test_2"
)
my_conn = my_connect.cursor()


root.mainloop()
