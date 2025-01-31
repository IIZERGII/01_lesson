def month_to_season(month: int) -> str:
    seasons = {
        1: "Зима", 2: "Зима", 12: "Зима",
        3: "Весна", 4: "Весна", 5: "Весна",
        6: "Лето", 7: "Лето", 8: "Лето",
        9: "Осень", 10: "Осень", 11: "Осень"
    }
    return seasons.get(month, "Некорректный месяц")

month = int(input("Введите номер месяца: "))
print(f"Сезон: {month_to_season(month)}")