from functools import partial
from pathlib import PureWindowsPath             # library that cleans up windows path extensions
from openpyxl import *                          # Write to excel
import tkinter as tk                            # Tkinter's Tk class
import tkinter.ttk as ttk                       # Tkinter's Tkk class
import datetime as dt                           # Date library
import subprocess                               # Needed to open an executable
import time                                     # Needed to call time to count/pause
import os                                       # Needed for closing an executable
from PIL import ImageTk, Image                  # Displaying LAL background photo
from tkinter import messagebox                  # Exit standard message box

################# START NEW POP UP WINDOW #############################
GUI = tk.Tk()
GUI.title("Sample Sizes")
GUI.geometry('750x600')
GUI.configure(background='white')  # Set background color
GUI.option_add('*Font', 'Helvetica 11 bold')  # set the font and size for entire GUI
GUI.option_add('*foreground', 'black')  # set the text color, hex works too '#FFFFFF'
GUI.option_add('*background', 'white')  # set the background to white

lbl_cmd_mc1 = tk.Label(GUI, text="Are the samples numbered in order?").place(x=150, y=20, anchor='center')
lbl_cmd_mc2 = tk.Label(GUI, text="If not, click 'No' and a new window").place(x=150, y=40, anchor='center')
lbl_cmd_mc3 = tk.Label(GUI, text="will popup to select the sample").place(x=150, y=60, anchor='center')
lbl_cmd_mc4 = tk.Label(GUI, text="numbers listed in the work order.").place(x=150, y=80, anchor='center')

lbl_cmd_s1 = tk.Label(GUI, text="Sample Set #1: ").place(x=20, y=125)
lbl_cmd_s2 = tk.Label(GUI, text="Sample Set #2: ").place(x=20, y=165)
lbl_cmd_s3 = tk.Label(GUI, text="Sample Set #3: ").place(x=20, y=205)
lbl_cmd_s4 = tk.Label(GUI, text="Sample Set #4: ").place(x=20, y=245)
lbl_cmd_s5 = tk.Label(GUI, text="Sample Set #5: ").place(x=20, y=285)
lbl_cmd_s6 = tk.Label(GUI, text="Sample Set #6: ").place(x=20, y=325)
lbl_cmd_s7 = tk.Label(GUI, text="Sample Set #7: ").place(x=20, y=365)
lbl_cmd_s8 = tk.Label(GUI, text="Sample Set #8: ").place(x=20, y=405)
lbl_cmd_s9 = tk.Label(GUI, text="Sample Set #9: ").place(x=20, y=445)
lbl_cmd_s10 = tk.Label(GUI, text="Sample Set #10: ").place(x=20, y=485)

entry_s1 = tk.Entry(GUI, width=10)
entry_s1.focus_set()  # Places cursor in the first entry box.
entry_s1.place(x=150, y=125)

entry_s2 = tk.Entry(GUI, width=10)
entry_s2.place(x=150, y=165)

entry_s3 = tk.Entry(GUI, width=10)
entry_s3.place(x=150, y=205)

entry_s4 = tk.Entry(GUI, width=10)
entry_s4.place(x=150, y=245)

entry_s5 = tk.Entry(GUI, width=10)
entry_s5.place(x=150, y=285)

entry_s6 = tk.Entry(GUI, width=10)
entry_s6.place(x=150, y=325)

entry_s7 = tk.Entry(GUI, width=10)
entry_s7.place(x=150, y=365)

entry_s8 = tk.Entry(GUI, width=10)
entry_s8.place(x=150, y=405)

entry_s9 = tk.Entry(GUI, width=10)
entry_s9.place(x=150, y=445)

entry_s10 = tk.Entry(GUI, width=10)
entry_s10.place(x=150, y=485)

lbl_dis_s1 = tk.Label(GUI, text="Sample Set #1: ").place(x=350, y=125)
lbl_dis_s2 = tk.Label(GUI, text="Sample Set #2: ").place(x=350, y=165)
lbl_dis_s3 = tk.Label(GUI, text="Sample Set #3: ").place(x=350, y=205)
lbl_dis_s4 = tk.Label(GUI, text="Sample Set #4: ").place(x=350, y=245)
lbl_dis_s5 = tk.Label(GUI, text="Sample Set #5: ").place(x=350, y=285)
lbl_dis_s6 = tk.Label(GUI, text="Sample Set #6: ").place(x=350, y=325)
lbl_dis_s7 = tk.Label(GUI, text="Sample Set #7: ").place(x=350, y=365)
lbl_dis_s8 = tk.Label(GUI, text="Sample Set #8: ").place(x=350, y=405)
lbl_dis_s9 = tk.Label(GUI, text="Sample Set #9: ").place(x=350, y=445)
lbl_dis_s10 = tk.Label(GUI, text="Sample Set #10: ").place(x=350, y=485)

lbl_out_s1 = tk.Label(GUI, text="minesweep Output").place(x=475, y=135,anchor='w')
lbl_out_s2 = tk.Label(GUI, text="Test").place(x=475, y=175,anchor='w')
lbl_out_s3 = tk.Label(GUI, text="Test").place(x=475, y=215,anchor='w')
lbl_out_s4 = tk.Label(GUI, text="Test").place(x=475, y=255,anchor='w')
lbl_out_s5 = tk.Label(GUI, text="Test").place(x=475, y=295,anchor='w')
lbl_out_s6 = tk.Label(GUI, text="Test").place(x=475, y=335,anchor='w')
lbl_out_s7 = tk.Label(GUI, text="Test").place(x=475, y=375,anchor='w')
lbl_out_s8 = tk.Label(GUI, text="Test").place(x=475, y=415,anchor='w')
lbl_out_s9 = tk.Label(GUI, text="Test").place(x=475, y=455,anchor='w')
lbl_out_s10 = tk.Label(GUI, text="Align West").place(x=475, y=495,anchor='w')

set = int(0)
sum_tot = int(0)

def get_all():
    s1 = entry_s1.get()
    s2 = entry_s2.get()
    s3 = entry_s3.get()
    s4 = entry_s4.get()
    s5 = entry_s5.get()
    s6 = entry_s6.get()
    s7 = entry_s7.get()
    s8 = entry_s8.get()
    s9 = entry_s9.get()
    s10 = entry_s10.get()

#########      Sample Entry #1       #########
    if s1.isdigit():
        set = int(1)
        try:
            s1_int = int(s1)
            sum_tot = s1_int
            #############         Sample Entry #2         ###########
            if s2.isdigit():
                set = int(2)
                try:
                    s2_int = int(s2)
                    sum_tot = sum_tot + s2_int
                    #############       Sample Entry #3        ###############
                    if s3.isdigit():
                        set = int(3)
                        try:
                            s3_int = int(s3)
                            sum_tot = sum_tot + s3_int
                            #############       Sample Entry #4        ###############
                            if s4.isdigit():
                                set = int(4)
                                try:
                                    s4_int = int(s4)
                                    sum_tot = sum_tot + s4_int
                                    #############       Sample Entry #5        ###############
                                    if s5.isdigit():
                                        set = int(5)
                                        try:
                                            s5_int = int(s5)
                                            sum_tot = sum_tot + s5_int
                                            #############         Sample Entry #6         ###########
                                            if s6.isdigit():
                                                set = int(6)
                                                try:
                                                    s6_int = int(s6)
                                                    sum_tot = sum_tot + s6_int
                                                    #############       Sample Entry #7        ###############
                                                    if s7.isdigit():
                                                        set = int(7)
                                                        try:
                                                            s7_int = int(s7)
                                                            sum_tot = sum_tot + s7_int
                                                            #############       Sample Entry #8        ###############
                                                            if s8.isdigit():
                                                                set = int(8)
                                                                try:
                                                                    s8_int = int(s8)
                                                                    sum_tot = sum_tot + s8_int
                                                                    #############       Sample Entry #9        ###############
                                                                    if s9.isdigit():
                                                                        set = int(9)
                                                                        try:
                                                                            s9_int = int(s9)
                                                                            sum_tot = sum_tot + s9_int
                                                                            #############       Sample Entry #10        ###############
                                                                            if s10.isdigit():
                                                                                set = int(10)
                                                                                try:
                                                                                    s10_int = int(s9)
                                                                                    sum_tot = sum_tot + s10_int
                                                                                except ValueError:  # Close Try 10
                                                                                    set = int(9)
                                                                            else:  # Close Loop 10
                                                                                pass
                                                                        except ValueError:  # Close Try 9
                                                                            set = int(8)
                                                                    else:  # Close Loop 9
                                                                        pass
                                                                except ValueError:  # Close Try 8
                                                                    set = int(7)
                                                            else:  # Close Loop 8
                                                                pass
                                                        except ValueError:  # Close Try 7
                                                            set = int(6)
                                                    else:  # Close Loop 7
                                                        pass
                                                except ValueError:  # Close Try 6
                                                    set = int(5)
                                            else:  # Close Loop 6
                                                pass
                                        except ValueError:  # Close Try 5
                                            set = int(4)
                                    else:  # Close Loop 5
                                        pass
                                except ValueError:  # Close Try 4
                                    set = int(3)
                            else:  # Close Loop 4
                                pass
                        except ValueError:  # Close Try 3
                            set = int(2)
                    else:   # Close Loop 3
                        pass
                except ValueError:  # Close Try 2
                    set = int(1)
            else:   # Close Loop 2
                pass
        except ValueError:  # Close Try 1
            set = int(0)
    else:   # Close Loop 1
        pass
    print("s1, s2, s3: ", s1, " ", s2, " ", s3, s4, s5, s6, s7, s8, s9, s10)
    print("There is/are ", set, " set(s) of samples to run")
    print("There are ", sum_tot, " samples total to test")

def minesweep():
############ OPEN NEW minesweep GUI   ###################
    print("minesweep will be here soon")

btn_no1 = tk.Button(GUI, text='No', width=5, command=minesweep)
btn_no1.place(x=250, y=120)
btn_no2 = tk.Button(GUI, text='No', width=5, command=minesweep)
btn_no2.place(x=250, y=160)
btn_no3 = tk.Button(GUI, text='No', width=5, command=minesweep)
btn_no3.place(x=250, y=200)
btn_no4 = tk.Button(GUI, text='No', width=5, command=minesweep)
btn_no4.place(x=250, y=240)
btn_no5 = tk.Button(GUI, text='No', width=5, command=minesweep)
btn_no5.place(x=250, y=280)
btn_no6 = tk.Button(GUI, text='No', width=5, command=minesweep)
btn_no6.place(x=250, y=320)
btn_no7 = tk.Button(GUI, text='No', width=5, command=minesweep)
btn_no7.place(x=250, y=360)
btn_no8 = tk.Button(GUI, text='No', width=5, command=minesweep)
btn_no8.place(x=250, y=400)
btn_no9 = tk.Button(GUI, text='No', width=5, command=minesweep)
btn_no9.place(x=250, y=440)
btn_no10 = tk.Button(GUI, text='No', width=5, command=minesweep)
btn_no10.place(x=250, y=480)

btn_ok = tk.Button(GUI, text='Save All', width=7, command=get_all)
btn_ok.place(x=525, y=550)

btn_cls = tk.Button(GUI, text='Close', width=7, command=GUI.destroy)
btn_cls.place(x=625, y=550)

GUI.mainloop()
################# END POP UP WINDOW #############################