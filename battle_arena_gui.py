import tkinter as tk
from tkinter import ttk
import random
from characters.warrior import Warrior





class BattleArenaGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Retro Battle Arena")
        self.window.geometry("600x550")
        self.window.configure(bg="#1e272e") 
        
        self.player = Warrior("Arthas (You)")
        
        self.setup_ui()


