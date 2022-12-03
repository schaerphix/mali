# *********************************************************************
# 
#                           Mali
#
#**********************************************************************
#
#  Autor:    Philippe Schär
#  Date:     02.12.2022
#  Revision: V1.3
#
#  LICENSE:  GNU General Public License v3.0



#   ********************************************************************
#                           Import
#   ********************************************************************

from tkinter import*
from tkinter import Button
from PIL import Image
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
        self.picturePath = ""
        self.w = self.win.winfo_screenwidth()
        self.h = self.win.winfo_screenheight()
        self.winSizeMain = str(self.w) + "x" + str(self.h)
        self.bg = self.gray
        self.winBg = None
        self.widthBu = 3
        
        self.butBrei = 20
        self.deltaX = 43 
        self.actXpos = ((self.w-(20*self.butBrei)-(19*self.deltaX))/2)+10 #75
        
        self.penColor = "#ffffff"
        self.caMain = None
        
        self.COLORS = ["#1a1c2c","#5d275d","#b13e53","#ef7d57","#ffcd75",
        "#a7f070","#38b764","#257179","#29366f","#3b5dc9","#41a6f6","#73eff7",
        "#f4f4f4","#94b0c2","#566c86","#333c57"]


    def CreatGui(self):
        self.win.geometry(self.winSizeMain)
        self.win.title(self.mainTitle)
        self.winBg = self.win.tk_setPalette(self.bg)
        self.win.overrideredirect(True)
        self.win.iconphoto(False, PhotoImage(file='/usr/local/src/mali/mali.png'))
        
        self.CreatCanvas(self.win,self.w-120,self.h-100,self.white,5,5)
        self.CreatColorButton()
        self.CreatSaveButton(self.win,self.white,self.w-80, 100)
        self.CreatCloseButton(self.win,self.red,self.w-80, 10)
        return self.win
        
    def CreatCanvas (self,rot,w,h,col,px,py):
        self.ca = Canvas(rot, width= w, height= h, bg=col)
        self.ca.bind('<B1-Motion>',self.Paint)
        self.ca.place(x=px, y=py)

    def CreatColorButton(self):
        for c in self.COLORS:
            self.CreatPaletteButton(self.win,c,self.actXpos,self.h-75)
            self.actXpos = self.actXpos + self.deltaX + self.butBrei

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

def main(args):
    mainWindow = MainWin()
    mainWindow = mainWindow.CreatGui()
    mainWindow.mainloop()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
