# *********************************************************************
# 
#                           Mali ini
#
#**********************************************************************
#
#  Autor:    schaerphix
#  Date:     28.12.2022
#  Revision: V2.0
#
#  LICENSE:  GNU General Public License v3.0


#   Import
import os
import getpass

#   Setup
mali_username = getpass.getuser()
mali_save_path = "/home/" + mali_username                                # Insert Path to store the Picture
mali_open_path = "/home/" + mali_username                                # Insert Path to open the Picture

#   General
mali_name = 'mali'
mali_folder = os.path.abspath(os.path.dirname(__file__))

#   Colors
mali_white = "#ffffff"
mali_red = "#AF1C1C"
mali_gray = "#EEEEEE"

mali_color_palet_1 = ["#1a1c2c","#5d275d","#b13e53","#ef7d57","#ffcd75",
        "#a7f070","#38b764","#257179","#29366f","#3b5dc9","#41a6f6","#73eff7",
        "#f4f4f4","#94b0c2","#566c86","#333c57","#ffffff"]

mali_color_palet = mali_color_palet_1

#   Icons
mali_icon = mali_folder + '/icons/' + 'mali.png'
mali_new_icon = mali_folder + '/icons/' + 'new_s.png'
mali_load_icon = mali_folder + '/icons/' + 'load_s.png'
mali_save_icon = mali_folder + '/icons/' + 'save_s.png'
mali_dot_icon = mali_folder + '/icons/' + 'dot.png'
mali_dot_line_icon = mali_folder + '/icons/' + 'dotedLine.png'
mali_line_icon = mali_folder + '/icons/' + 'line.png'
mali_line45_icon = mali_folder + '/icons/' + 'line45.png'
