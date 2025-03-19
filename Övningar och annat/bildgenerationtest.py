import tkinter as tk
from tkinter import Entry, Button, Label
import requests
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image, ImageTk


def fetch_image():
    query = entry.get()
    search_url = f"https://www.google.com/search?tbm=isch&q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    image_tags = soup.find_all("img")
    if len(image_tags) > 1:
        img_url = image_tags[1]["src"]  # Första bilden är oftast Googles logga, så vi tar den andra
        image_response = requests.get(img_url)
        img_data = Image.open(BytesIO(image_response.content))
        img_data = img_data.resize((300, 300))  # Ändra storlek på bilden
        img = ImageTk.PhotoImage(img_data)

        img_label.config(image=img)
        img_label.image = img
    else:
        img_label.config(text="Ingen bild hittades.")


# Skapa Tkinter GUI
root = tk.Tk()
root.title("Bildsökare")

Label(root, text="Skriv ett nyckelord:").pack()
entry = Entry(root)
entry.pack()

btn = Button(root, text="Sök bild", command=fetch_image)
btn.pack()

img_label = Label(root)
img_label.pack()

root.mainloop()