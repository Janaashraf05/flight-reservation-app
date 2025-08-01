import tkinter as tk
from tkinter import messagebox
from database import Database

class BookingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.db = Database()

        tk.Label(self, text="Book a Flight", font=("Arial", 18)).pack(pady=10)

        self.entries = {}
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        
        for field in fields:
            tk.Label(self, text=field).pack()
            entry = tk.Entry(self, width=30)
            entry.pack()
            self.entries[field] = entry

        tk.Button(self, text="Submit", width=15, command=self.submit_booking).pack(pady=10)
        tk.Button(self, text="Back to Home", width=15, command=lambda: controller.show_frame("HomePage")).pack()

    def submit_booking(self):
        data = [self.entries[field].get() for field in self.entries]

        if "" in data:
            messagebox.showwarning("Warning", "All fields must be filled")
            return

        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
                VALUES (?, ?, ?, ?, ?, ?)
            """, data)
            conn.commit()
            messagebox.showinfo("Success", "Flight booked successfully!")
            
            for entry in self.entries.values():
                entry.delete(0, tk.END)
                
        except Exception as e:
            messagebox.showerror("Error", f"Booking failed: {str(e)}")
        finally:
            if 'conn' in locals():
                conn.close()






