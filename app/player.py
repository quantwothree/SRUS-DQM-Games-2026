class Player:
    def __init__(self, unique_id : str, player_name : str) -> None:
        self._unique_id = unique_id
        self._player_name = player_name

    @property
    def uid(self):
        return self._unique_id

    @property
    def name(self):
        return self._player_name

    def __str__(self):
        return f"This player's unique ID is: {self._unique_id}, and the player's name is: {self._player_name}"



