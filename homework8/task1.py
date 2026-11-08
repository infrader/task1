pets = {}

pet_name = input("Введите кличку питомца: ")
species = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: ")) 
owner = input("Введите имя владельца: ")

# Заполняем словарь
pets[pet_name] = {
    "Вид питомца": species,
    "Возраст питомца": age,
    "Имя владельца": owner
}

def get_age_word(age):
    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif age % 10 in (2, 3, 4):
        return "года"
    else:
        return "лет"

pet_names = list(pets.keys())
pet_info = list(pets.values())[0] 

name = pet_names[0]
age_word = get_age_word(pet_info["Возраст питомца"])

print(f'Это {pet_info["Вид питомца"]} по кличке "{name}". Возраст: {pet_info["Возраст питомца"]} {age_word}. Имя владельца: {pet_info["Имя владельца"]}')