import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Gestionnaire de Produits")
root.geometry("1200x800")

# Frame for buttons on the left
button_frame = tk.Frame(root, width=200, bg="lightgray")
button_frame.pack(side="left", fill="y")

# Add 8 buttons to the left frame
for i in range(1, 9):
    button = tk.Button(button_frame, text=f"Button {i}", width=20, height=2)
    button.pack(pady=15)

# Frame for the product list on the right
list_frame = tk.Frame(root)
list_frame.pack(side="right", fill="both", expand=True)

# Label for the product list
list_label = tk.Label(list_frame, text="Liste de Produits", font=("Arial", 14))
list_label.pack(pady=10)

# Treeview widget for displaying products and their characteristics
columns = ("Id", "Nom", "Type", "Stock", "Prix")
product_list = ttk.Treeview(list_frame, columns=columns, show="headings")
product_list.heading("Id", text="Id")
product_list.heading("Nom", text="Nom")
product_list.heading("Type", text="Type")
product_list.heading("Stock", text="Stock")
product_list.heading("Prix", text="Prix")
product_list.pack(fill="both", expand=True)

product_list.insert("", "end", values=(1, "Produit 1", "Type A", 10, 19.99))
product_list.insert("", "end", values=(2, "Produit 2", "Type B", 5, 29.99)) 

# Start the main event loop
root.mainloop()