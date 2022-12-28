# *********************************************************************
# 
#                           Mali
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
from mali_gui import*




#   Classes

#   ********************************************************************
#                           Main
#   ********************************************************************

def main():#(args):
    mainWindow = MaliGUI()
    mainWindow = mainWindow.CreatGui()
    mainWindow.mainloop()
    return 0

if __name__ == '__main__':
    main()
