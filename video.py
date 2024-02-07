import tkinter as tk
from pytube import YouTube
import os
def download_video():
    url = url_text.get(1.0, "end-1c")
    yt = YouTube(url)
    folder_path = "downloads"

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    stream = yt.streams.get_highest_resolution()
    stream.download(output_path=folder_path)
    label.config(text="Відео завантажено!", fg="white")

window = tk.Tk()
window.title("Завантаження відео з YouTube")
window.geometry("500x300")

frame = tk.Frame(window, bg="#bd1b0f", padx=10, pady=10)
frame.pack(fill="both", expand="true")

label = tk.Label(frame, text="Вставте URL відео з YouTube:", font=("Arial", 12), width=40, height=2, fg="white", bg="#8c8787")
label.config(relief="solid")
label.config(borderwidth=1)
label.pack(pady=10)



url_text = tk.Text(frame, wrap=tk.WORD, width=40, height=2, font=("Arial", 12))
url_text.pack(pady=10)
url_text.config(highlightthickness=2)
url_text.config(highlightbackground="#910f06")


button = tk.Button(frame, text="Завантажити відео", command=download_video, fg="white", bg="#8c8787", font=("Arial", 12,))
button.config(relief="solid", borderwidth=1)
button.pack(padx=10, pady=10)

window.mainloop()
