import tkinter as tk  # Import the Tkinter library for creating GUI applications
from tkinter import messagebox  # Import messagebox for displaying pop-up messages

# Main application class that inherits from tk.Tk
class Application(tk.Tk):
    def __init__(self):
        super().__init__()  # Initialize the parent class (Tk)
        self.title("Box Company Management System")  # Set the window title
        self.geometry("500x400")  # Set the window size

        # Dictionary to hold all the frames (pages of the app)
        self.frames = {}
        
        # Initialize and store all the frames (StartPage, ClientPortal, StaffPortal, QuotePage)
        for F in (StartPage, ClientPortal, StaffPortal, QuotePage):
            frame = F(self)  # Create an instance of each frame
            self.frames[F] = frame  # Store the frame in the dictionary
            frame.grid(row=0, column=0, sticky="nsew")  # Position each frame to cover the entire window
        
        # Show the first page (StartPage) when the app starts
        self.show_frame(StartPage)
    
    # Method to bring the requested frame to the front
    def show_frame(self, page_class):
        frame = self.frames[page_class]  # Retrieve the frame based on the page class
        frame.tkraise()  # Bring the frame to the top of the stacking order

# Class for the starting page
class StartPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)  # Initialize the parent class (Frame)
        self.parent = parent  # Store a reference to the parent (Application)

        # Create buttons for navigating to the Client Portal and Staff Portal
        tk.Button(self, text="Client Portal", command=self.open_client_portal).pack(pady=20)
        tk.Button(self, text="Staff Portal", command=self.open_staff_portal).pack(pady=20)
    
    # Method to navigate to the Client Portal
    def open_client_portal(self):
        self.parent.show_frame(ClientPortal)
    
    # Method to navigate to the Staff Portal
    def open_staff_portal(self):
        self.parent.show_frame(StaffPortal)

# Class for the Client Portal
class ClientPortal(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)  # Initialize the parent class (Frame)
        self.parent = parent  # Store a reference to the parent (Application)
        
        # Create a label and a button to navigate to the Quote Page
        tk.Label(self, text="Client Portal").pack(pady=20)
        tk.Button(self, text="Get a Quote", command=self.open_quote_page).pack(pady=10)
        tk.Button(self, text="Back", command=self.go_back).pack(pady=10)
    
    # Method to navigate to the Quote Page
    def open_quote_page(self):
        self.parent.show_frame(QuotePage)

    # Method to go back to the Start Page
    def go_back(self):
        self.parent.show_frame(StartPage)

# Class for the Quote Page where clients can select options and get a quote
class QuotePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)  # Initialize the parent class (Frame)
        self.parent = parent  # Store a reference to the parent (Application)
        self.cart = []  # List to hold the items added to the cart
        self.vat_rate = 0.15  # VAT rate of 15%

        # Page title
        tk.Label(self, text="Quote Page").pack(pady=10)

        # Dropdown menu for selecting box dimensions
        tk.Label(self, text="Select Box Dimensions (cm):").pack()
        self.dimensions_var = tk.StringVar(value="30x30x30")  # Default value for dimensions
        tk.OptionMenu(self, self.dimensions_var, "30x30x30", "40x40x40", "50x50x50").pack()

        # Dropdown menu for selecting box quality
        tk.Label(self, text="Select Box Quality:").pack()
        self.quality_var = tk.StringVar(value="Standard")  # Default value for quality
        tk.OptionMenu(self, self.quality_var, "Standard", "Premium").pack()

        # Label to display the calculated price
        self.price_label = tk.Label(self, text="Price: ")
        self.price_label.pack(pady=10)

        # Buttons for calculating price, adding to cart, and placing order
        tk.Button(self, text="Calculate Price", command=self.calculate_price).pack(pady=5)
        tk.Button(self, text="Add to Cart", command=self.add_to_cart).pack(pady=5)
        tk.Button(self, text="Place Order & Generate Invoice", command=self.generate_invoice).pack(pady=10)
        tk.Button(self, text="Back", command=self.go_back).pack(pady=10)

    # Method to calculate the price based on selected options
    def calculate_price(self):
        dimensions = self.dimensions_var.get()  # Get selected dimensions
        quality = self.quality_var.get()  # Get selected quality

        # Pricing logic (this can be replaced with actual pricing rules)
        base_price = 20  # Base price for any box
        if dimensions == "40x40x40":
            base_price += 10
        elif dimensions == "50x50x50":
            base_price += 20
        
        if quality == "Premium":
            base_price += 15

        # Include VAT in the final price
        price_with_vat = base_price + (base_price * self.vat_rate)
        self.price_label.config(text=f"Price: {price_with_vat:.2f} (Including VAT)")  # Update the price label

        # Store the calculated price for adding to the cart later
        self.current_price = price_with_vat

    # Method to add the current selection to the cart
    def add_to_cart(self):
        dimensions = self.dimensions_var.get()  # Get selected dimensions
        quality = self.quality_var.get()  # Get selected quality
        price = getattr(self, 'current_price', 0)  # Get the calculated price

        # Ensure that the price has been calculated before adding to cart
        if price:
            self.cart.append((dimensions, quality, price))  # Add the item to the cart
            messagebox.showinfo("Cart", f"Added to cart: {dimensions}, {quality}, {price:.2f}")  # Show confirmation
        else:
            messagebox.showerror("Error", "Please calculate the price first")  # Show error if no price is calculated

    # Method to generate an invoice based on the items in the cart
    def generate_invoice(self):
        # Ensure that there are items in the cart
        if not self.cart:
            messagebox.showerror("Error", "Your cart is empty!")
            return
        
        # Build the invoice
        invoice = "Invoice:\n\n"
        total = 0  # Total cost for all items
        for item in self.cart:
            dimensions, quality, price = item
            invoice += f"{dimensions} - {quality}: {price:.2f}\n"  # Add item details to the invoice
            total += price  # Update the total cost
        
        invoice += f"\nTotal: {total:.2f} (Including VAT)"  # Add the total to the invoice
        messagebox.showinfo("Invoice", invoice)  # Show the invoice in a messagebox
    
    # Method to go back to the Client Portal
    def go_back(self):
        self.parent.show_frame(ClientPortal)

# Class for the Staff Portal where staff members can log in
class StaffPortal(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)  # Initialize the parent class (Frame)
        
        profile_var = tk.StringVar()  # Variable to hold the selected user profile
        
        # Create radio buttons for selecting a user profile
        tk.Label(self, text="Select User Profile").pack(pady=10)
        tk.Radiobutton(self, text="Staff", variable=profile_var, value="Staff").pack()
        tk.Radiobutton(self, text="Manager", variable=profile_var, value="Manager").pack()
        tk.Radiobutton(self, text="Business Owner", variable=profile_var, value="Business Owner").pack()
        
        # Username and password fields for login
        tk.Label(self, text="Username").pack(pady=5)
        username_entry = tk.Entry(self)  # Entry field for username
        username_entry.pack()
        
        tk.Label(self, text="Password").pack(pady=5)
        password_entry = tk.Entry(self, show="*")  # Entry field for password (masked input)
        password_entry.pack()
        
        # Button to handle the login process
        tk.Button(self, text="Login", command=lambda: self.authenticate_user(profile_var, username_entry, password_entry)).pack(pady=20)
        tk.Button(self, text="Back", command=self.go_back).pack(pady=10)
    
    # Method to handle user authentication (this is just a placeholder)
    def authenticate_user(self, profile_var, username_entry, password_entry):
        profile = profile_var.get()  # Get the selected profile
        username = username_entry.get()  # Get the entered username
        password = password_entry.get()  #
