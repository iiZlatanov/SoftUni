class Weapon:
    def __init__(self, initial_bullets: int):
        self.bullets = initial_bullets

    def shoot(self):
        if self.bullets:
            self.bullets -= 1
            return "shooting..."
        return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"
