import tkinter as tk
import random

class ShootingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Valorant-like Shooting Game")
        self.master.geometry("800x600")

        self.canvas = tk.Canvas(self.master, width=800, height=600, bg="black")
        self.canvas.pack()

        self.player_size = 20
        self.player = self.canvas.create_rectangle(390, 290, 410, 310, fill="blue")

        self.target_radius = 20
        self.target = self.canvas.create_oval(0, 0, 0, 0, fill="red")

        self.score = 0
        self.score_label = tk.Label(self.master, text="Score: 0", fg="white", bg="black")
        self.score_label.pack()

        self.canvas.bind("<Motion>", self.move_player)
        self.canvas.bind("<Button-1>", self.shoot)

        self.move_target()

    def move_target(self):
        x = random.randint(self.target_radius, 800 - self.target_radius)
        y = random.randint(self.target_radius, 600 - self.target_radius)
        self.canvas.coords(self.target, x - self.target_radius, 
                                          y - self.target_radius,
                                          x + self.target_radius, 
                                          y + self.target_radius)
        self.master.after(2000, self.move_target)

    def move_player(self, event):
        x, y = event.x, event.y
        self.canvas.coords(self.player, x - self.player_size / 2,
                                          y - self.player_size / 2,
                                          x + self.player_size / 2,
                                          y + self.player_size / 2)

    def shoot(self, event):
        x, y = event.x, event.y
        overlap = self.canvas.find_overlapping(x, y, x, y)
        if self.target in overlap:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")

def main():
    root = tk.Tk()
    game = ShootingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
