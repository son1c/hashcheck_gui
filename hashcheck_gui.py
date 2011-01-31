#!/usr/bin/env python3
# encoding: utf-8


import sys, tkinter, shutil, sys
from tkinter.filedialog import *



def ende () :
    sys.exit(0)
def datei() :
    e1.delete(0,"end")
    filename = askopenfilename()
    filename = "\"" +filename + "\""
    e1.insert(0,filename)
	
def md5_hash () :
    
    ew1 = e1.get()
    ew2 = e2.get()
    
    cs = case.get()
    if cs == "off" :
	    datei = os.popen("openssl md5 " + ew1).read()		
    if cs == "on" :											
        datei = os.popen("openssl md5 -c " + ew1).read()
	
    datei_split = datei.split("=")						
    hashwert = datei_split[1]							
    laenge = len(hashwert)									
    md5 = (hashwert [:laenge-1])							
    md5z = len(md5)										 
    md5f = (md5 [1:md5z])								 
   
    wert1 = md5f.lower()								
    wert2 = ew2.lower()									

    if wert1 == wert2 :
    	auslab["text"] = "ok"
    else :
        auslab["text"] = "false"
    
    
    
def sha1_hash ():
    ew1 = e1.get()
    ew2 = e2.get()
    
    cs = case.get()
    if cs == "off" :
       datei = os.popen("openssl sha1 " + ew1).read()		
    if cs == "on" :											
       datei = os.popen("openssl sha1 -c " + ew1).read()
	
    datei_split = datei.split("=")						
    hashwert = datei_split[1]							
    laenge = len(hashwert)									
    md5 = (hashwert [:laenge-1])							 
    md5z = len(md5)										 
    md5f = (md5 [1:md5z])								
   
    wert1 = md5f.lower()								
    wert2 = ew2.lower()									

    if wert1 == wert2 :
    	auslab["text"] = "ok"
    else :
        auslab["text"] = "false"

    

def compare() :
                           			
    ha = hash_alg.get()

    if ha == "md5" :
        md5_hash()
    
    if ha == "sha1" :
        sha1_hash()
    


main = tkinter.Tk()
main.geometry("460x135")


case = tkinter.StringVar()
case.set("off")

hash_alg = tkinter.StringVar()
hash_alg.set("md5")


filebutton = tkinter.Button(main, text = "File :", command = datei)
filebutton.grid(row=0, column=0, sticky="w")


e1 = tkinter.Entry(main, width=40)
e1.grid(row=0, column=1)


lab2 = tkinter.Label(main, text ="Hash-Value: ")
lab2.grid(row=1, column=0, sticky="w")


e2 = tkinter.Entry(main, width=40)
e2.grid(row=1, column=1)


rb1 = tkinter.Radiobutton(main, text="md5", variable=hash_alg, value="md5")
rb1.grid(row=2, column=0, sticky="w")
rb2 = tkinter.Radiobutton(main, text="sha1", variable=hash_alg, value="sha1")
rb2.grid(row=2, column=1, sticky="w")



cb1 = tkinter.Checkbutton(main, text="Separating Colons", variable=case, onvalue="on", offvalue="off")  
cb1.grid(row=3,column=0, sticky="w")


auslab = tkinter.Label(main, text ="")
auslab.grid(row=3, column=1)

bok = tkinter.Button(main, text="OK", command=compare)   
bok.grid(row=4, column=0, sticky="w")

bexit = tkinter.Button(main, text="Ende", command=ende)     
bexit.grid(row=4, column=1, sticky="e")

main.mainloop()




