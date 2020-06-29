import subprocess
from tkinter import *
USER="user"
PASSWORD="pass"
def new(nome_drive,sito,username,password):
    subprocess.run(["rclone","config","create",nome_drive,sito,USER,username,PASSWORD,password],shell=True)

def copia(drive1,drive2,path1,path2):
    source=f'{drive1}:{path1}'
    to=f'{drive2}:{path2}'
    subprocess.run(["rclone","copy",source,to])

def sposta(drive1,drive2,path1,path2):
    source=f'{drive1}:{path1}'
    to=f'{drive2}:{path2}'
    subprocess.run(["rclone","move",source,to])

def nuovo_drive_window():
    window=Toplevel()
    window.title("nuovo drive")

    #riga unox


    nome_drive_Label = Label(window, text = "nome drive")
    nome_drive_Label.grid(column = 1, row = 1)

    sito_web_Label = Label(window, text = "sito web")
    sito_web_Label.grid(column = 2, row = 1)

    username_utente_Label= Label(window, text = "user")
    username_utente_Label.grid(column = 3, row = 1)

    pwd_Label = Label(window, text = "pwd")
    pwd_Label.grid(column = 4, row = 1)



    #riga 2

    nome_drive = Entry(window, width = 15)
    nome_drive.grid(column = 1, row= 2)


    sitiweb=["mega","drive","yandex"]
    sitosel=StringVar()
    sitosel.set(sitiweb[0])
    sito_web = OptionMenu(window,sitosel,*sitiweb)
    sito_web.grid(column = 2, row= 2)

    username_utente = Entry(window, width = 15)
    username_utente.grid(column = 3, row= 2)

    pwd = Entry(window, width = 15)
    pwd.grid(column = 4, row= 2)


    #riga 3
    nuovo = Button(window, text = "allacciare nuovo cloud?", command= lambda: new(nome_drive.get(),sitosel.get(),username_utente.get(),pwd.get()))
    nuovo.grid(column = 1, row = 3)
    window.mainloop()

def copia_su_drive_window():
    window=Toplevel()
    window.title("copia drive")

    #riga 1
    da_Label = Label(window, text = "from")
    da_Label.grid(column = 1, row = 1)

    path1_Label = Label(window, text = "path")
    path1_Label.grid(column = 2, row = 1)

    a_Label= Label(window, text = "to")
    a_Label.grid(column = 3, row = 1)

    path2_Label = Label(window, text = "path")
    path2_Label.grid(column = 4, row = 1)



    #riga 2
#////////////////
    #da=["mega","drive","yandex"...]
    #sitosel1=StringVar()
    #sitosel1.set(da[0])
    #sito_web = OptionMenu(window,sitosel1,*da)
    #sito_web.grid(column = 1, row= 2)

    sitosel1=Entry(window, width = 15)
    sitosel1.grid(column = 1, row= 2)
#////////////
    path1 = Entry(window, width = 15)
    path1.grid(column = 2, row= 2)
#//////////
    #a=["mega","drive","yandex"...]
    #sitosel2=StringVar()
    #sitosel2.set(a[0])
    #sito_web = OptionMenu(window,sitosel2,*a)
    #sito_web.grid(column = 3, row= 2)

    sitosel2=Entry(window, width = 15)
    sitosel2.grid(column = 3, row= 2)
#//////////////////    

    path2 = Entry(window, width = 15)
    path2.grid(column = 4, row= 2)


    #riga 3
    nuovo = Button(window, text = "copia!!!!", command= lambda: copia(sitosel1.get(),sitosel2.get(),path1.get(),path2.get()))
    nuovo.grid(column = 1, row = 3)
    window.mainloop()



root = Tk()
root.title("root")
root.minsize(400,100)
root_nuovo_drive= Button(root,text="nuovo drive",command=lambda:nuovo_drive_window())
root_nuovo_drive.grid(column=0,row=0)

root_copia=Button(root,text="copia", command=lambda:copia_su_drive_window())
root_copia.grid(column=1,row=0)

root_sposta=Button(root,text="sposta", command=lambda:sposta_su_drive_window())
root_sposta.grid(column=2,row=0)
root.mainloop()