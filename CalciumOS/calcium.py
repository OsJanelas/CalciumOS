import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import time
import webbrowser

class CalciumOS:
    def __init__(self, root):
        self.root = root
        self.root.title("CalciumOS v3.0 - Estrutura Forte")
        self.root.geometry("1000x700")
        
        # Configurações de Tema
        self.themes = {
            "Padrão (Osso)": {"bg": "#E3DAC9", "fg": "black", "task": "#D2B48C"},
            "Noturno (Cálcio)": {"bg": "#2C3E50", "fg": "white", "task": "#1A252F"},
            "Matrix": {"bg": "black", "fg": "#00FF00", "task": "#003300"}
        }
        self.current_theme = "Padrão (Osso)"

        # Wallpaper e Desktop
        self.desktop = tk.Frame(self.root, bg=self.themes[self.current_theme]["bg"])
        self.desktop.pack(expand=True, fill="both")

        # Barra de Tarefas
        self.taskbar = tk.Frame(self.root, bg=self.themes[self.current_theme]["task"], height=45)
        self.taskbar.pack(side="bottom", fill="x")

        self.setup_ui()

    def setup_ui(self):
        # Botão Iniciar
        self.btn_start = tk.Button(self.taskbar, text="🦴 Iniciar", command=self.menu_iniciar, bg="#F5F5F5")
        self.btn_start.pack(side="left", padx=5, pady=5)

        # Ícones do Desktop
        self.add_icon("📂 Arquivos", self.app_explorer, 20, 20)
        self.add_icon("📝 Notas", self.app_notes, 20, 100)
        self.add_icon("💻 Prompt", self.app_terminal, 20, 180)
        self.add_icon("🌐 Navegador", self.app_browser, 20, 260)
        self.add_icon("🎮 Jogo", self.app_game, 20, 340)
        self.add_icon("🎨 Temas", self.app_themes, 20, 420)

        # Relógio
        self.lbl_clock = tk.Label(self.taskbar, bg=self.taskbar["bg"], fg="white", font=("Arial", 10))
        self.lbl_clock.pack(side="right", padx=10)
        self.update_clock()

    def add_icon(self, text, command, x, y):
        btn = tk.Button(self.desktop, text=text, command=command, bg="white", relief="flat", width=12)
        btn.place(x=x, y=y)

    def create_window(self, title, width=400, height=300):
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry(f"{width}x{height}")
        win.configure(bg="#F0F0F0")
        return win

    # --- APLICATIVOS ---

    def app_explorer(self):
        win = self.create_window("Explorador de Arquivos")
        path = os.getcwd()
        listbox = tk.Listbox(win)
        listbox.pack(expand=True, fill="both", pady=10)
        for item in os.listdir(path):
            listbox.insert(tk.END, f" {item}")

    def app_notes(self):
        win = self.create_window("Bloco de Notas", 500, 400)
        text_area = tk.Text(win)
        text_area.pack(expand=True, fill="both")
        
        menu = tk.Menu(win)
        win.config(menu=menu)
        file_menu = tk.Menu(menu)
        menu.add_cascade(label="Arquivo", menu=file_menu)
        file_menu.add_command(label="Salvar", command=lambda: messagebox.showinfo("Ca-OS", "Nota Calificada!"))

    def app_terminal(self):
        win = self.create_window("Calcium Prompt", 600, 300)
        win.configure(bg="black")
        entry = tk.Entry(win, bg="black", fg="#00FF00", insertbackground="white")
        entry.pack(side="bottom", fill="x")
        output = tk.Text(win, bg="black", fg="#00FF00")
        output.pack(expand=True, fill="both")
        output.insert(tk.END, "CalciumOS [Versão 3.0]\n(c) 2026 Laboratórios K. Digite comandos...\n\n")

    def app_browser(self):
        # Simulação de Navegador abrindo o Google real
        webbrowser.open("https://www.google.com")

    def app_game(self):
        win = self.create_window("Jogo: Clique no Osso", 300, 200)
        self.score = 0
        btn_osso = tk.Button(win, text="🦴", font=("Arial", 20), command=lambda: self.update_score(lbl))
        btn_osso.pack(pady=20)
        lbl = tk.Label(win, text="Score: 0")
        lbl.pack()

    def update_score(self, lbl):
        self.score += 1
        lbl.config(text=f"Score: {self.score}")

    def app_themes(self):
        win = self.create_window("Gerenciador de Temas")
        for t_name in self.themes:
            tk.Button(win, text=t_name, command=lambda n=t_name: self.apply_theme(n)).pack(fill="x", pady=5)

    def apply_theme(self, name):
        theme = self.themes[name]
        self.desktop.config(bg=theme["bg"])
        self.taskbar.config(bg=theme["task"])
        self.lbl_clock.config(bg=theme["task"], fg=theme["fg"])
        self.current_theme = name

    def update_clock(self):
        self.lbl_clock.config(text=time.strftime("%H:%M:%S"))
        self.root.after(1000, self.update_clock)

    def menu_iniciar(self):
        messagebox.showinfo("Cálcio Menu", "Sistema operacional 100% forte e saudável.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalciumOS(root)
    root.mainloop()