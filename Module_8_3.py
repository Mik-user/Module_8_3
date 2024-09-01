class Car:
    def __init__(self,model,_vin,_numbers):
        self.model = model
        valid_vin = self._is_valid_vin(_vin)
        if valid_vin == True:
            self._vin = _vin
        valid_numbers = self._is_valid_numbers(_numbers)
        if valid_numbers == True:
            self._numbers = _numbers

    def _is_valid_vin(self,vin_number):
        if isinstance(vin_number,int) == False:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number >=1000000 and vin_number <=9999999:
            self._is_valid_vin = True
        else:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

    def _is_valid_numbers(self,number):
        if isinstance(number,str):
            if len(number) == 6:
                self._is_valid_numbers = True
            else:
                raise IncorrectCarNumbers('Неверная длина номера')
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')

class IncorrectVinNumber(Exception):
    def __init__(self,message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self,message):
        self.message = message





try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')