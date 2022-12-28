# *********************************************************************
# 
#                           Mali GUI
#
#**********************************************************************
#
#  Autor:    schaerphix
#  Date:     28.12.2022
#  Revision: V2.0
#
#  LICENSE:  GNU General Public License v3.0


#   Import
from mali_ini import*

from tkinter import*
from tkinter import Button
import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk

import io
import datetime


#   Classes
class MaliGUI():
    def __init__(self):     
        self.win=Tk()
        
        self.mainTitle = mali_name
        self.userName = mali_username
        self.picturePath = mali_save_path                               
        self.w = self.win.winfo_screenwidth()
        self.h = self.win.winfo_screenheight() - 50 
        self.wDiff = 80
        self.hDiff = 150
        self.winSizeMain = str(self.w) + "x" + str(self.h)
        self.bg = mali_gray
        self.winBg = None
        self.widthBu = 3
        self.style = None
        
        self.COLORS = mali_color_palet
        
        self.butWith = 20
        self.deltaX = (self.w - (self.butWith * len(self.COLORS))) / (len(self.COLORS) + 1) 
        self.actXpos =  self.deltaX / 2
        
        self.scale_var = DoubleVar()
        
        self.penColor = mali_color_palet[0]
        self.caMain = None
        self.penwidthIni = 6
            
    def CreatGui(self):
        self.win.geometry(self.winSizeMain)
        self.win.title(self.mainTitle)
        self.winBg = self.win.tk_setPalette(self.bg)
        self.win.iconphoto(False, PhotoImage(file=mali_icon))
        
        self.CreatCanvas(self.win,self.w-self.wDiff,self.h-self.hDiff,mali_white,10,65)
        self.CreatCloseButton(self.win,mali_red,self.w-60, 10)
        self.CreateStyleButtons()
        self.CreatColorButton()
        self.clororShow = self.CreateColorShow(self.win,self.w/8,self.h/25,self.penColor,((self.w/2)-(self.w/8)/2),10)
        
        self.slider_width = Scale(self.win, variable = self.scale_var, from_=100, to=0, orient= 'vertical',showvalue=None)
        self.slider_width.place(x=self.w-70,y=self.h-self.hDiff-40)
        self.slider_width.set(self.penwidthIni)
        
        return self.win

    def CreatCloseButton(self,rot,col,px,py):
        but = Button(rot, bg=col, text ="X", width=self.widthBu, height=2,relief = "flat")                  
        but ["command"] = self.close
        but.place(x=px,y=py)
    
    def CreatCanvas(self,rot,w,h,col,px,py):
        self.ca = Canvas(rot, width= w, height= h, bg=col)
        self.ca.bind('<ButtonPress-1>',self.Paint)                           
        self.ca.bind('<ButtonRelease-1>',self.Paint)                          
        self.ca.bind('<B1-Motion>',self.Paint)  
        self.ca.place(x=px, y=py)

    def CreateColorShow(self,rot,w,h,col,px,py):
        can = Canvas(rot, width= w, height= h, bg=col)
        can.place(x=px, y=py)
        return can

    def CreatColorButton(self):
        for c in self.COLORS:
            self.CreatPaletteButton(self.win,c,self.actXpos,self.h-75)
            self.actXpos = self.actXpos + self.deltaX + self.butWith
        
    def CreateStyleButtons(self):
        #   New Button
        picN = PhotoImage(file=mali_new_icon)
        self.NewButton = Canvas(self.win, width= 40, height= 40)
        self.NewButton.bind('<ButtonPress-1>',self.new) 
        self.NewButton.bind('<ButtonRelease-1>',self.new) 
        self.NewButton.image = picN
        self.NewButton.create_image(20, 20, image=picN)
        self.NewButton.place(x=10,y=10)
        
        #   Save Button
        picS = PhotoImage(file=mali_save_icon)
        self.SaveButton = Canvas(self.win, width= 40, height= 40)
        self.SaveButton.bind('<ButtonPress-1>',self.save) 
        self.SaveButton.bind('<ButtonRelease-1>',self.save) 
        self.SaveButton.image = picS
        self.SaveButton.create_image(20, 20, image=picS)
        self.SaveButton.place(x=160,y=10)
        
        #   Load Button
        picL = PhotoImage(file=mali_load_icon)
        self.LoadButton = Canvas(self.win, width= 40, height= 40)
        self.LoadButton.bind('<ButtonPress-1>',self.load) 
        self.LoadButton.bind('<ButtonRelease-1>',self.load) 
        self.LoadButton.image = picL
        self.LoadButton.create_image(20, 20, image=picL)
        self.LoadButton.place(x=310,y=10)
        
        #   Dot Button
        picD = PhotoImage(file=mali_dot_icon)
        self.DotButton = Canvas(self.win, background=mali_white, width= 40, height= 40)
        self.DotButton.bind('<ButtonRelease-1>',self.CreateDotButton) 
        self.DotButton.image = picD
        self.DotButton.create_image(20, 20, image=picD)
        self.DotButton.place(x=self.w-60,y=(self.h/10)*3)
        
        #   DotLine Button
        picDL = PhotoImage(file=mali_dot_line_icon)
        self.DotLineButton = Canvas(self.win, width= 40, height= 40)
        self.DotLineButton.bind('<ButtonRelease-1>',self.CreateDotLineButton) 
        self.DotLineButton.image = picDL
        self.DotLineButton.create_image(20, 20, image=picDL)
        self.DotLineButton.place(x=self.w-60,y=(self.h/10)*4)
        
        #   Line Button
        picLi = PhotoImage(file=mali_line_icon)
        self.LineButton = Canvas(self.win, width= 40, height= 40)
        self.LineButton.bind('<ButtonRelease-1>',self.CreateLineButton) 
        self.LineButton.image = picLi
        self.LineButton.create_image(20, 20, image=picLi)
        self.LineButton.place(x=self.w-60,y=(self.h/10)*5)
        
        #   Line45 Button
        picLi45 = PhotoImage(file=mali_line45_icon)
        self.Line45Button = Canvas(self.win, width= 40, height= 40)
        self.Line45Button.bind('<ButtonRelease-1>',self.CreateSpezLineButton) 
        self.Line45Button.image = picLi45
        self.Line45Button.create_image(20, 20, image=picLi45)
        self.Line45Button.place(x=self.w-60,y=(self.h/10)*6)


    def CreateDotButton(self,event):
        if str(event.type) == '5':
            self.SetStyle('Dot')
            self.ResetButtonBG()
            self.DotButton['background'] = mali_white
                
    def CreateDotLineButton(self,event):
        if str(event.type) == '5':
            self.SetStyle('DotLine')
            self.ResetButtonBG()
            self.DotLineButton['background'] = mali_white

    def CreateLineButton(self,event):
        if str(event.type) == '5':
            self.SetStyle('Line')
            self.ResetButtonBG()
            self.LineButton['background'] = mali_white
        
    def CreateSpezLineButton(self,event):
        if str(event.type) == '5':
            self.SetStyle('SpezLine')
            self.ResetButtonBG()
            self.Line45Button['background'] = mali_white
     
    def ResetButtonBG(self):
        self.DotButton['background'] = mali_gray
        self.DotLineButton['background'] = mali_gray
        self.LineButton['background'] = mali_gray
        self.Line45Button['background'] = mali_gray
    
    def SetStyle(self,style):
        self.style = style
        
    def Paint(self,event):
        if self.style == 'Dot':
            self.PaintDot(event)
        elif self.style == 'DotLine':
            self.PaintDotLine(event)
        elif self.style == 'Line':
            self.PaintLine(event)
        elif self.style == 'SpezLine':
            self.PaintLineSpecial(event)
        else:
            self.PaintDot(event)        
        
    def PaintLine(self,event):
        if str(event.type) == '4':                  # event 4: Press Mouse button1
            self.ca.old_coords = event.x, event.y
        elif str(event.type) == '5':                # event 5: Releases Mouse button1
            x, y = event.x, event.y
            x1, y1 = self.ca.old_coords
            self.ca.create_line(x, y, x1, y1,width=self.slider_width.get(), fill=self.penColor)
        
    def PaintLineSpecial(self,event):
        if str(event.type) == '6':                  # event 6: Move pressed Mouse button1
            # get x1, y1, x2, y2 co-ordinates
            r = self.slider_width.get()/2
            x1, y1 = (event.x-r), (event.y-r)
            x2, y2 = (event.x+r), (event.y+r)
            color = self.penColor
            # display the mouse movement inside canvas
            self.ca.create_line(x1, y1, x2, y2, fill=color)#, outline=color)
        
    def PaintDot(self,event):   # Action: Button-1
        if str(event.type) == '4':                  # event 4: Press Mouse button1
            # get x1, y1, x2, y2 co-ordinates
            r = self.slider_width.get()/2
            x1, y1 = (event.x-r), (event.y-r)
            x2, y2 = (event.x+r), (event.y+r)
            color = self.penColor
            # display the mouse movement inside canvas
            self.ca.create_oval(x1, y1, x2, y2, fill=color, outline=color)
        
    def PaintDotLine(self, event):  # Action: B1-Motion
        if str(event.type) == '6':                  # event 6: Move pressed Mouse button1
            # get x1, y1, x2, y2 co-ordinates
            r = self.slider_width.get()/2
            x1, y1 = (event.x-r), (event.y-r)
            x2, y2 = (event.x+r), (event.y+r)
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
        self.clororShow['bg'] = self.penColor
        
    def new(self,event=None):
        if event == None:
            self.save()
            self.ca.destroy()
            self.CreatCanvas(self.win,self.w-self.wDiff,self.h-self.hDiff,mali_white,10,65)
        else:
            if str(event.type) == '4':                  # event 4: Press Mouse button1
                self.NewButton['background'] = mali_white
            elif str(event.type) == '5':
                self.save()
                self.ca.destroy()
                self.CreatCanvas(self.win,self.w-self.wDiff,self.h-self.hDiff,mali_white,10,65)
                self.NewButton['background'] = mali_gray
        
    def load(self,event=None):
        if str(event.type) == '4':                  # event 4: Press Mouse button1
            self.LoadButton['background'] = mali_white
        elif str(event.type) == '5':
            self.new()
            selectPic = fd.askopenfilename(title="", initialdir=mali_open_path)
            img = Image.open(selectPic)
            pic1 = ImageTk.PhotoImage(img)
            self.ca.image = pic1  
            self.ca.create_image(self.w / 2, self.h /2 , image=pic1)  
            self.LoadButton['background'] = mali_gray             
       
    def save(self,event=None):
        if event == None:
            ps = self.ca.postscript(colormode='color')
            img = Image.open(io.BytesIO(ps.encode('utf-8')))
            img.save(self.picturePath + self.userName + '_Mali_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg')
        else: 
            if str(event.type) == '5':
                ps = self.ca.postscript(colormode='color')
                img = Image.open(io.BytesIO(ps.encode('utf-8')))
                img.save(self.picturePath + self.userName + '_Mali_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg')
                self.SaveButton['background'] = mali_gray
            elif str(event.type) == '4':                  # event 4: Press Mouse button1
                self.SaveButton['background'] = mali_white
    
    def close(self):
        self.save()
        self.win.destroy()
