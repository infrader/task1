import os
import sys
import time
import random
import json
import msvcrt # Если linux то закоминтировать! Библиотека только для windows

EMPTY = ' . '
TREE = ' 🌳'
FIRE = ' 🔥'
BURNED = ' x '
RIVER = ' ~ '
HELI = ' 🚁'
HOSPITAL = ' 🏥'
SHOP = ' 🛒'

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[EMPTY for _ in range(width)] for _ in range(height)]
        
        self.player = {'x': width // 2, 'y': height // 2, 'hp': 100, 'max_hp': 100, 
                       'score': 0, 'water': 1, 'max_water': 1, 'turns': 0}
        
        self.weather = 0
        
        self.generate_map()
        self.hospital_pos = None
        self.shop_pos = None
        self.place_buildings()
        self.place_player()

    def place_buildings(self):
        self.hospital_pos = (random.randint(0, self.width-1), random.randint(0, self.height-1))
        self.grid[self.hospital_pos[1]][self.hospital_pos[0]] = HOSPITAL
        
        self.shop_pos = (random.randint(0, self.width-1), random.randint(0, self.height-1))
        while self.shop_pos == self.hospital_pos:
            self.shop_pos = (random.randint(0, self.width-1), random.randint(0, self.height-1))
        self.grid[self.shop_pos[1]][self.shop_pos[0]] = SHOP

    def generate_map(self):
        if random.choice([True, False]):
            river_y = random.randint(2, self.height - 3)
            for x in range(self.width):
                self.grid[river_y][x] = RIVER
        else:
            river_x = random.randint(2, self.width - 3)
            for y in range(self.height):
                self.grid[y][river_x] = RIVER

        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == EMPTY and random.random() < 0.3: 
                    self.grid[y][x] = TREE

    def place_player(self):
        self.grid[self.player['y']][self.player['x']] = HELI

    def draw(self):
        os.system('clear') 
        print(f"🌦 Погода: {['Ясно', 'Дождь', 'Гроза'][self.weather]} | Ходов: {self.player['turns']}")
        print(f"💧 Вода: {self.player['water']}/{self.player['max_water']} | ❤️ HP: {self.player['hp']}/{self.player['max_hp']} | 🏆 Очки: {self.player['score']}")
        print("Управление: W/A/S/D - движение, Пробел - действие (тушить/пополнить/лечиться), Q - выход")
        print(" " + "-" * (self.width * 3))
        
        for y in range(self.height):
            row_str = "|"
            for x in range(self.width):
                if x == self.player['x'] and y == self.player['y']:
                    row_str += HELI + "|"
                else:
                    row_str += self.grid[y][x] + "|"
            print(row_str)
        print(" " + "-" * (self.width * 3))

    def move(self, dx, dy):
        new_x = self.player['x'] + dx
        new_y = self.player['y'] + dy
        
        # Проверка границ
        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            self.player['x'] = new_x
            self.player['y'] = new_y
            self.check_tile()

    def check_tile(self):
        x, y = self.player['x'], self.player['y']
        
        if self.grid[y][x] == RIVER:
            self.player['water'] = self.player['max_water']
            
    def action(self):
        x, y = self.player['x'], self.player['y']
        
        if self.grid[y][x] == RIVER:
            if self.player['water'] < self.player['max_water']:
                self.player['water'] = self.player['max_water']
                print("💧 Бак пополнен!")
                time.sleep(0.5)
            return

        if self.grid[y][x] == HOSPITAL:
            if self.player['score'] >= 10 and self.player['hp'] < self.player['max_hp']:
                self.player['score'] -= 10
                self.player['hp'] = min(self.player['max_hp'], self.player['hp'] + 20)
                print("❤️ Здоровье восстановлено за 10 очков!")
                time.sleep(0.5)
            return

        if self.grid[y][x] == SHOP:
            if self.player['score'] >= 15:
                self.player['score'] -= 15
                self.player['max_water'] += 1
                self.player['water'] = self.player['max_water']
                print(f"🛒 Улучшение куплено! Макс. вода: {self.player['max_water']} (потрачено 15 очков)")
                time.sleep(0.5)
            return

        for dy in range(-1, 2):
            for dx in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if self.grid[ny][nx] == FIRE:
                        if self.player['water'] > 0:
                            self.grid[ny][nx] = EMPTY
                            self.player['water'] -= 1
                            self.player['score'] += 5
                            print("🔥 Пожар потушен! +5 очков")
                            time.sleep(0.3)
                            return
                        else:
                            print("⚠️ Нет воды! Летите к реке (~) чтобы пополнить бак.")
                            time.sleep(0.5)
                            return

    def update_environment(self):
        self.player['turns'] += 1
        

        if self.player['turns'] % 5 == 0:
            self.weather = random.choice([0, 1, 2])

        new_grid = [row[:] for row in self.grid] 
        
        trees_count = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == TREE:
                    trees_count += 1

                    burn_chance = 0.05 if self.weather == 0 else (0.01 if self.weather == 1 else 0.15)
                    if random.random() < burn_chance:
                        new_grid[y][x] = FIRE
                        
                elif self.grid[y][x] == FIRE:
                    if random.random() < 0.2:
                        new_grid[y][x] = BURNED
                        self.player['score'] -= 2 
                    elif random.random() < 0.4:
                        for dy in range(-1, 2):
                            for dx in range(-1, 2):
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < self.width and 0 <= ny < self.height:
                                    if self.grid[ny][nx] == TREE:
                                        new_grid[ny][nx] = FIRE

        self.grid = new_grid
        
        if trees_count == 0 and self.player['score'] >= 0:
            self.end_game("Все деревья сгорели! Вы проиграли.")

    def save_game(self, filename="savegame.json"):
        data = {
            'width': self.width,
            'height': self.height,
            'grid': self.grid,
            'player': self.player,
            'weather': self.weather,
            'hospital_pos': self.hospital_pos,
            'shop_pos': self.shop_pos
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
        print("Игра сохранена!")

    def load_game(self, filename="savegame.json"):
        if not os.path.exists(filename):
            print("Файл сохранения не найден!")
            time.sleep(1)
            return False
            
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        self.width = data['width']
        self.height = data['height']
        self.grid = data['grid']
        self.player = data['player']
        self.weather = data['weather']
        self.hospital_pos = tuple(data['hospital_pos']) if data['hospital_pos'] else None
        self.shop_pos = tuple(data['shop_pos']) if data['shop_pos'] else None
        print("Игра загружена!")
        time.sleep(1)
        return True

    def end_game(self, message):
        self.draw()
        print(f"\n🏁 {message}")
        print(f"Итоговый счет: {self.player['score']}")
        sys.exit()

def get_key():
    if os.name == 'nt':
        return msvcrt.getch().decode('utf-8').lower()
    else:
        import termios
        import tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch.lower()

def main():
    print("Добро пожаловать в игру 'Вертолет-Пожарный'!")
    print("1. Новая игра")
    print("2. Загрузить игру")
    choice = input("Выберите действие (1/2): ")
    
    game = None
    
    if choice == '2':
        game = Game(10, 10)
        if not game.load_game():
            game = None 
            
    if game is None:
        try:
            w = int(input("Введите ширину поля (например, 10): "))
            h = int(input("Введите высоту поля (например, 10): "))
            if w < 5 or h < 5:
                print("Слишком маленькое поле! Ставим 10х10.")
                w, h = 10, 10
        except ValueError:
            print("Неверный ввод! Ставим 10х10.")
            w, h = 10, 10
            
        game = Game(w, h)

    while True:
        game.draw()
        key = get_key()
        
        if key == 'q':
            break
        elif key == 'w':
            game.move(0, -1)
        elif key == 's':
            game.move(0, 1)
        elif key == 'a':
            game.move(-1, 0)
        elif key == 'd':
            game.move(1, 0)
        elif key == ' ':
            game.action()
        elif key == '1': 
            game.save_game()
            continue 
            
        game.update_environment()

        if game.grid[game.player['y']][game.player['x']] == FIRE:
            game.player['hp'] -= 20
            if game.player['hp'] <= 0:
                game.end_game("Вертолет сгорел! Вы проиграли.")

if __name__ == "__main__":
    main()