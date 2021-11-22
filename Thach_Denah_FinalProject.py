# Program Name: Thach_Denah_FinalProject
# Author: Denah Thach
# Date: 11/21/2021
# Summary: GUI to allow a user to make a food order
# Variables:

import tkinter as tk

# Create the main window
main_window = tk.Tk()
main_window.title("WhatPhoDenah")
main_window.geometry("500x400")
#main_window.configure(background="tan")

# Create label
title_label = tk.Label(main_window, text = "WhatPhoDenah!?", font=("Raleway", 25)).pack()
#title_label.grid()

# Create button to start the order
order_button = tk.Button(main_window, bg="tan", text="Make an Order!").pack()
#order_button.grid()


# Enter the inter main loop()
tk.mainloop()
                                                

        
