from address import Address

class Mailing:
    def __init__(self, to_addr, from_addr, weight, tracking_number):
        self.to_addr = to_addr
        self.from_addr = from_addr
        self.weight = weight
        self.tracking_number = tracking_number

    def __str__(self):
        return f"To address: {self.to_addr.postal_code}, {self.to_addr.city}, {self.to_addr.street}, {self.to_addr.house}, {self.to_addr.apartment}\nFrom address: {self.from_addr.postal_code}, {self.from_addr.city}, {self.from_addr.street}, {self.from_addr.house}, {self.from_addr.apartment}\nWeight: {self.weight}\nTracking number: {self.tracking_number}"

to_addr = Address("620000", "?. ????????????", "??. ??????", "55", "22")
from_addr = Address("620800", "?. ??????", "??. ?????????", "22", "45")
sending = Mailing(to_addr, from_addr, 1200, "1234567890")

print(sending)