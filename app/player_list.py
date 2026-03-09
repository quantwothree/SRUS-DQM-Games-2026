from app.player_node import PlayerNode

class PlayerList:
    def __init__(self) -> None:
        self._head = None

    @property
    def is_empty(self) -> bool:
        if self._head is None:
            return True
        else:
            return False

    def insert_head(self, player_node: PlayerNode) -> None:
        if self.is_empty:
            self._head = player_node
        else:
            player_node.next = self._head
            self._head.previous = player_node
            self._head = player_node

    @property
    def head(self) -> PlayerNode:
        return self._head

