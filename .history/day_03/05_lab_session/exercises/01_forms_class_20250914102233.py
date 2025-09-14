import tkinter as tk
from tkinter import messagebox
import json

class FormApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User Feedback Form")

        # Form variables
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.theme_var = tk.StringVar(value="Light")
        self.subscribe_var = tk.BooleanVar()
        self.rating_var = tk.IntVar(value=3)

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(padx=10, pady=10)

        # Build sections
        self.build_name()
        self.build_age()
        self.build_theme()
        self.build_subscription()
        self.build_rating()
        self.build_submit_button()

    def build_name(self):
        tk.Label(self.main_frame, text="Name:").grid(row=0, column=0, sticky="e")
        tk.Entry(self.main_frame, textvariable=self.name_var).grid(row=0, column=1, sticky="w")

    def build_age(self):
        tk.Label(self.main_frame, text="Age:").grid(row=1, column=0, sticky="e")
        tk.Entry(self.main_frame, textvariable=self.age_var).grid(row=1, column=1, sticky="w")

    def build_theme(self):
        tk.Label(self.main_frame, text="Theme:").grid(row=2, column=0, sticky="e")
        themes = ["Light", "Dark", "Blue"]
        for i, theme in enumerate(themes):
            tk.Radiobutton(
                self.main_frame, text=theme, variable=self.theme_var, value=theme
            ).grid(row=2, column=1 + i, sticky="w")

    def build_subscription(self):
        tk.Checkbutton(
            self.main_frame, text="Subscribe to newsletter", variable=self.subscribe_var
        ).grid(row=3, column=1, sticky="w")

    def build_rating(self):
        tk.Label(self.main_frame, text="Rating:").grid(row=4, column=0, sticky="e")
        tk.Scale(
            self.main_frame, from_=1, to=5, orient="horizontal", variable=self.rating_var
        ).grid(row=4, column=1, sticky="w")

    def build_submit_button(self):
        tk.Button(
            self.main_frame, text="Submit", command=self.save_to_json
        ).grid(row=5, column=0, columnspan=3, pady=10)

    def save_to_json(self):
        data = {
            "name": self.name_var.get(),
            "age": self.age_var.get(),
            "theme": self.theme_var.get(),
            "subscribe": self.subscribe_var.get(),
            "rating": self.rating_var.get(),
        }
        try:
            with open("feedback.json", "w") as f:
                json.dump(data, f, indent=4)
            messagebox.showinfo("Success", "Feedback saved to feedback.json")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save: {e}")

if __name__ == "__main__":
    app = FormApp()
    app.mainloop()
