import tkinter as tk
from tkinter import font
from autocomplete_model import AddressAutocompleteModel
from load_addresses import load_addresses_from_csv

# Update the path to your actual CSV
address_list = load_addresses_from_csv("Data\cayuga-addresses-county.csv")

model = AddressAutocompleteModel(address_list)


def on_key_release(event):
    query = entry.get()
    suggestions = model.suggest(query)
    listbox.delete(0, tk.END)
    for suggestion in suggestions:
        listbox.insert(tk.END, suggestion)
    if suggestions:
        listbox.place(x=entry.winfo_x(), y=entry.winfo_y() + entry.winfo_height() + 2)
    else:
        listbox.place_forget()

def on_select(event):
    if listbox.curselection():
        selected = listbox.get(listbox.curselection())
        entry.delete(0, tk.END)
        entry.insert(0, selected)
        listbox.place_forget()

root = tk.Tk()
root.title("Smart Address Autocomplete")
root.geometry("600x200")
root.configure(bg="#f9f9f9")

title_font = font.Font(family="Helvetica", size=14, weight="bold")
entry_font = font.Font(family="Segoe UI", size=12)
list_font = font.Font(family="Segoe UI", size=11)

title = tk.Label(root, text="Enter your address", font=title_font, bg="#f9f9f9")
title.pack(pady=(20, 10))

entry = tk.Entry(root, font=entry_font, bd=2, relief="solid", width=50)
entry.pack(ipady=6)
entry.bind("<KeyRelease>", on_key_release)

listbox = tk.Listbox(root, font=list_font, width=50, height=5, bd=1, relief="solid", bg="#ffffff", highlightthickness=0)
listbox.bind("<<ListboxSelect>>", on_select)

root.mainloop()
