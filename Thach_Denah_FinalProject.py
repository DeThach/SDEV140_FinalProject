# Program Name: Thach_Denah_FinalProject
# Author: Denah Thach
# Date: 12/13/2021  
# Summary: GUI to calculate the gas consumption of a vehicle and display the dollar amount
# Variables:
#   root.main_window - the root main window of tkinter
#   root.top_frame - the top frame
#   root.mid_frame - the first mid frame for Year/Make/Model
#   root.mid2_frame - the second mid frame for MPG
#   root.mid3_frame - the third mid frame for Mileage Point
#   root.mid4_frame - the fourth mid frame for Gas Price
#   root.mid5_frame - the fifth mid frame to diplay the results
#   root.bottom_frame - the bottom frame for the three button
#   root.logo, root.logo_label, root.logo_label.image, root.logo_label.pack - the image png logo
#   root.yearMakeModel_label - label for Year/Make/Model
#   root.yearMakeModel_entry - entry text box for Year/Make/Model
#   root.mpg_label - label for MPG
#   root.mpg_entry - entry text box for MPG
#   root.mileagePoint_label - label for mileage point
#   root.mileagePoint_entry - entry text box for mileage point
#   root.gasPrice_label - label for gas price
#   root.gasPrice_entry - entry text box for gas price
#   root.results_label - label for "Total cost is $"
#   root.totalCost - str to show the dollar amount calculation
#   root.totalCost_label - label for total cost
#   root.Reset_button - button to clear all the entry boxes
#   root.Calculate_button - button to calculate the dollar amount for gas consumption
#   root.quit_button - button to close the program
#   root.totalCost1 - str to show the dollar amount calculation and reset to 0 if the
#                       reset button is pressed (float)
#   root.mileagePoint - to get the mileagePoint entry (int)
#   root.mpg - to get the mpg entry (int)
#   root.gasPrice - to get the gasPrice entry (float)

import tkinter
from tkinter import *
from PIL import Image, ImageTk

class GasSpenderGUI:
    def __init__(root):
        # Create the main window
        root.main_window = tkinter.Tk()
        root.main_window.title("Gas $pender")
        root.main_window.geometry("400x300")

        # Create the frames
        root.top_frame = tkinter.Frame(root.main_window)
        root.mid_frame = tkinter.Frame(root.main_window)
        root.mid2_frame = tkinter.Frame(root.main_window)
        root.mid3_frame = tkinter.Frame(root.main_window)
        root.mid4_frame = tkinter.Frame(root.main_window)
        root.mid5_frame = tkinter.Frame(root.main_window)
        root.bottom_frame = tkinter.Frame(root.main_window)

        # Create Logo and put it into the top frame
        root.logo = Image.open('GasSpender.png')
        root.logo = ImageTk.PhotoImage(root.logo)
        root.logo_label = tkinter.Label(image=root.logo)
        root.logo_label.image = root.logo
        root.logo_label.pack(side="top")

        # Create widgets for the mid frames
        #root.yearMakeModel_label = tkinter.Label(root.mid_frame, \
                                                 #text = "Year/Make/Model: ", font = "Raleway")
        #root.yearMakeModel_entry = tkinter.Entry(root.mid_frame, width = 25)
        root.mpg_label = tkinter.Label(root.mid2_frame, \
                                       text = "How many miles per gallon? ", font = "Raleway")
        root.mpg_entry = tkinter.Entry(root.mid2_frame, width = 4)
        root.mileagePoint_label = tkinter.Label(root.mid3_frame, \
                                                text = "Mileage point (Ex. 100000) ", font = "Raleway")
        root.mileagePoint_entry = tkinter.Entry(root.mid3_frame, width = 7)
        root.gasPrice_label = tkinter.Label(root.mid4_frame, \
                                            text = "What is the price of gas per gallon? ", font = "Raleway")
        root.gasPrice_entry = tkinter.Entry(root.mid4_frame, width = 5)

        # Pack the mid frame widgets
        #root.yearMakeModel_label.pack(side="left")
        #root.yearMakeModel_entry.pack(side="left")
        root.mpg_label.pack(side="left")
        root.mpg_entry.pack(side="left")
        root.mileagePoint_label.pack(side="left")
        root.mileagePoint_entry.pack(side="left")
        root.gasPrice_label.pack(side="left")
        root.gasPrice_entry.pack(side="left")

        # Create widgets for the middle frame
        root.results_label = tkinter.Label(root.mid5_frame, \
                                           text = "Total cost is $", font = "Raleway")
        
        # Create a blank label to show the total cost
        root.totalCost = tkinter.StringVar()
        root.totalCost_label = tkinter.Label(root.mid5_frame, \
                                             textvariable = root.totalCost)

        # Pack the middle frame widget
        root.results_label.pack(side="left")
        root.totalCost_label.pack(side="left")

        #Create the buttons for the bottom frame
        root.Reset_button = tkinter.Button(root.bottom_frame, \
                                                  text = "Reset", font = "Raleway", \
                                                  height = 2, width = 7, bg="#e0c996", \
                                                  command = root.reset)
        root.Calculate_button = tkinter.Button(root.bottom_frame, \
                                                  text = "Calculate", font = "Raleway", \
                                                  height = 3, width = 12, bg="#e0c996", \
                                                  command = root.calculate_TotalCost)
        root.quit_button = tkinter.Button(root.bottom_frame, \
                                                  text = "Quit", font = "Raleway", \
                                                  height = 2, width = 7, bg="#e0c996", \
                                                  command = root.main_window.destroy)

        # Pack the bottom frame widgets
        root.Reset_button.pack(side="left", padx=6)
        root.Calculate_button.pack(side="left", padx=6)
        root.quit_button.pack(side="left", padx=6)

        # Pack the frames
        root.top_frame.pack()
        root.mid_frame.pack()
        root.mid2_frame.pack()
        root.mid3_frame.pack()
        root.mid4_frame.pack()
        root.mid5_frame.pack()
        root.bottom_frame.pack()

        # Enter the inter main loop()
        tkinter.mainloop()

    # Define the reset button to clear all the entry boxes and totalcost1
    def reset(root):
        #root.yearMakeModel_entry.delete(0, END)
        root.mpg_entry.delete(0, END)
        root.mileagePoint_entry.delete(0, END)
        root.gasPrice_entry.delete(0, END)
        root.totalCost1 = 0
        root.totalCost.set(format(root.totalCost1, '.2f'))
        
    # Define the calculate button
    def calculate_TotalCost(root):
        root.mileagePoint = int(root.mileagePoint_entry.get())
        root.mpg = int(root.mpg_entry.get())
        root.gasPrice = float(root.gasPrice_entry.get())
        root.totalCost1 = (root.mileagePoint / root.mpg) * root.gasPrice
        root.totalCost.set(format(root.totalCost1, '.2f'))

# Create an instance of the class
totalCost = GasSpenderGUI()
        

        
