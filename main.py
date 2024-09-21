import tkinter as tk
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Box Company Management System")  # Set the title of the main application window
        self.geometry("500x400")  # Set the dimensions of the window
        
        # Initialize the frames for navigation
        self.frames = {}
        for F in (StartPage, ClientPortal, StaffPortal, QuotePage):
            frame = F(self)  # Create a frame for each page
            self.frames[F] = frame  # Store the frame in a dictionary
            frame.grid(row=0, column=0, sticky="nsew")  # Use grid layout for frames
        
        # Show the starting page initially
        self.show_frame(StartPage)
    
    def show_frame(self, page_class):
        """Raise the specified frame to the front for display."""
        frame = self.frames[page_class]
        frame.tkraise()  # Bring the specified frame to the top

class StartPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        # Create buttons for navigating to the Client and Staff portals
        tk.Button(self, text="Client Portal", command=self.open_client_portal).pack(pady=20)
        tk.Button(self, text="Staff Portal", command=self.open_staff_portal).pack(pady=20)
    
    def open_client_portal(self):
        """Navigate to the Client Portal page."""
        self.parent.show_frame(ClientPortal)
    
    def open_staff_portal(self):
        """Navigate to the Staff Portal page."""
        self.parent.show_frame(StaffPortal)

class ClientPortal(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        tk.Label(self, text="Client Portal").pack(pady=20)  # Title label for Client Portal
        tk.Button(self, text="Get a Quote", command=self.open_quote_page).pack(pady=10)  # Button to get a quote
        tk.Button(self, text="Back", command=self.go_back).pack(pady=10)  # Button to return to Start Page
    
    def open_quote_page(self):
        """Navigate to the Quote page for box ordering."""
        self.parent.show_frame(QuotePage)

    def go_back(self):
        """Return to the Start Page."""
        self.parent.show_frame(StartPage)

class QuotePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.cart = []  # Initialize an empty cart
        self.vat_rate = 0.15  # Define VAT rate (15%)

        # Sample inventory data for available boxes
        self.inventory = {
            "30x30x30": {"Standard": 10, "Premium": 5},  # Dimensions and available qualities
            "40x40x40": {"Standard": 0, "Premium": 8},
            "50x50x50": {"Standard": 2, "Premium": 1},
        }

        tk.Label(self, text="Quote Page").pack(pady=10)  # Title label for Quote Page

        # Box dimensions selection
        tk.Label(self, text="Select Box Dimensions (cm):").pack()
        self.dimensions_var = tk.StringVar(value="30x30x30")  # Default selection
        tk.OptionMenu(self, self.dimensions_var, *self.inventory.keys()).pack()  # Dropdown for dimensions

        # Box quality selection
        tk.Label(self, text="Select Box Quality:").pack()
        self.quality_var = tk.StringVar(value="Standard")  # Default selection
        tk.OptionMenu(self, self.quality_var, "Standard", "Premium").pack()  # Dropdown for quality

        # Quantity entry field
        tk.Label(self, text="Quantity:").pack()
        self.quantity_entry = tk.Entry(self)  # Entry for quantity
        self.quantity_entry.pack()

        # Label to display calculated price
        self.price_label = tk.Label(self, text="Price: ")
        self.price_label.pack(pady=10)

        # Buttons for actions
        tk.Button(self, text="Calculate Price", command=self.calculate_price).pack(pady=5)  # Calculate price
        tk.Button(self, text="Add to Cart", command=self.add_to_cart).pack(pady=5)  # Add item to cart
        tk.Button(self, text="Place Order & Generate Invoice", command=self.generate_invoice).pack(pady=10)  # Generate invoice
        tk.Button(self, text="Back", command=self.go_back).pack(pady=10)  # Back to Client Portal

        # Cart management section
        self.cart_frame = tk.Frame(self)  # Frame for cart
        self.cart_frame.pack(pady=10)
        tk.Label(self.cart_frame, text="Items in Cart:").pack()  # Label for cart items
        self.cart_listbox = tk.Listbox(self.cart_frame, width=50)  # Listbox to show cart items
        self.cart_listbox.pack()
        tk.Button(self.cart_frame, text="Remove Selected Item", command=self.remove_from_cart).pack(pady=5)  # Button to remove item

    def calculate_price(self):
        """Calculate the price based on selected dimensions, quality, and VAT."""
        dimensions = self.dimensions_var.get()
        quality = self.quality_var.get()

        # Simple pricing logic based on dimensions
        base_price = 20  # Base price for any box
        if dimensions == "40x40x40":
            base_price += 10
        elif dimensions == "50x50x50":
            base_price += 20
        
        if quality == "Premium":
            base_price += 15  # Add price for premium quality

        # Calculate price including VAT
        price_with_vat = base_price + (base_price * self.vat_rate)
        self.price_label.config(text=f"Price: {price_with_vat:.2f} (Including VAT)")  # Update price label

        # Store the calculated price for adding to cart later
        self.current_price = price_with_vat

    def add_to_cart(self):
        """Add selected item to the cart."""
        dimensions = self.dimensions_var.get()
        quality = self.quality_var.get()
        price = getattr(self, 'current_price', 0)  # Get the current calculated price
        quantity = self.quantity_entry.get()  # Get the quantity entered

        # Validate the quantity input
        if not quantity.isdigit():
            messagebox.showerror("Error", "Please enter a valid quantity")
            return

        quantity = int(quantity)  # Convert quantity to integer

        # Check inventory for availability
        if dimensions in self.inventory:
            if quality in self.inventory[dimensions]:
                available_quantity = self.inventory[dimensions][quality]  # Get available quantity
                if available_quantity < quantity:
                    messagebox.showerror("Error", f"Only {available_quantity} available for {dimensions} - {quality}")
                    return
                if available_quantity == 0:
                    messagebox.showerror("Error", "Selection out of stock")
                    return
            
                # Add item to cart if all checks are fine
                self.cart.append((dimensions, quality, price, quantity))
                self.update_cart_listbox()  # Update cart display
                messagebox.showinfo("Cart", f"Added to cart: {dimensions}, {quality}, {quantity}, {price:.2f}")
            else:
                messagebox.showerror("Error", "Selected quality not available")
        else:
            messagebox.showerror("Error", "Selected dimensions not available")

    def update_cart_listbox(self):
        """Update the cart listbox display."""
        self.cart_listbox.delete(0, tk.END)  # Clear the listbox
        for item in self.cart:
            dimensions, quality, price, quantity = item
            # Insert each item into the listbox
            self.cart_listbox.insert(tk.END, f"{quantity} x {dimensions} - {quality}: {price:.2f}")

    def remove_from_cart(self):
        """Remove the selected item from the cart."""
        selected_index = self.cart_listbox.curselection()  # Get selected item index
        if selected_index:
            del self.cart[selected_index[0]]  # Remove the selected item from cart
            self.update_cart_listbox()  # Update cart display
            messagebox.showinfo("Cart", "Item removed from cart")
        else:
            messagebox.showerror("Error", "Select an item to remove")

    def generate_invoice(self):
        """Generate and display an invoice based on cart contents."""
        if not self.cart:
            messagebox.showerror("Error", "Your cart is empty!")  # Check if cart is empty
            return
        
        invoice = "Invoice:\n\n"  # Initialize invoice string
        total = 0  # Total price counter
        for item in self.cart:
            dimensions, quality, price, quantity = item
            invoice += f"{quantity} x {dimensions} - {quality}: {price:.2f}\n"  # Add item details to invoice
            total += price * quantity  # Calculate total price
        
        invoice += f"\nTotal: {total:.2f} (Including VAT)"  # Add total price to invoice
        messagebox.showinfo("Invoice", invoice)  # Display invoice

    def go_back(self):
        """Return to the Client Portal page."""
        self.parent.show_frame(Client
