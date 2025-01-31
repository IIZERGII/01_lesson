def is_year_leap(year: int) -> bool:
    return year % 4 == 0

year = int(input("Введите год: "))
print(f"Год {year}: {is_year_leap(year)}")