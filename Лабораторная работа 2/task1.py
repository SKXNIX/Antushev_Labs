BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int) -> None:
        self.id_ = None
        self.name = None
        self.pages = None

        self._validate_id(id_)
        self._validate_name(name)
        self._validate_pages(pages)

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages})"

    def _validate_id(self, id_: int) -> None:
        if not isinstance(id_, int):
            raise TypeError("id_ должен быть типа int")
        if id_ < 0:
            raise ValueError("id_ должен быть положительным числом")
        self.id_ = id_

    def _validate_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("name должен быть типа str")
        if not name:
            raise ValueError("name должен быть не пустым")
        self.name = name

    def _validate_pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError("pages должен быть типа int")
        if pages < 0:
            raise ValueError("pages должен быть положительным числом")
        self.pages = pages


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
