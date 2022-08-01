#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kahkashan
#
# Created:     25/05/2022
# Copyright:   (c) Kahkashan 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import*
dsc=Tk()
dsc.geometry("720x480")
dsc.title("Paint Application")
dsc.configure(bg="violet")
lal=Label(dsc,text="Draw").pack()
giet=Canvas(dsc,width=720,height=480,bg="white")
giet.pack()

def redc():
    global color
    color="red"
    giet.bind('<B1-Motion>',paint_page)
def yellowc():
    global color
    color="yellow"
    giet.bind('<B1-Motion>',paint_page)
def bluec():
    global color
    color="blue"
    giet.bind('<B1-Motion>',paint_page)
def greenc():
    global color
    color="green"
    giet.bind('<B1-Motion>',paint_page)
def blackc():
    global color
    color="black"
    giet.bind('<B1-Motion>',paint_page)
def deletec():
    giet.delete('all')
#def paintingc():
#    global color
#    color="orange"
#    giet.bind('<B1-Motion>',paint_area)

btn=Button(dsc,text="black colour",bg="white",fg="black",command=blackc)
btn.place(x=20,y=30)
btn=Button(dsc,text="red colour",bg="red",fg="white",command=redc)
btn.place(x=20,y=60)
btn=Button(dsc,text="yellow colour",bg="yellow",fg="white",command=yellowc)
btn.place(x=20,y=90)
btn=Button(dsc,text="blue colour",bg="blue",fg="white",command=bluec)
btn.place(x=20,y=120)
btn=Button(dsc,text="green colour",bg="green",fg="white",command=greenc)
btn.place(x=20,y=150)
#btn=Button(dsc,text="paint orange",bg="orange",fg="white",command=paintingc)
#btn.place(x=20,y=180)
btn=Button(dsc,text="Delete",bg="black",fg="white",command=deletec)
btn.place(x=20,y=210)


#lal=Label(dsc, text="Enter First Number", font=('Calibri 10'))
#lal.place(x=120,y=60)
#a=Entry(dsc, width=35)
#a.place(x=120,y=90)
#size=int(a.get())


def paint_page(event):
    x1,y1=(event.x+1),(event.y-1)
    x2,y2=(event.x+1),(event.y-1)
    giet.create_oval(x1,y1,x2,y2,fill=color,outline=color)

#def paint_area(event):
#    x1,y1=(event.x+10),(event.y)
 #   x2,y2=(event.x),(event.y+10)
  #  giet.create_oval(x1,y1,x2,y2,fill=color,outline=color)

dsc.mainloop()
