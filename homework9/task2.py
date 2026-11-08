import collections

pets = {}

def get_suffix(age):
    """Функция для получения правильного склонения слова 'год'"""
    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif age % 10 in (2, 3, 4):
        return "года"
    else:
        return "лет"

def get_pet(ID):
    """Получает информацию о питомце по ID. Если нет - возвращает False"""
    return pets[ID] if ID in pets.keys() else False

def pets_list():
    """Выводит список всех питомцев"""
    if not pets:
        print("База данных пуста.")
        return
        
    for pet_id in pets:
        pet_data = get_pet(pet_id)
        pet_name = list(pet_data.keys())[0]
        info = pet_data[pet_name]
        
        suffix = get_suffix(info["Возраст питомца"])
        print(f'ID: {pet_id}. Это {info["Вид питомца"]} по кличке "{pet_name}". Возраст: {info["Возраст питомца"]} {suffix}. Имя владельца: {info["Имя владельца"]}')

def create():
    """Добавляет новую запись"""
    if not pets:
        next_id = 1
    else:
        last_id = collections.deque(pets, maxlen=1)[0]
        next_id = last_id + 1
        
    name = input("Введите кличку питомца: ")
    species = input("Введите вид питомца: ")
    age = int(input("Введите возраст: "))
    owner = input("Введите имя владельца: ")
    pets[next_id] = {
        name: {
            "Вид питомца": species,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f"Питомец успешно добавлен под ID: {next_id}")

def read():
    """Выводит информацию о конкретном питомце"""
    try:
        pet_id = int(input("Введите ID питомца: "))
        pet_data = get_pet(pet_id)
        
        if not pet_data:
            print("Питомец с таким ID не найден.")
            return
            
        pet_name = list(pet_data.keys())[0]
        info = pet_data[pet_name]
        suffix = get_suffix(info["Возраст питомца"])
        
        print(f'Это {info["Вид питомца"]} по кличке "{pet_name}". Возраст: {info["Возраст питомца"]} {suffix}. Имя владельца: {info["Имя владельца"]}')
    except ValueError:
        print("Ошибка: ID должен быть целым числом.")

def update():
    """Обновляет информацию о питомце (полностью перезаписывает)"""
    try:
        pet_id = int(input("Введите ID питомца для обновления: "))
        
        if not get_pet(pet_id):
            print("Питомец с таким ID не найден.")
            return
            
        print("Введите новые данные (старые будут стерты):")
        name = input("Новая кличка: ")
        species = input("Новый вид: ")
        age = int(input("Новый возраст: "))
        owner = input("Новое имя владельца: ")
        
        pets[pet_id] = {
            name: {
                "Вид питомца": species,
                "Возраст питомца": age,
                "Имя владельца": owner
            }
        }
        print("Информация обновлена.")
    except ValueError:
        print("Ошибка: ID и возраст должны быть числами.")

def delete():
    """Удаляет запись по ID"""
    try:
        pet_id = int(input("Введите ID питомца для удаления: "))
        
        if get_pet(pet_id):
            del pets[pet_id]
            print(f"Питомец с ID {pet_id} удален.")
        else:
            print("Питомец с таким ID не найден.")
    except ValueError:
        print("Ошибка: ID должен быть целым числом.")

# --- Главный цикл программы ---
command = ""
print("Добро пожаловать в базу данных ветеринарной клиники!")
print("Доступные команды: create, read, update, delete, list, stop")

while command != "stop":
    command = input("\nВведите команду: ").strip().lower()
    
    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    elif command == "stop":
        print("Завершение работы программы. До свидания!")
    else:
        print("Неизвестная команда. Попробуйте еще раз.")