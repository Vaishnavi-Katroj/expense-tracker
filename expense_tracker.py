import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

FILE_NAME = "expenses.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Category", "Amount", "Note"])

def add_expense():
    date = date_entry.get()
    category = category_combo.get()
    amount = amount_entry.get()
    note = note_entry.get()

    if date == "" or category == "" or amount == "":
        messagebox.showerror("Error", "Fill all required fields")
        return

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, note])

    load_expenses()
    clear_fields()

def load_expenses():
    for row in tree.get_children():
        tree.delete(row)

    total = 0
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            tree.insert("", tk.END, values=row)
            total += float(row[2])

    total_label.config(text=f"Total Expense: ₹{total}")

def clear_fields():
    date_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    note_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Smart Expense Tracker")
root.geometry("700x500")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Date (DD-MM-YYYY)").grid(row=0, column=0)
date_entry = tk.Entry(frame)
date_entry.grid(row=0, column=1)

tk.Label(frame, text="Category").grid(row=1, column=0)
category_combo = ttk.Combobox(frame, values=["Food", "Travel", "Shopping", "Bills", "Other"])
category_combo.grid(row=1, column=1)

tk.Label(frame, text="Amount").grid(row=2, column=0)
amount_entry = tk.Entry(frame)
amount_entry.grid(row=2, column=1)

tk.Label(frame, text="Note").grid(row=3, column=0)
note_entry = tk.Entry(frame)
note_entry.grid(row=3, column=1)

tk.Button(frame, text="Add Expense", command=add_expense).grid(row=4, columnspan=2, pady=10)

columns = ("Date", "Category", "Amount", "Note")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(fill=tk.BOTH, expand=True)

total_label = tk.Label(root, text="Total Expense: ₹0", font=("Arial", 12, "bold"))
total_label.pack(pady=10)

load_expenses()
root.mainloop()
