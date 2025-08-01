import tkinter as tk
from tkinter import messagebox
from database import Database

class EditReservationPage(tk.Frame):
    def __init__(self, parent, controller, reservation_id):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.reservation_id = reservation_id
        self.db = Database()

        label = tk.Label(self, text="Edit Reservation", font=("Arial", 16))
        label.pack(pady=10)

        self.entries = {}
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]

        for field in fields:
            frame = tk.Frame(self)
            frame.pack(fill="x", padx=20, pady=5)
            
            tk.Label(frame, text=field, width=15).pack(side="left")
            entry = tk.Entry(frame)
            entry.pack(side="right", expand=True, fill="x")
            self.entries[field] = entry

        self.load_data()

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=20)

        update_btn = tk.Button(btn_frame, text="Update", command=self.update_reservation)
        update_btn.pack(side="left", padx=10)

        cancel_btn = tk.Button(btn_frame, text="Cancel", command=lambda: controller.show_frame("ViewPage"))
        cancel_btn.pack(side="left")

    def load_data(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM reservations WHERE id=?", (self.reservation_id,))
            row = cursor.fetchone()

            if row:
                self.entries["Name"].insert(0, row[1])
                self.entries["Flight Number"].insert(0, row[2])
                self.entries["Departure"].insert(0, row[3])
                self.entries["Destination"].insert(0, row[4])
                self.entries["Date"].insert(0, row[5])
                self.entries["Seat Number"].insert(0, row[6])

            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {str(e)}")
            self.controller.show_frame("ViewPage")

    def update_reservation(self):
        try:
            values = (
                self.entries["Name"].get(),
                self.entries["Flight Number"].get(),
                self.entries["Departure"].get(),
                self.entries["Destination"].get(),
                self.entries["Date"].get(),
                self.entries["Seat Number"].get(),
                self.reservation_id
            )

            if "" in values[:-1]:
                messagebox.showwarning("Warning", "All fields must be filled")
                return

            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE reservations 
                SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
                WHERE id=?
            """, values)
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Reservation updated")
            self.controller.show_frame("ViewPage")
        except Exception as e:
            messagebox.showerror("Error", f"Update failed: {str(e)}")