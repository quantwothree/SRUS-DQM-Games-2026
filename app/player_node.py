from app.player import Player

class PlayerNode:
    def __init__(self, player: Player) -> None:
        self._player = player
        self._next = None
        self._previous = None

    @property
    def player(self) -> Player:
        return self._player

    @property
    def next(self) -> PlayerNode:
        return self._next

    @next.setter
    def next(self, player_node: PlayerNode) -> None:
        self._next = player_node

    @property
    def previous(self) -> PlayerNode:
        return self._previous

    @previous.setter
    def previous(self, player_node: PlayerNode) -> None:
        self._previous = player_node

    @property
    def key(self) -> str:
        return self._player.uid

    def __str__(self) -> str:
        return f"This node contains the player named: {self._player.name} with an ID of: {self.key}"

