from app.player import Player
from app.player_bnode import PlayerBNode

class PlayerBST:
    def __init__(self, root = None) -> None:
        self._root = root

    @property
    def root(self) -> None:
        return self._root

    @root.setter
    def root(self, root) -> None:
        self._root = root

    def insert(self, player: Player) -> PlayerBNode | None:
        if self.root is None:
            self.root = PlayerBNode(player)
            return self.root
        else:
            current = self.root
            if player.name < current.player.name:
                current.left_bnode = PlayerBST(current.left_bnode).insert(player)
            elif player.name > current.player.name:
                current.right_bnode = PlayerBST(current.right_bnode).insert(player)
            else:
                self.root.player = player
            return self.root

    def search(self, name: str) -> PlayerBNode | None:
        if self.root is None:
            return None
        elif self.root.player.name == name:
            return self.root
        elif name < self.root.player.name:
            return PlayerBST(self.root.left_bnode).search(name)
        else:
            return PlayerBST(self.root.right_bnode).search(name)
