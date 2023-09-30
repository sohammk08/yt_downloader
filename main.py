import tkinter
import customtkinter
from pytube import YouTube

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Video Downloader")

# Run app (loop)
app.mainloop()