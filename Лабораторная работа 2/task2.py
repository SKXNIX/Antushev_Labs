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


# TODO написать класс Library
class Library:
    def __init__(self, books: list = []) -> None:
        self.books = books
        if books:
            self.enum = None
            self.books_id_list = []
            self._create_enum()

    def _create_enum(self) -> None:
        for book in self.books:
            self.books_id_list.append(book.id_)
        self.enum = list(enumerate(self.books_id_list))

    def get_next_book_id(self) -> int:
        if not self.books:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_: int) -> int:
        if not self.books:
            raise ValueError("Книг нет")
        if id_ in self.books_id_list:
            for index, book_id in self.enum:
                if book_id == id_:
                    return index
        else:
            raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
