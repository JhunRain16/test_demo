import tkinter as tk
import random

class ShootingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Shooting Game")
        self.master.geometry("400x400")

        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="white")
        self.canvas.pack()

        self.target_radius = 20
        self.target_x = 0
        self.target_y = random.randint(self.target_radius, 400 - self.target_radius)
        self.target = self.canvas.create_oval(self.target_x - self.target_radius, 
                                              self.target_y - self.target_radius,
                                              self.target_x + self.target_radius, 
                                              self.target_y + self.target_radius,
                                              fill="red")

        self.score = 0
        self.score_label = tk.Label(self.master, text="Score: 0")
        self.score_label.pack()

        self.canvas.bind("<Button-1>", self.shoot)

        self.move_target()

    def move_target(self):
        self.target_x += 5
        if self.target_x > 400 + self.target_radius:
            self.target_x = 0
            self.target_y = random.randint(self.target_radius, 400 - self.target_radius)
        self.canvas.coords(self.target, self.target_x - self.target_radius, 
                                          self.target_y - self.target_radius,
                                          self.target_x + self.target_radius, 
                                          self.target_y + self.target_radius)
        self.master.after(50, self.move_target)

    def shoot(self, event):
        x, y = event.x, event.y
        distance = ((x - self.target_x) ** 2 + (y - self.target_y) ** 2) ** 0.5
        if distance <= self.target_radius:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")

def main():
    root = tk.Tk()
    game = ShootingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
