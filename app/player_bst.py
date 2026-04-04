from app.player import Player
from app.player_bnode import PlayerBNode

class PlayerBST:
    def __init__(self, root: PlayerBNode | None = None) -> None:
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

    def balance(self) -> None:
        #Create a sorted list from the unbalanced BST
        def create_sorted_list(bnode: PlayerBNode | None) -> list[Player]:
            if bnode is None:
                return []
            else:
                return create_sorted_list(bnode.left_bnode) + [bnode.player] + create_sorted_list(bnode.right_bnode)

        def recursion_helper(sorted_list: list[Player]) -> PlayerBNode | None:
            if not sorted_list:
                return None
            else:
                middle = len(sorted_list) // 2
                bnode = PlayerBNode(sorted_list[middle])

                # Create left and right children
                bnode.left_bnode = recursion_helper(sorted_list[:middle])
                bnode.right_bnode = recursion_helper(sorted_list[middle + 1:])

                return bnode

        sorted_list = create_sorted_list(self.root)
        self.root = recursion_helper(sorted_list)


