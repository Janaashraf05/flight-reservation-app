import tkinter as tk
from home import HomePage
from booking import BookingPage
from view import ViewPage
from edit_reservation import EditReservationPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flight Reservation System")
        self.geometry("600x500")
        self.resizable(True, True)

        # Main container setup
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Initialize all pages except EditReservationPage
        for F in (HomePage, BookingPage, ViewPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # EditReservationPage will be created when needed
        self.frames["EditReservationPage"] = None

        self.show_frame("HomePage")

    def show_frame(self, page_name, *args):
        """Show a frame for the given page name"""
        if page_name == "EditReservationPage":
            # Create new instance with reservation_id when editing
            if self.frames["EditReservationPage"] is not None:
                self.frames["EditReservationPage"].destroy()
            
            frame = EditReservationPage(
                parent=self.container,
                controller=self,
                reservation_id=args[0] if args else None
            )
            self.frames["EditReservationPage"] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        else:
            frame = self.frames[page_name]
        
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()