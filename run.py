import tkinter as tk
import webbrowser

def open_browser():
    webbrowser.open("https://hackedscreen.com/")

def show_warning():
    root = tk.Tk()
    root.title("System Alert")
    root.geometry("400x200")
    root.resizable(False, False)
    tk.Label(root, text="Your system is infected!", font=("Arial", 14), fg="red").pack(pady=20)
    tk.Label(root, text="Click 'Fix Now' to resolve the issue.", font=("Arial", 12)).pack(pady=10)
    tk.Button(root, text="Fix Now", command=open_browser, bg="red", fg="white", width=15).pack(pady=20)
    root.after(100, lambda: root.destroy())  # Automatically close after 100ms
    root.mainloop()

# Display the alert 100 times without requiring user interaction to close
for _ in range(1):
    show_warning()
    open_browser()




# python -m PyInstaller --onefile --noconsole .\setup.py

