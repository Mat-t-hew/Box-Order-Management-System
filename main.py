import tkinter as tk
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Box Company Management System")
        self.geometry("400x300")
        
        # Initialize the frames
        self.frames = {}
        for F in (StartPage, ClientPortal, StaffPortal):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Show the starting page
        self.show_frame(StartPage)
    
    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()
    
class StartPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        # Create buttons for each portal
        tk.Button(self, text="Client Portal", command=self.open_client_portal).pack(pady=20)
        tk.Button(self, text="Staff Portal", command=self.open_staff_portal).pack(pady=20)
    
    def open_client_portal(self):
        self.parent.show_frame(ClientPortal)
    
    def open_staff_portal(self):
        self.parent.show_frame(StaffPortal)

class ClientPortal(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        tk.Label(self, text="Client Portal functionality goes here").pack(pady=20)
        tk.Button(self, text="Back", command=self.go_back).pack(pady=10)
    
    def go_back(self):
        self.parent.show_frame(StartPage)

class StaffPortal(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        profile_var = tk.StringVar()
        
        tk.Label(self, text="Select User Profile").pack(pady=10)
        tk.Radiobutton(self, text="Staff", variable=profile_var, value="Staff").pack()
        tk.Radiobutton(self, text="Manager", variable=profile_var, value="Manager").pack()
        tk.Radiobutton(self, text="Business Owner", variable=profile_var, value="Business Owner").pack()
        
        tk.Label(self, text="Username").pack(pady=5)
        username_entry = tk.Entry(self)
        username_entry.pack()
        
        tk.Label(self, text="Password").pack(pady=5)
        password_entry = tk.Entry(self, show="*")
        password_entry.pack()
        
        tk.Button(self, text="Login", command=lambda: self.authenticate_user(profile_var, username_entry, password_entry)).pack(pady=20)
        tk.Button(self, text="Back", command=self.go_back).pack(pady=10)
    
    def authenticate_user(self, profile_var, username_entry, password_entry):
        profile = profile_var.get()
        username = username_entry.get()
        password = password_entry.get()
        # Add authentication logic here
        messagebox.showinfo("Login", f"Profile: {profile}\nUsername: {username}\nPassword: {password}")
    
    def go_back(self):
        self.parent.show_frame(StartPage)

# Run the application
if __name__ == "__main__":
    app = Application()
    app.mainloop()