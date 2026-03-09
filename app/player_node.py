from app.player import Player

class PlayerNode:
    def __init__(self, player: Player):
        self._player = player
        self._next = None
        self._previous = None

    @property
    def player(self):
        return self._player

    @property
    def next(self):
        return self._next

    @property
    def previous(self):
        return self._previous

    @property
    def key(self):
        return self._player.uid

    def __str__(self):
        return f"This node contains the player named: {self._player.name} with an ID of: {self.key}"

