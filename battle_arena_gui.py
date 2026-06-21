import tkinter as tk
from tkinter import ttk
import random
from characters.warrior import Warrior
from characters.mage import Mage

class BattleArenaGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("OOP Retro Battle Arena")
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
        self.combat_log.insert(tk.END, message + "\n\n")
        self.combat_log.see(tk.END) 

    def update_bars(self):
        self.p1_hp_bar["value"] = self.player.get_health()
        self.p1_res_bar["value"] = self.player.get_resource()
        self.p2_hp_bar["value"] = self.enemy.get_health()
        self.p2_res_bar["value"] = self.enemy.get_resource()

    def execute_turn(self, action):
        if self.player.get_health() <= 0 or self.enemy.get_health() <= 0:
            return

        if action == "attack":
            msg = self.player.attack(self.enemy)
        elif action == "special":
            msg = self.player.special_move(self.enemy)
            if "❌" in msg: 
                self.log_message(msg)
                return
        elif action == "heal":
            msg = self.player.heal()
            
        self.log_message(f"--- YOUR TURN ---\n{msg}")
        self.update_bars()

        if self.enemy.get_health() <= 0:
            self.log_message("🏆 VICTORY! The enemy has been defeated!")
            return

        self.window.after(1000, self.enemy_ai)

    def enemy_ai(self):
        if self.enemy.get_health() < 30 and self.enemy.get_resource() >= 30:
            msg = self.enemy.heal()
        elif self.enemy.get_resource() >= 40:
            msg = self.enemy.special_move(self.player)
        else:
            msg = self.enemy.attack(self.player)

        self.log_message(f"--- ENEMY TURN ---\n{msg}")
        self.update_bars()

        if self.player.get_health() <= 0:
            self.log_message("💀 DEFEAT! You have fallen in battle...")

if __name__ == "__main__":
    root = tk.Tk()
    app = BattleArenaGUI(root)
    root.mainloop()

