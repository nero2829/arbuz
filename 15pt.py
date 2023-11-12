import math
class Oct:
    def __init__(self, dovz):
        self.dovz= dovz
    def ops(self):
        return round(self.dovz/(2*math.sin(math.pi/8)),2)
    def vps(self):
        return round(self.dovz/(2*math.tan(math.pi/8)),2)
x=float(input("Введіть довжину сторони 8 кутника:"))
octagon=Oct(x)
print(f"Радіус описаного кола:{octagon.ops()}")
print(f"Радіус вписаного кола:{octagon.vps()}")
