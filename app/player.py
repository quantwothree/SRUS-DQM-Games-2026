class Player:
    def __init__(self, unique_id: str, player_name: str) -> None:
        self._unique_id = unique_id
        self._player_name = player_name

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