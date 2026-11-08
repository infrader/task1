import math

class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s
        
    def go_up(self):
        self.y += self.s
        
    def go_down(self):
        self.y -= self.s
        
    def go_left(self):
        self.x -= self.s
        
    def go_right(self):
        self.x += self.s
        
    def evolve(self):
        """Увеличивает шаг на 1"""
        self.s += 1
        
    def degrade(self):
        """Уменьшает шаг на 1, либо выкидывает ошибку"""
        self.s -= 1
        if self.s <= 0:
            raise ValueError("Размер шага не может быть меньше или равен 0!")
            
    def count_moves(self, x2, y2):
        """Возвращает минимальное количество действий до точки x2, y2"""
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        
        moves_x = math.ceil(dx / self.s)
        moves_y = math.ceil(dy / self.s)
        
        return moves_x + moves_y


turtle = Turtle(x=0, y=0, s=1)
turtle.go_right()
turtle.go_up()
turtle.evolve() 

print(turtle.count_moves(5, 5))