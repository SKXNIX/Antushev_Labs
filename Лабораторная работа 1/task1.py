# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union


class StorageCell:
    def __init__(self, id_cell: int, stored_item: str, count_item: int):
        """
        Создание и подготовка к работе объекта "Ячейка"

        :param id_cell: ID ячейки
        :param stored_item: Имя хранимого предмета
        :param count_item: Количество хранимого предмета

        Примеры:
        >>> cell = StorageCell(214, "brain", 1)  # инициализация экземпляра класса
        """

        self.id_cell = None
        self._validate_id_cell(id_cell)

        self.stored_item = None
        self._validate_stored_item(stored_item)

        self.count_item = None
        self._validate_count_item(count_item)

    def _validate_id_cell(self,id_cell: int):
        if not isinstance(id_cell, int):
            raise TypeError("ID ячейки должен быть типа int")
        self.id_cell = id_cell

    def _validate_stored_item(self,stored_item: str):
        if not isinstance(stored_item, str):
            raise TypeError("Имя хранимого предмета должно быть типа str")
        self.stored_item = stored_item

    def _validate_count_item(self,count_item: int):
        if not isinstance(count_item, int):
            raise TypeError("Количество хранимого предмета должно быть типа int")
        if count_item <= 0:
            raise ValueError("Количество хранимого предмета должно быть положительным числом")
        self.count_item = count_item

    def is_empty_cell(self) -> bool:
        """
        Функция которая проверяет является ли ячейка пустой
        :return: Является ли ячейка пустой

        Примеры:
        >>> cell = StorageCell(214, "brain", 1)
        >>> cell.is_empty_cell()
        """
        ...

    def add_item_to_cell(self, stored_item: str, count_item: int) -> None:
        """
        Добавление предмета в ячейку
        :param stored_item: Имя хранимого предмета
        :param count_item: Количество хранимого предмета

        >>> cell = StorageCell(214,"brain",1)
        >>> cell.add_item_to_cell("brain",1)
        """

        if not isinstance(stored_item, str):
            raise TypeError("Добавляемый предмет должен быть типа str")
        if not isinstance(count_item, int):
            raise TypeError("Количество добавляемого предмета должно быть типа int")
        if count_item <= 0:
            raise ValueError("Количество добавляемого предмета должно быть больше нуля")
        ...

    def remove_item_from_cell(self, stored_item: str, count_item: int) -> None:
        """
        Удаление предмета из ячейки
        :param stored_item: Имя удаляемого предмета
        :param count_item: Количество удаляемого предмета

        :raise ValueError: Если количество удаляемого предмета меньше или равно нулю, то вызываем ошибку

        >>> cell = StorageCell(214,"brain",2)
        >>> cell.remove_item_from_cell("brain",1)
        """

        if not isinstance(stored_item, str):
            raise TypeError("Удаляемый предмет должен быть типа str")
        if not isinstance(count_item, int):
            raise TypeError("Количество удаляемого предмета должно быть типа int")
        if count_item <= 0:
            raise ValueError("Количество удаляемого предмета должно быть больше нуля")
        ...


class Battery:
    def __init__(self, size: str, capacity: Union[int, float], charge: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Аккумулятор"
        :param size: Типоразмер аккумулятора
        :param capacity: Емкость аккумулятора
        :param charge: Заряд аккумулятора

        Пример:
        >>> battery = Battery("AA", 20, 0)
        """

        self.size = None
        self._validate_size(size)

        self.capacity = None
        self._validate_capacity(capacity)

        self.charge = None
        self._validate_charge(charge)

    def _validate_size(self, size: str) -> None:
        """
        Валидация типоразмера аккумулятора
        :param size: Типоразмер аккумулятора
        """
        if not isinstance(size, str):
            raise TypeError("Размер должен быть типа str")
        if not size in ("AA", "AAA"):
            raise ValueError('Размер должен быть "AA" или "AAA"')
        self.size = size

    def _validate_capacity(self, capacity: Union[int, float]) -> None:
        """
        Валидация емкости аккумулятора
        :param capacity: Емкость аккумулятора
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError("Емкость должна быть тип int или float")
        if capacity <= 0:
            raise ValueError("Емкость должна быть больше нуля")
        self.capacity = capacity

    def _validate_charge(self, charge: Union[int, float]) -> None:
        """
        Валидация заряда аккумулятора
        :param charge: Заряд аккумулятора
        """
        if not isinstance(charge, (int, float)):
            raise TypeError("Заряд должен быть тип int или float")
        if charge > self.capacity:
            raise ValueError("Заряд должен быть меньше емкости")
        self.charge = charge

    def is_empty_battery(self) -> bool:
        """
        Функция, которая проверяет, разряжен ли аккумулятор
        :return: Разряжен ли аккумулятор

        Пример:
        >>> battery = Battery("AAA", 200, 100)
        >>> battery.is_empty_battery()
        """
        if self.charge == 0:
            return True

    def show_info(self) -> None:
        """
        Функция, которая выводит информацию об аккумуляторе
        :print: Информация об аккумуляторе

        Пример:
        >>> battery = Battery("AAA", 200, 100)
        >>> battery.show_info()
        Данный аккумулятор типоразмера AAA имеет:
        Емкость: 200,
        Заряд: 100.
        """
        print("Данный аккумулятор типоразмера {} имеет:\nЕмкость: {},\nЗаряд: {}.".format(self.size, self.capacity,
                                                                                          self.charge))

    def charge_battery(self, charge: Union[int, float]) -> None:
        """
        Зарядка аккумулятора
        :param charge: Величина заряда

        Пример:
        >>> battery = Battery("AAA", 200, 100)
        >>> battery.charge_battery(50)
        """
        if not isinstance(charge, (int, float)):
            raise TypeError("Величина заряда должна быть тип int или float")
        if charge < 0:
            raise ValueError("Величина заряда должна быть положительным числом")

        if self.charge + charge <= self.capacity:
            self.charge += charge
        else:
            self.charge = self.capacity

    def discharge_battery(self, charge: Union[int, float]) -> None:
        """
        Разрядка аккумулятора
        :param charge: Величина заряда

        Пример:
        >>> battery = Battery("AAA", 200, 100)
        >>> battery.discharge_battery(50)
        """
        if not isinstance(charge, (int, float)):
            raise TypeError("Величина заряда должна быть тип int или float")
        if charge < 0:
            raise ValueError("Величина заряда должна быть положительным числом")

        if self.charge - charge >= self.capacity:
            self.charge += charge
        else:
            self.charge = 0


class Weather:
    def __init__(self, temperature: float, humidity: int, wind_speed: float):
        """
        Создание и подготовка к работе объекта "Погода"
        :param temperature: Температура воздуха
        :param humidity: Влажность воздуха
        :param wind_speed: Скорость ветра

        Пример:
        >>> weather = Weather(-4.0,79,4.0)
        """

        self.temperature = None
        self._validate_temperature(temperature)

        self.humidity = None
        self._validate_humidity(humidity)

        self.wind_speed = None
        self._validate_wind_speed(wind_speed)

    def _validate_temperature(self, temperature: float) -> None:
        if not isinstance(temperature, float):
            raise TypeError("Температура воздуха должна быть типа float")
        if not -100 < temperature < 100:
            raise ValueError("Температура воздуха должна быть в интервале от -100 до 100")
        self.temperature = temperature

    def _validate_humidity(self, humidity: int):
        if not isinstance(humidity, int):
            raise TypeError("Влажность воздуха должна быть типа int")
        if not 0 <= humidity <= 100:
            raise ValueError("Влажность воздуха должна быть в пределах от 0 до 100")
        self.humidity = humidity

    def _validate_wind_speed(self, wind_speed: float):
        if not isinstance(wind_speed, float):
            raise TypeError("Скорость ветра должна быть типа float")
        if not 0 <= wind_speed <= 100:
            raise ValueError("Скорость ветра должна быть в пределах от 0 до 100")
        self.wind_speed = wind_speed

    def change_temperature(self, temperature: float):
        """
        Изменение температуры воздуха
        :param temperature: Разница температуры воздуха

        Пример:
        >>> weather = Weather(-4.0,79,4.0)
        >>> weather.change_temperature(-2.1)
        """
        if not isinstance(temperature, float):
            raise TypeError("Температура должна быть типа float")
        if not -100 < self.temperature + temperature < 100:
            raise ValueError("Температура должна быть в интервале от -100 до 100")
        self.temperature += temperature

    def change_humidity(self, humidity: int):
        """
        Изменение влажности воздуха
        :param humidity: Разница влажности воздуха

        Пример:
        >>> weather = Weather(-4.0,79,4.0)
        >>> weather.change_humidity(7)
        """
        if not isinstance(humidity, int):
            raise TypeError("Влажность должна быть типа int")
        if not 0 <= self.humidity + humidity <= 100:
            raise ValueError("Влажность должна быть в пределах от 0 до 100")
        self.humidity += humidity

    def change_wind_speed(self, wind_speed: float):
        """
        Изменение скорости ветра
        :param wind_speed: Разница скорости ветра

        Пример:
        >>> weather = Weather(-4.0,79,4.0)
        >>> weather.change_wind_speed(-3.5)
        """
        if not isinstance(wind_speed, float):
            raise TypeError("Скорость ветра должна быть типа float")
        if not 0 <= self.wind_speed + wind_speed <= 100:
            raise ValueError("Скорость ветра должна быть в пределах от 0 до 100")
        self.wind_speed += wind_speed


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
