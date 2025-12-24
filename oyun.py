import tkinter as tk
import random

PENCERE_SAYISI = 150
HIZ = 100          # büyüt = daha hızlı
GUNCELLEME = 200  # ms

root = tk.Tk()
root.withdraw()

EKRAN_W = root.winfo_screenwidth()
EKRAN_H = root.winfo_screenheight()

pencereler = []

class TestPencere:
    def __init__(self):
        self.win = tk.Toplevel()
        self.win.title("Test")
        self.w = 200
        self.h = 100

        self.x = random.randint(0, EKRAN_W - self.w)
        self.y = random.randint(0, EKRAN_H - self.h)

        self.dx = random.choice([-HIZ, HIZ])
        self.dy = random.choice([-HIZ, HIZ])

        self.win.geometry(f"{self.w}x{self.h}+{self.x}+{self.y}")

        label = tk.Label(
            self.win,
            text="Hehe Naber?",
            fg="lime",
            font=("Arial", 16, "bold")
        )
        label.pack(expand=True)

    def hareket_et(self):
        self.x += self.dx
        self.y += self.dy

        # Kenarlardan sekme
        if self.x <= 0 or self.x >= EKRAN_W - self.w:
            self.dx *= -1
        if self.y <= 0 or self.y >= EKRAN_H - self.h:
            self.dy *= -1

        self.win.geometry(f"+{self.x}+{self.y}")

for _ in range(PENCERE_SAYISI):
    pencereler.append(TestPencere())

def guncelle():
    for p in pencereler:
        p.hareket_et()
    root.after(GUNCELLEME, guncelle)

guncelle()
root.mainloop()
