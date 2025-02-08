import tkinter as tk

def center_window(window, width, height):
    x = (window.winfo_screenwidth() - width) // 2
    y = (window.winfo_screenheight() - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


root = tk.Tk()
root.title("Bonjour")
root.configure(bg="ivory")
center_window(root,400,80)

tk.Label(root,text="Bonjour tout le monde !",font=("Arial", 12, "bold"),fg="dark blue",bg="ivory").pack(pady=10)
tk.Button(root,text="Quitter",command=root.quit,font=("Arial", 10, "bold"),bg="light grey",relief="raised").pack()

root.mainloop()
