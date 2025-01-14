import json
import os
import tkinter as tk
from tkinter import messagebox
import html

def load_memories(file_path):
    if not os.path.isfile(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_memories(file_path, memories):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(memories, file, ensure_ascii=False, indent=4)

def add_memory_entry():
    title = title_entry.get()
    artist = artist_entry.get()
    pic = pic_entry.get()
    mp3 = mp3_entry.get()
    date = date_entry.get()
    article = article_entry.get("1.0", tk.END).strip()

    if not all([title, artist, pic, mp3, date, article]):
        messagebox.showerror("Input Error", "All fields must be filled out!")
        return

    # Escape HTML characters in the article
    article = html.escape(article)

    # Replace newlines with <br> tags
    article = article.replace('\n', '<br>')

    new_entry = {
        "title": title,
        "artist": artist,
        "pic": pic,
        "mp3": mp3,
        "date": date,
        "article": article
    }

    memories.append(new_entry)
    save_memories('memp.json', memories)
    messagebox.showinfo("Success", "New entry added successfully!")
    clear_entries()

def clear_entries():
    title_entry.delete(0, tk.END)
    artist_entry.delete(0, tk.END)
    pic_entry.delete(0, tk.END)
    mp3_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    article_entry.delete("1.0", tk.END)

# Load existing memories
memories = load_memories('memp.json')

# Set up the GUI
root = tk.Tk()
root.title("Add Memory Entry")

# Configure grid weights for responsiveness
root.columnconfigure(1, weight=1)
for i in range(6):
    root.rowconfigure(i, weight=1)

# Create and place labels and entries
tk.Label(root, text="Title").grid(row=0, column=0, padx=10, pady=5, sticky="ew")
title_entry = tk.Entry(root, width=40)
title_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Artist").grid(row=1, column=0, padx=10, pady=5, sticky="ew")
artist_entry = tk.Entry(root, width=40)
artist_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Picture File Name").grid(row=2, column=0, padx=10, pady=5, sticky="ew")
pic_entry = tk.Entry(root, width=40)
pic_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="MP3 File Name").grid(row=3, column=0, padx=10, pady=5, sticky="ew")
mp3_entry = tk.Entry(root, width=40)
mp3_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Date (YYYY/MM/DD)").grid(row=4, column=0, padx=10, pady=5, sticky="ew")
date_entry = tk.Entry(root, width=40)
date_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Article (HTML format)").grid(row=5, column=0, padx=10, pady=5, sticky="ew")
article_entry = tk.Text(root, width=40, height=5)
article_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

# Add button
add_button = tk.Button(root, text="Add Entry", command=add_memory_entry)
add_button.grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")

# Start the GUI event loop
root.mainloop()
