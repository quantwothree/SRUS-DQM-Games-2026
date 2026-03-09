from app.player_node import PlayerNode

class PlayerList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None

    @property
    def is_empty(self) -> bool:
        if self._head is None:
            return True
        else:
            return False

    def insert_head(self, player_node: PlayerNode) -> None:
        if self.is_empty:
            self._head = player_node
            self._tail = player_node
        else:
            player_node.next = self._head
            self._head.previous = player_node
            self._head = player_node

    @property
    def head(self) -> PlayerNode:
        return self._head

    @property
    def tail(self) -> PlayerNode:
        return self._tail

    def insert_tail(self, player_node: PlayerNode) -> None:
        if self.is_empty:
            self._head = player_node
            self._tail = player_node
        else:
            self._tail.next = player_node
            player_node.previous = self._tail
            self._tail = player_node

    def delete_at_head(self) -> None:
        if self.is_empty:
            raise IndexError("List is empty, nothing to delete")
        # If list only has 1 node
        elif self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self.head.next
            self.head.previous = None

    def delete_at_tail(self) -> None:
        if self.is_empty:
            raise IndexError("List is empty, nothing to delete")
        # If list only has 1 node
        elif self.head == self.tail:
            self._head = None
            self._tail = None
        else:
            self._tail = self.tail.previous
            self.tail.next = None

    def delete_at_key(self, key_to_delete) -> None:
        if self.is_empty:
            raise IndexError("List is empty, nothing to delete")
        # If list has 1 node
        elif self.head == self.tail:
            # And key to delete is head/tail
            if self.head.key == key_to_delete:
                self.delete_at_head()
                return
            # The key to delete is not head /tail
            else:
                raise IndexError("Key does not exist in list")
        else:
            # Loop to find they node with that key
            if self.head.key == key_to_delete:
                self.delete_at_head()
                return
            if self.tail.key == key_to_delete:
                self.delete_at_tail()
                return
            else:
                current_node = self.head.next
                while current_node:
                    if current_node.key == key_to_delete:
                        current_node.previous.next = current_node.next
                        current_node.next.previous = current_node.previous
                        return
                    else:
                        current_node = current_node.next
                raise IndexError("Key does not exist in list")