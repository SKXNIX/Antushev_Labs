class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self) -> str:
        return self.name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("name должно быть типа str")
        self.name = name

    @property
    def author(self) -> str:
        return self.author

    @author.setter
    def author(self, author: str) -> None:
        if not isinstance(author, str):
            raise TypeError("author должно быть типа str")
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self.pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError("pages должно быть типа int")
        if pages < 0:
            raise ValueError("pages должно быть целым положительным числом")
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> int:
        return self.duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError("duration должно быть типа float")
        if duration < 0:
            raise ValueError("duration должно быть положительным числом")
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
