from address import Address
from mailing import Mailing

to_addr = Address("620000", "г. Екатеринбург", "ул. Ленина", "55", "22")
from_addr = Address("620800", "г. Москва", "ул. Свердлова", "22", "45")
sending = Mailing(to_addr, from_addr, 1200, "1234567890")

print(
    "Отправление",
    sending.track,
    "из",
    from_addr,
    "в",
    to_addr,
    ". Стоимость",
    sending.cost,
    "рублей.",
)