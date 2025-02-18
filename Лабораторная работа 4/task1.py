class Spaceship:
    """Базовый класс для представления космического корабля.

    
    :param name (str): Название корабля.
    :param max_speed (float): Максимальная скорость в км/с.
    :param fuel_type (str): Тип топлива.
    :param is_active (bool): Статус активности корабля (работает/не работает).

    Пример:
    >>> spaceship = Spaceship("Звездолёт-1", 10.5, "антиматерия")
    >>> spaceship.launch()
    """

    def __init__(self, name: str, max_speed: float, fuel_type: str, is_active: bool = True) -> None:
        """Инициализация экземпляра Spaceship.

        
        :param name: Название корабля
        :param max_speed: Максимальная скорость
        :param fuel_type: Тип топлива
        :param is_active: Статус активности корабля
        """
        self.name = name
        self.max_speed = max_speed
        self.fuel_type = fuel_type
        self.is_active = is_active

    def __str__(self) -> str:
        """Возвращает строковое представление корабля."""
        status = "активен" if self.is_active else "неактивен"
        return f"{self.name} (скорость: {self.max_speed} км/с, топливо: {self.fuel_type}, статус: {status})"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление корабля."""
        return f"Spaceship(name={self.name!r}, max_speed={self.max_speed}, fuel_type={self.fuel_type!r}, " \
               f"is_active={self.is_active})"

    def launch(self) -> str:
        """Запускает корабль.


        :returns Сообщение о запуске.
        """
        if self.is_active:
            return f"{self.name} запущен и движется со скоростью {self.max_speed} км/с!"
        return f"{self.name} не может быть запущен, так как он неактивен."

    def refuel(self, fuel_amount: float) -> str:
        """Заправляет корабль.


        :param fuel_amount: Количество топлива для заправки.

        :returns Сообщение о заправке.
        """
        return f"{self.name} заправлен на {fuel_amount} литров {self.fuel_type}."


class CargoSpaceship(Spaceship):
    """Класс, представляющий грузовой космический корабль. Наследуется от Spaceship.

    
    :param cargo_capacity (float): Вместимость груза в тоннах.
    :param current_cargo (float): Текущий груз в тоннах.

    Пример:
    >>> cargo_ship = CargoSpaceship("Грузовик-7", 8.2, "водород", 100.0)
    >>> cargo_ship.load_cargo(50)
    """

    def __init__(self, name: str, max_speed: float, fuel_type: str,
                 cargo_capacity: float, current_cargo: float = 0.0) -> None:
        """Расширение конструктора Spaceship, добавление параметров груза.

        
        :param cargo_capacity: Вместимость груза.
        :param current_cargo: Текущий груз.
        """
        super().__init__(name, max_speed, fuel_type)
        self.cargo_capacity = cargo_capacity
        self.current_cargo = current_cargo

    def __str__(self) -> str:
        """Перегрузка метода __str__ с учётом параметров груза."""
        return f"{super().__str__()}, груз: {self.current_cargo}/{self.cargo_capacity} тонн"

    def __repr__(self) -> str:
        """Перегрузка метода __repr__ с учётом параметров груза."""
        return f"CargoSpaceship(name={self.name!r}, max_speed={self.max_speed}, fuel_type={self.fuel_type!r}, " \
               f"cargo_capacity={self.cargo_capacity}, current_cargo={self.current_cargo})"

    def load_cargo(self, cargo_weight: float) -> str:
        """Загружает груз на корабль.

        
        :param cargo_weight: Вес груза для загрузки.

        :returns Сообщение о загрузке или ошибке, если груз превышает вместимость.
        """
        if self.current_cargo + cargo_weight <= self.cargo_capacity:
            self.current_cargo += cargo_weight
            return f"Груз {cargo_weight} тонн загружен на {self.name}."
        return f"Ошибка: груз превышает вместимость {self.name}."

    def unload_cargo(self) -> str:
        """Разгружает весь груз с корабля.


        :returns Сообщение о разгрузке.
        """
        unloaded_cargo = self.current_cargo
        self.current_cargo = 0.0
        return f"Груз {unloaded_cargo} тонн разгружен с {self.name}."


class PassengerSpaceship(Spaceship):
    """Класс, представляющий пассажирский космический корабль. Наследуется от Spaceship.

    
    :param passenger_capacity (int): Вместимость пассажиров.
    :param current_passengers (int): Текущее количество пассажиров.

    Пример:
    >>> passenger_ship = PassengerSpaceship("Пассажир-3", 12.0, "плазма", 50)
    >>> passenger_ship.board_passengers(30)
    """

    def __init__(self, name: str, max_speed: float, fuel_type: str,
                 passenger_capacity: int, current_passengers: int = 0) -> None:
        """Расширение конструктора Spaceship, добавление параметров пассажиров.

        
        :param passenger_capacity: Вместимость пассажиров.
        :param current_passengers: Текущее количество пассажиров.
        """
        super().__init__(name, max_speed, fuel_type)
        self.passenger_capacity = passenger_capacity
        self.current_passengers = current_passengers

    def __str__(self) -> str:
        """Перегрузка метода __str__ с учётом параметров пассажиров."""
        return f"{super().__str__()}, пассажиры: {self.current_passengers}/{self.passenger_capacity}"

    def __repr__(self) -> str:
        """Перегрузка метода __repr__ с учётом параметров пассажиров."""
        return f"PassengerSpaceship(name={self.name!r}, max_speed={self.max_speed}, fuel_type={self.fuel_type!r}, " \
               f"passenger_capacity={self.passenger_capacity}, current_passengers={self.current_passengers})"

    def board_passengers(self, passengers: int) -> str:
        """Посадка пассажиров на корабль.

        
        :param passengers: Количество пассажиров для посадки.

        :returns Сообщение о посадке или ошибке, если превышена вместимость.
        """
        if self.current_passengers + passengers <= self.passenger_capacity:
            self.current_passengers += passengers
            return f"{passengers} пассажиров сели на борт {self.name}."
        return f"Ошибка: превышена вместимость {self.name}."

    def disembark_passengers(self) -> str:
        """Высадка всех пассажиров с корабля.


        :returns Сообщение о высадке.
        """
        disembarked_passengers = self.current_passengers
        self.current_passengers = 0
        return f"{disembarked_passengers} пассажиров высажены с {self.name}."


if __name__ == "__main__":
    pass
