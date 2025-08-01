import tkinter as tk
from tkinter import ttk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Title label
        label = ttk.Label(self, text="Flight Reservation System", font=("Arial", 18, "bold"))
        label.pack(pady=30)

        # Book Flight Button
        book_btn = ttk.Button(self, text="Book Flight", command=lambda: controller.show_frame("BookingPage"))
        book_btn.pack(pady=10)

         #View Page Button
        view_btn = ttk.Button(self, text="View Reservations", command=lambda: controller.show_frame("ViewPage"))
        view_btn.pack(pady=10)

        
       
