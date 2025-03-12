import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Exempel GUI")

# Labels och inmatningsfält
tk.Label(root, text="Förnamn:").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text="Efternamn:").grid(row=1, column=0)
tk.Entry(root).grid(row=1, column=1)

# Knappar
def visa_meddelande():
    print("Knappen trycktes!")
    print(val.get())  # Skriver ut det valda värdet, t.ex. "M", "K", eller "A"

tk.Button(root, text="Skicka", command=visa_meddelande).grid(row=2, column=0, columnspan=3, sticky="ew")

# Radioknappar
val = tk.StringVar()
tk.Radiobutton(root, text="Man", variable=val, value="M").grid(row=3, column=0)
tk.Radiobutton(root, text="Kvinna", variable=val, value="K").grid(row=3, column=1)
tk.Radiobutton(root, text="Annat", variable=val, value="A").grid(row=3, column=2)


# Textområde
tk.Text(root, height=5, width=30).grid(row=4, column=0, columnspan=3)

# Treeview-tabell
tree = ttk.Treeview(root, columns=("Namn_col", "Ålder_col"), show="headings")
tree.heading("Namn_col", text="Namn")
tree.heading("Ålder_col", text="Ålder")
tree.insert("", "end", values=("Sara", 25))
tree.insert("", "end", values=("Kalle", 30))
tree.grid(row=5, column=0, columnspan=3)

root.mainloop()