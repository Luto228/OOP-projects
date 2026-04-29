#__eq__	==	Equal (Равно)q
#__ne__	!=	Not Equal (Не равно)
#__lt__	<	Less Than (Меньше)
#__gt__	>	Greater Than (Больше)
#__le__	<=	Less or Equal (Меньше или равно)
#__ge__	>= Greater or Equal (Больше или равно)
class Cars:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        if other is None or not isinstance(other, Cars):
            return False
        return self.name == other.name

if __name__ == "__main__":
    car1 = Cars("BMW")
    car2 = Cars("BMW")
    print(car1 == car2)