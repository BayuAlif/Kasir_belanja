import requests
import tkinter as tk
from tkinter import ttk, messagebox

def getAnimeByName(name):
    # URL API Jikan untuk mendapatkan daftar anime berdasarkan nama
    url = f"https://api.jikan.moe/v4/anime?q={name}"  # Menggunakan parameter 'q'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['data']
    else:
        print("Gagal", f"Terjadi kesalahan saat mengambil data anime: {response.status_code}")
        return []

def animeResultDisplay():
    name = name_entry.get()  # Mengambil nama anime dari input

    if not name:
        messagebox.showerror("Error", "Nama anime tidak boleh kosong!")
        return

    # Mendapatkan daftar anime berdasarkan nama
    anime_list = getAnimeByName(name)

    # Menghapus item sebelumnya di Treeview
    for item in anime_tree.get_children():
        anime_tree.delete(item)

    for anime in anime_list:
        # Memeriksa apakah genre ada sebelum mengaksesnya
        genre = anime["genres"][0]["name"] if anime["genres"] else "N/A"

        anime_tree.insert("", "end", values=(anime["title"], anime["year"], genre, anime["score"]))


# Setup jendela utama
root = tk.Tk()
root.title("Pencarian Anime")

# Bagian untuk memasukkan nama anime
ttk.Label(root, text="Masukkan nama anime: ").pack(pady=10)

name_entry = tk.Entry(root)  # Input untuk nama anime
name_entry.pack(pady=5)

# Output dari pencarian anime
columns = ("Title", "Year", "Genre", "Score")
anime_tree = ttk.Treeview(root, columns=columns, show="headings")

# Mengatur judul kolom
anime_tree.heading("Title", text="Judul Anime")
anime_tree.heading("Year", text="Tahun Rilis")
anime_tree.heading("Genre", text="Genre Anime")
anime_tree.heading("Score", text="Skor Anime")
anime_tree.pack(pady=20)

# Tombol untuk mencari
search_button = ttk.Button(root, text="Cari anime", command=animeResultDisplay)
search_button.pack(pady=10)

# Memulai loop utama aplikasi
print("Program dimulai")
root.mainloop()
print("Program ditutup")
