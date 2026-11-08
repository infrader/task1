word = input("Введите слово: ").lower()

vowels = "aeiou"
vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
total_vowels = 0
total_consonants = 0

for char in word:
    if char in vowels:
        total_vowels += 1
        vowel_counts[char] += 1
    elif char.isalpha():
        total_consonants += 1

print(f"Количество гласных: {total_vowels}")
print(f"Количество согласных: {total_consonants}")

for v in vowels:
    print(f"{v}: {vowel_counts[v]}")

if 0 in vowel_counts.values():
    print(False)