class Book:
    def __init__(self, title: str = "None", number_of_pages: int = 0, is_fictional: bool = None):
        self._title = title
        self._number_of_pages = number_of_pages
        self._is_fictional = is_fictional

    # ... keep your existing getters and setters ...

    # Title Getters and Setters
    def get_title(self) -> str:
        return self._title

    def set_title(self, title: str):
        self._title = title

    # Pages Getters and Setters
    def get_number_of_pages(self) -> int:
        return self._number_of_pages

    def set_number_of_pages(self, pages: int):
        # Good practice: only set if pages is positive
        if pages >= 0:
            self._number_of_pages = pages

    # Fictional Getters and Setters
    def get_is_fictional(self) -> bool:
        return self._is_fictional

    def set_is_fictional(self, is_fictional: bool):
        self._is_fictional = is_fictional