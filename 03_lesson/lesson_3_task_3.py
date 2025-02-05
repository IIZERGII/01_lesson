from address import Address
from mailing import Mailing

to_address = Address
from_address = Address
to_address = 620000, "г. Екатеринбург", "ул. Ленина", 55, 22
from_address = 620800, "г. Москва", "ул. Свердлова", 22, 45

sending = Mailing
sending(to_address, from_address, 1200, 1234567890)

print(
    "Отправление",
    sending.track,
    "из",
    from_address,
    "в",
    to_address,
    ". Стоимость",
    sending.cost,
    "рублей.",
)