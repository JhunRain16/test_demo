import tkinter as tk
from tkinter import messagebox
import Facebook

class FacebookGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Facebook GUI")
        self.master.geometry("400x200")

        self.label = tk.Label(self.master, text="Enter Access Token:")
        self.label.pack()

        self.access_token_entry = tk.Entry(self.master)
        self.access_token_entry.pack()

        self.login_button = tk.Button(self.master, text="Login", command=self.login)
        self.login_button.pack()

        self.info_label = tk.Label(self.master, text="")
        self.info_label.pack()

    def login(self):
        access_token = self.access_token_entry.get()
        try:
            graph = Facebook.GraphAPI(access_token)
            profile = graph.get_object("me")
            info = f"Name: {profile['name']}\nID: {profile['id']}"
            self.info_label.config(text=info)
        except Facebook.GraphAPIError as e:
            messagebox.showerror("Error", e.message)

def main():
    root = tk.Tk()
    facebook_gui = FacebookGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
