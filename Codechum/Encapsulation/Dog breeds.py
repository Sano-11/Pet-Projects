class Dog:
    def __init__(self, breed: str):
        # Initializing private-style properties
        self._breed = breed
        self._bark_count = 0

    # Getter and Setter for breed
    def get_breed(self) -> str:
        return self._breed

    def set_breed(self, breed: str) -> None:
        self._breed = breed

    # Getter for bark_count
    def get_bark_count(self) -> int:
        return self._bark_count

    def has_barked_a_lot(self) -> bool:
        # Returns True if bark_count is 100 or more
        return self._bark_count >= 100

    def bark(self, n: int) -> None:
        # Prints "Woof" n times and updates the counter
        for _ in range(n):
            print("Woof")
        
        self._bark_count += n