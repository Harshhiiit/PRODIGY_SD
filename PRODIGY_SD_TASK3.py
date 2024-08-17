import tkinter as tk
from tkinter import messagebox, simpledialog

# File to store contacts
contacts_file = "contacts.txt"

# Function to load contacts from the file
def load_contacts():
    contacts = {}
    try:
        with open(contacts_file, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                contacts[name] = {"phone": phone, "email": email}
    except FileNotFoundError:
        pass
    return contacts

# Function to save contacts to the file
def save_contacts(contacts):
    with open(contacts_file, "w") as file:
        for name, info in contacts.items():
            file.write(f"{name},{info['phone']},{info['email']}\n")

# Function to add a new contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()

    if name and phone and email:
        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)
        update_contact_list()
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter all fields.")

# Function to update the contact list in the GUI
def update_contact_list():
    listbox_contacts.delete(0, tk.END)
    for name in contacts:
        listbox_contacts.insert(tk.END, name)

# Function to view a selected contact's details
def view_contact():
    selected_contact = listbox_contacts.get(tk.ACTIVE)
    if selected_contact:
        info = contacts[selected_contact]
        messagebox.showinfo("Contact Details", f"Name: {selected_contact}\nPhone: {info['phone']}\nEmail: {info['email']}")

# Function to delete a selected contact
def delete_contact():
    selected_contact = listbox_contacts.get(tk.ACTIVE)
    if selected_contact:
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {selected_contact}?"):
            del contacts[selected_contact]
            save_contacts(contacts)
            update_contact_list()

# Function to edit a selected contact
def edit_contact():
    selected_contact = listbox_contacts.get(tk.ACTIVE)
    if selected_contact:
        new_name = simpledialog.askstring("Edit Name", "Enter new name:", initialvalue=selected_contact)
        new_phone = simpledialog.askstring("Edit Phone", "Enter new phone number:", initialvalue=contacts[selected_contact]["phone"])
        new_email = simpledialog.askstring("Edit Email", "Enter new email address:", initialvalue=contacts[selected_contact]["email"])

        if new_name and new_phone and new_email:
            del contacts[selected_contact]
            contacts[new_name] = {"phone": new_phone, "email": new_email}
            save_contacts(contacts)
            update_contact_list()

# Main program setup
root = tk.Tk()
root.title("Contact Manager")

# Load contacts from file
contacts = load_contacts()

# GUI Elements
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_phone = tk.Label(root, text="Phone:")
label_phone.grid(row=1, column=0, padx=10, pady=5)

entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1, padx=10, pady=5)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=5)

entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

button_add = tk.Button(root, text="Add Contact", command=add_contact)
button_add.grid(row=3, column=1, padx=10, pady=10)

listbox_contacts = tk.Listbox(root)
listbox_contacts.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

button_view = tk.Button(root, text="View Contact", command=view_contact)
button_view.grid(row=5, column=0, padx=10, pady=5, sticky="ew")

button_edit = tk.Button(root, text="Edit Contact", command=edit_contact)
button_edit.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

button_delete = tk.Button(root, text="Delete Contact", command=delete_contact)
button_delete.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Update the contact list on startup
update_contact_list()

# Start the GUI event loop
root.mainloop()
