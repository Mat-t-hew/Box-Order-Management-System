import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Box Company Management System")
        self.geometry("600x450")
        self.configure(bg="#f0f0f0")  # Set background color
        
        self.frames = {}
        for F in (StartPage, ClientPortal, StaffPortal, QuotePage):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(StartPage)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="lightblue")
        self.parent = parent
        
        # Title with custom font and color
        tk.Label(self, text="Welcome to the Box Management System", font=("Helvetica", 18, "bold"), bg="lightblue", fg="darkblue").pack(pady=30)
        
        # Buttons with custom styling
        tk.Button(self, text="Client Portal", command=self.open_client_portal, font=("Helvetica", 14), bg="blue", fg="white").pack(pady=20)
        tk.Button(self, text="Staff Portal", command=self.open_staff_portal, font=("Helvetica", 14), bg="green", fg="white").pack(pady=20)
    
    def open_client_portal(self):
        self.parent.show_frame(ClientPortal)
    
    def open_staff_portal(self):
        self.parent.show_frame(StaffPortal)

class ClientPortal(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#e6f7ff")
        self.parent = parent
        
        tk.Label(self, text="Client Portal", font=("Helvetica", 18, "bold"), bg="#e6f7ff").pack(pady=30)
        tk.Button(self, text="Get a Quote", command=self.open_quote_page, font=("Helvetica", 14), bg="blue", fg="white").pack(pady=20)
        tk.Button(self, text="Back", command=self.go_back, font=("Helvetica", 14), bg="red", fg="white").pack(pady=10)

    def open_quote_page(self):
        self.parent.show_frame(QuotePage)

    def go_back(self):
        self.parent.show_frame(StartPage)

class StaffPortal(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#d9f9d9")
        self.parent = parent

        profile_var = tk.StringVar()
        
        tk.Label(self, text="Select User Profile", font=("Helvetica", 16), bg="#d9f9d9").pack(pady=10)
        tk.Radiobutton(self, text="Staff", variable=profile_var, value="Staff", font=("Helvetica", 12), bg="#d9f9d9").pack()
        tk.Radiobutton(self, text="Manager", variable=profile_var, value="Manager", font=("Helvetica", 12), bg="#d9f9d9").pack()
        tk.Radiobutton(self, text="Business Owner", variable=profile_var, value="Business Owner", font=("Helvetica", 12), bg="#d9f9d9").pack()
        
        tk.Label(self, text="Username", font=("Helvetica", 12), bg="#d9f9d9").pack(pady=10)
        username_entry = tk.Entry(self)
        username_entry.pack()
        
        tk.Label(self, text="Password", font=("Helvetica", 12), bg="#d9f9d9").pack(pady=10)
        password_entry = tk.Entry(self, show="*")
        password_entry.pack()
        
        ttk.Style().configure("TButton", padding=6, relief="flat", background="#1E90FF")
        tk.Button(self, text="Login", command=lambda: self.authenticate_user(profile_var, username_entry, password_entry), bg="green", fg="white", font=("Helvetica", 14)).pack(pady=20)
        tk.Button(self, text="Back", command=self.go_back, bg="red", fg="white", font=("Helvetica", 14)).pack(pady=10)

    def authenticate_user(self, profile_var, username_entry, password_entry):
        profile = profile_var.get()
        username = username_entry.get()
        password = password_entry.get()
        messagebox.showinfo("Login", f"Profile: {profile}\nUsername: {username}\nPassword: {password}")

    def go_back(self):
        self.parent.show_frame(StartPage)

class QuotePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="lightyellow")
        tk.Label(self, text="Quote Page", font=("Helvetica", 18, "bold"), bg="lightyellow").pack(pady=30)
        tk.Button(self, text="Back", command=self.go_back, font=("Helvetica", 14), bg="red", fg="white").pack(pady=20)

    def go_back(self):
        self.parent.show_frame(ClientPortal)

if __name__ == "__main__":
    app = Application()
    app.mainloop()