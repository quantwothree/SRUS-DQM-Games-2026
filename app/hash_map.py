from app.player_list import PlayerList
from app.player import Player
from app.player_node import PlayerNode

class HashMap:
    def __init__(self, size: int) -> None:
        self.size = size
        self.hashmap = []
        for i in range(self.size):
            self.hashmap.append(PlayerList())

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.size
        else:
            temp_player = Player(key, "")
            return hash(temp_player) % self.size

    def __setitem__(self, key: str | Player, name: str) -> None:
        if isinstance(key, str):
            uid = key
        else:
            uid = key.uid
        # Accessing the PlayerList at the correct index
        player_list = self.hashmap[self.get_index(key)]
        # Calls __contains__ in PlayerList
        if uid in player_list:
            player = player_list.get_player_at_key(uid)
            player.name = name
        else:
            player = Player(uid, name)
            node = PlayerNode(player)
            player_list.insert_head(node)

    def __getitem__(self, key: str | Player) -> Player:
        if isinstance(key, str):
            uid = key
        else:
            uid = key.uid
        player_list = self.hashmap[self.get_index(key)]

        if uid in player_list:
            player = player_list.get_player_at_key(uid)
            return player
        else:
            raise IndexError("Player does not exist")

    def __delitem__(self, key: str | Player) -> None:
        if isinstance(key, str):
            uid = key
        else:
            uid = key.uid
        player_list = self.hashmap[self.get_index(key)]

        if uid in player_list:
            player_list.delete_at_key(uid)
        else:
            raise IndexError("Player does not exist")

    def __len__(self) -> int:
        count = 0
        for i in range(self.size):
            player_list = self.hashmap[i]
            count += len(player_list)
        return count

    def display(self):
        for index in range(self.size):
            player_list = self.hashmap[index]
            if player_list.is_empty:
                continue
            current_node = player_list.head
            while current_node:
                print(f"Index {index}: {current_node.player}")
                current_node = current_node.next