class Point:
    def _init_(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0), {-})". format(self.x, self.y)

p1 = Point(2, 3)
print(p1)