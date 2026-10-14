health = 100

while health > 0:
    print("Текущее здоровье:", health)
    print("1 — Атаковать")
    print("2 — Отдохнуть")
    print("3 — Найти выход")

    choice = input("Выбери действие: ")

    if choice == "1":
        health -= 25
        print("Ты атаковал! Здоровье уменьшилось на 25.")

    elif choice == "2":
        health += 15
        print("Ты отдохнул! Здоровье увеличилось на 15.")

    elif choice == "3":
        print("Ты нашёл выход! Победа!")
        break

    else:
        print("Неверный выбор!")

    if health <= 0:
        print("Игра окончена")
        break

    