class Phone:
    def __init__(self, color, size):
        self.color = color
        self.size = size


android = Phone("blue", 4.7)
print(android.color)

ios = Phone("black", 5)

print(ios.size)
