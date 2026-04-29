#__repr__ and __str__
class Banknote:
    def __init__(self, value: int):
        self.value = value
    
    def __repr__(self):
        return f"Banknote({self.value})"
    
    def __str__(self):
        return f"Банкнотом номиналом в ${self.value}"

if __name__ == "__main__":
    banknote = Banknote(100)
    print(banknote )