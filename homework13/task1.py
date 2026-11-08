class CashDesk:
    def __init__(self, money=0):
        self.money = money
        
    def top_up(self, X):
        """Пополняет кассу на X"""
        self.money += X
        print(f"Касса пополнена на {X}. Теперь в кассе: {self.money}")
        
    def count_1000(self):
        """Выводит сколько целых тысяч осталось в кассе"""
        # Целочисленное деление // отбрасывает копейки/сотни и оставляет тысячи
        print(f"Целых тысяч в кассе: {self.money // 1000}")
        
    def take_away(self, X):
        """Забирает X из кассы, либо выкидывает ошибку"""
        if X > self.money:
            raise ValueError("Недостаточно денег в кассе!")
        self.money -= X
        print(f"Из кассы забрали {X}. Остаток: {self.money}")

cash = CashDesk(5500)
cash.count_1000() 
cash.top_up(300) 
cash.take_away(800) 