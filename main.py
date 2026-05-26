import customtkinter as ctk 
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Projeto de wild ")
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="Olá, seja bem-vindo ao meu projeto de wild!")
        self.label.pack(pady=20)

        self.button = ctk.CTkButton(self, text="clique aqui ", command=self.button_click)
        self.button.pack(pady=10)

    def button_click(self):
        self.label.configure(text="Você clicou no botão!")
if __name__ == "__main__":
    app = App()
    app.mainloop()
