class Player:
    def __init__(self, unique_id: str, player_name: str, score: int = 0) -> None:
        self._unique_id = unique_id
        self._player_name = player_name
        self._score = score

    @property
    def uid(self) -> str:
        return self._unique_id

    @property
    def name(self) -> str:
        return self._player_name

    def __str__(self) -> str:
        return f"This player's unique ID is: {self._unique_id}, and the player's name is: {self._player_name}"

    @classmethod
    def djb2(cls, key: str) -> int:
        hash_value = 5381
        for i in key:
            hash_value = ((hash_value << 5) + hash_value) + ord(i)
        return hash_value

    def __hash__(self) -> int:
        return self.djb2(self.uid)

    # Use to update Player's name in hashmap
    @name.setter
    def name(self, new_name: str) -> None:
        self._player_name = new_name

    # Changed from comparing uid to comparing score of Players
    def __eq__(self, other):
        return self.score == other.score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score: int):
        if new_score < 0:
            raise ValueError("Score needs to be greater than 0")
        else:
            self._score = new_score

    def __repr__(self):
        return f"{self.__class__.__name__} (name= '{self._player_name}', uid= '{self._id}', score= {self._score})"

    def __lt__(self, other):
        return self.score < other.score

    @classmethod
    def custom_sort(cls, array: list) -> list:
        if len(array) <= 1:
            return array
        # Choosing the pivot roughly in the middle of the list
        pivot_index = round(len(array) / 2)
        pivot = array[pivot_index]

        # New array with no pivot
        new_array = array[:pivot_index] + array[pivot_index + 1:]
        left = []
        right = []

        for player in new_array:
            if player > pivot:
                left.append(player)
            else:
                right.append(player)
        return cls.custom_sort(left) + [pivot] + cls.custom_sort(right)

