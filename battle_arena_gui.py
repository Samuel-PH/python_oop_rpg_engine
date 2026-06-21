import tkinter as tk
from tkinter import ttk
import random
from characters.warrior import Warrior
from characters.mage import Mage




class BattleArenaGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Retro Battle Arena")
        self.window.geometry("600x550")
        self.window.configure(bg="#1e272e") 
        
        self.player = Warrior("Arthas (You)")
        self.enemy = Mage("Jaina (AI)")

        self.setup_ui()

def setup_ui(self):
        tk.Label(self.window, text="⚔️ BATTLE ARENA ⚔️", font=("Courier", 22, "bold"), bg="#1e272e", fg="#ffdd59").pack(pady=10)

        stats_frame = tk.Frame(self.window, bg="#1e272e")
        stats_frame.pack(fill=tk.X, padx=20)

        p1_frame = tk.Frame(stats_frame, bg="#1e272e")
        p1_frame.pack(side=tk.LEFT)
        self.p1_label = tk.Label(p1_frame, text=f"{self.player.name}", bg="#1e272e", fg="white", font=("Arial", 12, "bold"))
        self.p1_label.pack()
        self.p1_hp_bar = ttk.Progressbar(p1_frame, length=150, maximum=150, value=self.player.get_health())
        self.p1_hp_bar.pack(pady=2)
        self.p1_res_bar = ttk.Progressbar(p1_frame, length=150, maximum=100, value=self.player.get_resource())
        self.p1_res_bar.pack()
        tk.Label(p1_frame, text="Red: HP | Blue: Rage", bg="#1e272e", fg="gray", font=("Arial", 8)).pack()

        p2_frame = tk.Frame(stats_frame, bg="#1e272e")
        p2_frame.pack(side=tk.RIGHT)
        self.p2_label = tk.Label(p2_frame, text=f"{self.enemy.name}", bg="#1e272e", fg="white", font=("Arial", 12, "bold"))
        self.p2_label.pack()
        self.p2_hp_bar = ttk.Progressbar(p2_frame, length=150, maximum=80, value=self.enemy.get_health())
        self.p2_hp_bar.pack(pady=2)
        self.p2_res_bar = ttk.Progressbar(p2_frame, length=150, maximum=100, value=self.enemy.get_resource())
        self.p2_res_bar.pack()
        tk.Label(p2_frame, text="Red: HP | Blue: Mana", bg="#1e272e", fg="gray", font=("Arial", 8)).pack()

        self.combat_log = tk.Text(self.window, height=12, width=65, bg="black", fg="#0be881", font=("Courier", 10))
        self.combat_log.pack(pady=20)
        self.log_message("System: Battle Initialized. Player turn.")

        btn_frame = tk.Frame(self.window, bg="#1e272e")
        btn_frame.pack()
        
        tk.Button(btn_frame, text="🗡️ Attack", command=lambda: self.execute_turn("attack"), bg="#3c40c6", fg="white", width=12).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="💥 Special", command=lambda: self.execute_turn("special"), bg="#ff3f34", fg="white", width=12).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="🩹 Heal", command=lambda: self.execute_turn("heal"), bg="#05c46b", fg="white", width=12).grid(row=0, column=2, padx=10)

 def log_message(self, message):
     
 def update_bars(self):
     
 def execute_turn(self, action):
     
 def enemy_ai(self):
     







if __name__ == "__main__":
    root = tk.Tk()
    app = BattleArenaGUI(root)
    root.mainloop()