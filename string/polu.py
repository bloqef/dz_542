word = input("Введи слово: ")
word = word.lower().strip()
reversed_word = word[::-1]

if word == reversed_word:
    print(f"Это палиндром!{reversed_word}")
else:
    print(f"Не палиндром.{reversed_word}")
    