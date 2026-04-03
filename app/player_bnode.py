from app.player import Player

class PlayerBNode:
    def __init__(self, player: Player) -> None:
        self._player = player
        self._left_bnode = None
        self._right_bnode = None

    @property
    def player(self) -> Player:
        return self._player

    @player.setter
    def player(self, player: Player) -> None:
        self._player = player

    @property
    def left_bnode(self):
        return self._left_bnode

    @left_bnode.setter
    def left_bnode(self, bnode) -> None:
        self._left_bnode = bnode

    @property
    def right_bnode(self):
        return self._right_bnode

    @right_bnode.setter
    def right_bnode(self, bnode) -> None:
        self._right_bnode = bnode
