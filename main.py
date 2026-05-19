import customtkinter as ctk 
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CustomTkinter App")
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="Hello, CustomTkinter!")
        self.label.pack(pady=20)

        self.button = ctk.CTkButton(self, text="Click Me", command=self.button_click)
        self.button.pack(pady=10)

    def button_click(self):
        self.label.configure(text="Button Clicked!")
if __name__ == "__main__":
    app = App()
    app.mainloop()
