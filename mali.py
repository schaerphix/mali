# *********************************************************************
# 
#                           Mali
#
#**********************************************************************
#
#  Autor:    schaerphix
#  Date:     02.12.2022
#  Revision: V1.3
#
#  LICENSE:  GNU General Public License v3.0



#   ********************************************************************
#                           Import
#   ********************************************************************

from tkinter import*
from tkinter import Button
import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
import io
import datetime


#   ********************************************************************
#                           Classes
#   ********************************************************************

class MainWin ():
    
    def __init__(self):     
        self.win=Tk()
                                                    
        self.white = "#ffffff"
        self.gray = "#EEEEEE"
        self.red = '#b13e53'
        
        self.mainTitle = "Mali"
        self.picturePath = ""                               # Insert Path to store the Picture
        self.w = self.win.winfo_screenwidth()
        self.h = self.win.winfo_screenheight() - 20 
        self.wDiff = 80
        self.hDiff = 150
        self.winSizeMain = str(self.w) + "x" + str(self.h)
        self.bg = self.gray
        self.winBg = None
        self.widthBu = 3
        
        self.COLORS = ["#1a1c2c","#5d275d","#b13e53","#ef7d57","#ffcd75",
        "#a7f070","#38b764","#257179","#29366f","#3b5dc9","#41a6f6","#73eff7",
        "#f4f4f4","#94b0c2","#566c86","#333c57"]
        
        self.butWith = 20
        self.deltaX = (self.w - (self.butWith * len(self.COLORS))) / (len(self.COLORS) + 1) 
        self.actXpos =  self.deltaX / 2
        
        self.penColor = "#ffffff"
        self.caMain = None
        
    
    def CreatGui(self):
        self.win.geometry(self.winSizeMain)
        self.win.title(self.mainTitle)
        self.winBg = self.win.tk_setPalette(self.bg)
        #self.win.overrideredirect(True)
        self.win.iconphoto(False, PhotoImage(file='mali.png'))
        
        self.CreatCanvas(self.win,self.w-self.wDiff,self.h-self.hDiff,self.white,10,65)
        self.CreatColorButton()
        self.CreatNewButton(self.win,self.white,10, 10)
        self.CreatSaveButton(self.win,self.white,160, 10)
        self.CreatLoadButton(self.win,self.white,310, 10)
        self.CreatCloseButton(self.win,self.red,self.w-60, 10)
        return self.win
        
    def CreatCanvas (self,rot,w,h,col,px,py):
        self.ca = Canvas(rot, width= w, height= h, bg=col)
        self.ca.bind('<B1-Motion>',self.Paint)
        self.ca.place(x=px, y=py)

    def CreatColorButton(self):
        for c in self.COLORS:
            self.CreatPaletteButton(self.win,c,self.actXpos,self.h-75)
            self.actXpos = self.actXpos + self.deltaX + self.butWith

    def Paint(self,event):
        # get x1, y1, x2, y2 co-ordinates
        x1, y1 = (event.x-3), (event.y-3)
        x2, y2 = (event.x+3), (event.y+3)
        color = self.penColor
        # display the mouse movement inside canvas
        self.ca.create_oval(x1, y1, x2, y2, fill=color, outline=color)

    def CreatPaletteButton(self,rot,col,px,py):
        but = Button(rot, bg=col, width=self.widthBu, height=2, relief = "flat")
        but ["command"] = lambda: self.SetPenColor(col)
        but.place(x=px,y=py)
        return but
   
    def SetPenColor(self,colo):
        self.penColor = colo
        
    def CreatNewButton(self,rot,col,px,py):
        but = Button(rot, bg=col, text =" ", width=self.widthBu, height=2,relief = "flat")                  
        but ["command"] = self.new
        but.place(x=px,y=py)
        
    def new(self):
        self.save()
        self.ca.destroy()
        self.CreatCanvas(self.win,self.w-self.wDiff,self.h-self.hDiff,self.white,10,65)
        
    def CreatLoadButton(self,rot,col,px,py):
        but = Button(rot, bg=col, text ="[->", width=self.widthBu, height=2,relief = "flat")                  
        but ["command"] = self.load
        but.place(x=px,y=py)
        
    def load(self):
        self.new()
        selectPic = fd.askopenfilename(title="")
        img = Image.open(selectPic)
        pic1 = ImageTk.PhotoImage(img)
        self.ca.image = pic1  # <--- keep reference of your image
        self.ca.create_image(self.w / 2, self.h /2 , image=pic1)                # (0,0,anchor='nw',image=pic1) self.w-self.wDiff,self.h-self.hDiff
        #self.ca.place(x=10, y=65)
        
    def CreatSaveButton(self,rot,col,px,py):
        but = Button(rot, bg=col, text ="->]",  width=self.widthBu, height=2,relief = "flat")                  
        but ["command"] = self.save
        but.place(x=px,y=py)
        
    def save(self):
        ps = self.ca.postscript(colormode='color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        img.save(self.picturePath + 'Mali_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg')
    
        
    def CreatCloseButton(self,rot,col,px,py):
        but = Button(rot, bg=col, text ="X", width=self.widthBu, height=2,relief = "flat")                  
        but ["command"] = self.close
        but.place(x=px,y=py)
        
    def close(self):
        self.save()
        self.win.destroy()

#   ********************************************************************
#                           Main
#   ********************************************************************

def main():#(args):
    mainWindow = MainWin()
    mainWindow = mainWindow.CreatGui()
    mainWindow.mainloop()
    return 0

if __name__ == '__main__':
    #import sys
    #sys.exit(main(sys.argv))
    main()
