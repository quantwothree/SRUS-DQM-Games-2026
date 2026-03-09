import unittest
from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList

class TestPlayerList(unittest.TestCase):
    def test_insert_head_with_empty_list(self):
        # Create the Player List
        player_list = PlayerList()

        # Test if list is empty
        self.assertTrue(player_list.is_empty)

        player = Player("01", "Alice")
        node = PlayerNode(player)
        player_list.insert_head(node)

        # After adding a node, list should not be empty here
        self.assertFalse(player_list.is_empty)

        # Test if head is the added player node
        self.assertEqual(player_list.head.key, "01")

        # After adding 1 player node to an empty list, nothing should be on either side of head
        self.assertIsNone(player_list.head.previous)
        self.assertIsNone(player_list.head.next)

    def test_insert_head_with_not_empty_list(self):
        # Create the Player List
        player_list = PlayerList()

        # Test if list is empty
        self.assertTrue(player_list.is_empty)

        # Create 2 players
        player1 = Player("01", "Alice")
        player2 = Player("02", "Bob")

        # create 2 nodes from the 2 players
        node1 = PlayerNode(player1)
        node2 = PlayerNode(player2)

        # insert the nodes at head
        player_list.insert_head(node1)
        player_list.insert_head(node2)

        # Test if list is not empty after inserting nodes
        self.assertFalse(player_list.is_empty)

        # Node1 was inserted first so head should be Node 2 with key = 02
        self.assertEqual(player_list.head.key, "02")

        # And head's next node should be Node1
        self.assertEqual(player_list.head.next.key,node1.key)

        # And nothing should be in front of head
        self.assertIsNone(player_list.head.previous)

    if __name__ == "__main__":
        unittest.main()