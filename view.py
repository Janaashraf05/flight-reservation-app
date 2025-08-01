import tkinter as tk
from tkinter import ttk, messagebox
from database import Database

class ViewPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.db = Database()

        tk.Label(self, text="All Reservations", font=("Arial", 18)).pack(pady=10)

        # Treeview setup
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Flight", "From", "To", "Date", "Seat"), 
                               show="headings", height=10)
        
        # Column configuration
        self.tree.column("ID", width=50)
        self.tree.column("Name", width=120)
        self.tree.column("Flight", width=100)
        self.tree.column("From", width=100)
        self.tree.column("To", width=100)
        self.tree.column("Date", width=100)
        self.tree.column("Seat", width=80)
        
        # Headings
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        
        self.tree.pack(fill="x", padx=10, pady=5)

        # Button frame
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Edit", width=10, 
                 command=self.edit_reservation).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delete", width=10,
                 command=self.delete_reservation).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Refresh", width=10,
                 command=self.refresh_table).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Back", width=10,
                 command=lambda: self.controller.show_frame("HomePage")).pack(side="right", padx=5)

        # Initial load
        self.refresh_table()

    def refresh_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM reservations")
            
            for row in cursor.fetchall():
                self.tree.insert("", "end", values=row)
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {str(e)}")
        finally:
            if 'conn' in locals():
                conn.close()

    def edit_reservation(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Warning", "Please select a reservation first")
            return
            
        self.controller.show_frame("EditReservationPage", self.tree.item(selected)["values"][0])

    def delete_reservation(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Warning", "Please select a reservation first")
            return
            
        if messagebox.askyesno("Confirm", "Delete this reservation?"):
            try:
                conn = self.db.get_connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM reservations WHERE id=?", (self.tree.item(selected)["values"][0],))
                conn.commit()
                self.refresh_table()
            except Exception as e:
                messagebox.showerror("Error", f"Delete failed: {str(e)}")
            finally:
                if 'conn' in locals():
                    conn.close()






    
    
    


