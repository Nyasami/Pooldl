import tkinter as tk
from tkinter import filedialog
import gsAPI
def browse_folder(folder_path_entry):
    folder_path = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_path)

def run_code(text_input, folder_path_entry):
    
    input_text = text_input.get()
    folder_path = folder_path_entry.get()
    if folder_path == "":
        print("Please choose a folder to save the file")
        return
    if input_text == "":
        print("Please enter the sheet link")
        return
    gsAPI.download_map(input_text, folder_path)
    

def create_popup_window():
    popup = tk.Tk()
    popup.geometry("400x200")
    popup.title("Asami's mappool downloader")
    icon_image = tk.PhotoImage(file="icon.png")
    popup.wm_iconphoto(True, icon_image)

    input_label = tk.Label(popup, text="Enter link:")
    input_label.pack()
    input_field = tk.Entry(popup, width=50)
    input_field.pack()
    input_label2 = tk.Label(popup, text="Select folder:")
    input_label2.pack()
    folder_path_entry = tk.Entry(popup)
    folder_path_entry.pack()
    browse_button = tk.Button(popup, text="Browse", command=lambda: browse_folder(folder_path_entry))
    browse_button.pack()
    input_label3 = tk.Label(popup, text="Please see the log behind this window -->\nDon't worry if this window isn't responding")
    input_label3.pack()
    button = tk.Button(popup, text="Download!", command=lambda: run_code(input_field, folder_path_entry))
    button.pack()

    popup.mainloop()

create_popup_window() 