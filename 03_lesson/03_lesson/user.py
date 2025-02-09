class User:

    def __init__(self, first_name, last_name):
        self.first_n = first_name
        self.last_n = last_name

    def print_first_name(self):
        print(self.first_n)

    def print_last_name(self):
        print(self.last_n)

    def print_last_and_first_name(self):
        print(self.first_n, self.last_n)