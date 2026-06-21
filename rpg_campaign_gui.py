import tkinter as tk
from tkinter import ttk
import random
from characters.warrior import Warrior
from characters.mage import Mage
from enemies.monsters import Goblin, Orc, DarkElf, DemonLord

class BattleArenaGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Campaign Engine")
        self.window.geometry("700x700")
        self.window.configure(bg="#1e272e") 
        
        self.player_class = None
        self.player = None
        self.enemy = None
        self.level = 1
        
        self.menu_frame = tk.Frame(self.window, bg="#1e272e")
        self.combat_frame = tk.Frame(self.window, bg="#1e272e")
        self.post_frame = tk.Frame(self.window, bg="#1e272e")
        
        self.build_menu_ui()
        self.build_combat_ui()
        self.build_post_ui()
        self.show_menu()

    def show_menu(self):
        self.combat_frame.pack_forget()
        self.post_frame.pack_forget()
        self.menu_frame.pack(fill=tk.BOTH, expand=True)

    def show_combat(self):
        self.menu_frame.pack_forget()
        self.post_frame.pack_forget()
        self.combat_frame.pack(fill=tk.BOTH, expand=True)

    def show_post_battle(self, victory):
        self.combat_frame.pack_forget()
        self.post_result_label.config(text="🏆 VICTORY!" if victory else "💀 DEFEAT!")
        self.next_level_btn.config(state="normal" if victory and self.level < 10 else "disabled")
        if self.level == 10 and victory: self.post_result_label.config(text="👑 CAMPAIGN COMPLETE! 👑")
        self.post_frame.pack(fill=tk.BOTH, expand=True)

    def start_game(self, char_class):
        self.player_class = char_class
        if char_class == "Warrior": 
            self.player = Warrior("Arthas (You)")
            self.btn_defend.config(text="🛡️ Block/Parry")
            self.btn_utility.config(text="🗣️ Warcry")
        else: 
            self.player = Mage("Jaina (You)")
            self.btn_defend.config(text="🛡️ Barrier")
            self.btn_utility.config(text="🧘 Channel Mana")
            
        self.level = 1
        self.load_level()
        self.show_combat()

    def load_level(self):
        self.player.full_heal()
        
        if self.level == 10: 
            self.enemy = DemonLord()
        elif self.level == 8: # Rival Battle
            self.enemy = Mage("Rival Mage") if self.player_class == "Warrior" else Warrior("Rival Warrior")
        else:
            self.enemy = random.choice([Goblin(), Orc(), DarkElf()])
        
        self.p1_label.config(text=self.player.name)
        self.p2_label.config(text=self.enemy.name)
        self.p1_hp_bar.config(maximum=self.player.max_health)
        self.p2_hp_bar.config(maximum=self.enemy.get_health())
        
        self.combat_log.delete(1.0, tk.END)
        self.log_message(f"--- LOCATION {self.level}/10 REACHED ---")
        if self.level == 10: self.log_message("🔥 THE DEMON LORD AWAITS! 🔥")
        elif self.level == 8: self.log_message("⚔️ YOUR RIVAL APPEARS! ⚔️")
        else: self.log_message(f"A wild {self.enemy.name} blocks your path!")
        self.update_bars()

    def proceed_next_level(self):
        self.level += 1
        self.load_level()
        self.show_combat()

    def build_menu_ui(self):
        tk.Label(self.menu_frame, text="⚔️ CAMPAIGN ⚔️", font=("Courier", 30, "bold"), bg="#1e272e", fg="#ffdd59").pack(pady=50)
        tk.Button(self.menu_frame, text="🗡️ Play Warrior", font=("Arial", 14), bg="#ff4757", fg="white", width=20, command=lambda: self.start_game("Warrior")).pack(pady=10)
        tk.Button(self.menu_frame, text="✨ Play Mage", font=("Arial", 14), bg="#1e90ff", fg="white", width=20, command=lambda: self.start_game("Mage")).pack(pady=10)

    def build_post_ui(self):
        self.post_result_label = tk.Label(self.post_frame, text="", font=("Courier", 30, "bold"), bg="#1e272e", fg="#ffdd59")
        self.post_result_label.pack(pady=50)
        self.next_level_btn = tk.Button(self.post_frame, text="🗺️ Next Location", font=("Arial", 14), bg="#0be881", width=25, command=self.proceed_next_level)
        self.next_level_btn.pack(pady=20)
        tk.Button(self.post_frame, text="🏠 Main Menu", font=("Arial", 14), bg="#57606f", fg="white", width=25, command=self.show_menu).pack(pady=10)

    def build_combat_ui(self):
        stats_frame = tk.Frame(self.combat_frame, bg="#1e272e")
        stats_frame.pack(fill=tk.X, padx=20, pady=10)

        p1_frame = tk.Frame(stats_frame, bg="#1e272e")
        p1_frame.pack(side=tk.LEFT)
        self.p1_label = tk.Label(p1_frame, text="", bg="#1e272e", fg="white", font=("Arial", 12, "bold"))
        self.p1_label.pack()
        self.p1_hp_bar = ttk.Progressbar(p1_frame, length=180)
        self.p1_hp_bar.pack(pady=2)
        self.p1_res_bar = ttk.Progressbar(p1_frame, length=180, maximum=100)
        self.p1_res_bar.pack()

        p2_frame = tk.Frame(stats_frame, bg="#1e272e")
        p2_frame.pack(side=tk.RIGHT)
        self.p2_label = tk.Label(p2_frame, text="", bg="#1e272e", fg="white", font=("Arial", 12, "bold"))
        self.p2_label.pack()
        self.p2_hp_bar = ttk.Progressbar(p2_frame, length=180)
        self.p2_hp_bar.pack(pady=2)

        self.combat_log = tk.Text(self.combat_frame, height=18, width=70, bg="black", fg="#0be881", font=("Courier", 10))
        self.combat_log.pack(pady=10)

        btn_frame = tk.Frame(self.combat_frame, bg="#1e272e")
        btn_frame.pack()
        
        tk.Button(btn_frame, text="🗡️ Attack", command=lambda: self.execute_turn("attack"), bg="#3c40c6", fg="white", width=15).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="💥 Special", command=lambda: self.execute_turn("special"), bg="#ff3f34", fg="white", width=15).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="🩹 Heal", command=lambda: self.execute_turn("heal"), bg="#05c46b", fg="white", width=15).grid(row=0, column=2, padx=5, pady=5)
        
        self.btn_defend = tk.Button(btn_frame, text="🛡️ Defend", command=lambda: self.execute_turn("defend"), bg="#808e9b", fg="white", width=15)
        self.btn_defend.grid(row=1, column=0, columnspan=1, padx=5, pady=5)
        self.btn_utility = tk.Button(btn_frame, text="⚙️ Utility", command=lambda: self.execute_turn("utility"), bg="#808e9b", fg="white", width=15)
        self.btn_utility.grid(row=1, column=2, columnspan=1, padx=5, pady=5)

    def log_message(self, message):
        if message.strip():
            self.combat_log.insert(tk.END, message + "\n\n")
            self.combat_log.see(tk.END) 

    def update_bars(self):
        self.p1_hp_bar["value"] = self.player.get_health()
        self.p1_res_bar["value"] = self.player.get_resource()
        self.p2_hp_bar["value"] = self.enemy.get_health()

    def execute_turn(self, action):
        if self.player.get_health() <= 0 or self.enemy.get_health() <= 0: return 

        # Player Stun Check
        if self.player.statuses["stunned"]:
            self.log_message(f"💫 YOUR TURN SKIPPED! {self.player.name} is Stunned!")
            self.player.statuses["stunned"] = False
        else:
            mood_msg = self.player.roll_mood()
            if action == "attack": action_msg = self.player.attack(self.enemy)
            elif action == "special": action_msg = self.player.special_move(self.enemy)
            elif action == "heal": action_msg = self.player.heal()
            elif action == "defend": action_msg = self.player.defend()
            elif action == "utility": action_msg = self.player.utility(self.enemy)
                
            if "❌" in action_msg: # Action failed (e.g., no mana), refund turn
                self.log_message(action_msg)
                return
                
            self.log_message(f"--- YOUR TURN ---\n{mood_msg}\n{action_msg}")

        self.log_message(self.player.process_statuses()) # Apply player DoTs
        self.update_bars()

        if self.enemy.get_health() <= 0:
            self.window.after(1500, lambda: self.show_post_battle(victory=True))
            return

        self.window.after(1000, self.enemy_ai) 

    def enemy_ai(self):
        if self.enemy.statuses["stunned"]:
            self.log_message(f"💫 ENEMY TURN SKIPPED! {self.enemy.name} is Stunned!")
            self.enemy.statuses["stunned"] = False
        else:
            mood_msg = self.enemy.roll_mood()
            
            # AI Scaling based on Level & HP
            hp_pct = (self.enemy.get_health() / (self.enemy.get_health() + 1)) * 100
            
            if self.level >= 5 and hp_pct < 40 and random.randint(1,100) > 50:
                action_msg = self.enemy.defend()
            elif self.level == 10 and self.player.get_health() > 50 and self.enemy.get_resource() >= 40:
                action_msg = self.enemy.special_move(self.player) # Smart Demon Lord
            elif hp_pct < 30 and self.enemy.get_resource() >= 30: 
                action_msg = self.enemy.heal()
            else: 
                action_msg = self.enemy.attack(self.player)

            self.log_message(f"--- ENEMY TURN ---\n{mood_msg}\n{action_msg}")

        self.log_message(self.enemy.process_statuses()) # Apply enemy DoTs
        self.update_bars()

        if self.player.get_health() <= 0:
            self.window.after(1500, lambda: self.show_post_battle(victory=False))

if __name__ == "__main__":
    root = tk.Tk()
    app = BattleArenaGUI(root)
    root.mainloop()