#Use * to unpack banknotes and .extend() to add them to the Wallet.
#* распаковывает банкноты, а .extend() добавляет их в Wallet.
class Banknote:
    def __init__(self, value: int):
        self.value = value
    def __str__(self):
        return f"Banknote's nominal is {self.value}"
    def __repr__(self):
        return f"Banknote({self.value})"

banknote_100 = Banknote(100)
banknote_500 = Banknote(500)
banknote_50 = Banknote(50)

class Wallet:
    def __init__(self, *banknotes:Banknote):
        self.container = []
        self.container.extend(banknotes)
    def __repr__(self):
        return f"Wallet({self.container})"

if __name__ == "__main__":
    my_wallet = Wallet(banknote_100, banknote_50)
    print(my_wallet)