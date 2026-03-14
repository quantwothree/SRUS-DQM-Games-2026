import unittest
from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList

class TestPlayerList(unittest.TestCase):
    def test_insert_head_with_empty_list(self):
        player_list = PlayerList()
        self.assertTrue(player_list.is_empty)

        player = Player("01", "Alice")
        node = PlayerNode(player)
        player_list.insert_head(node)

        self.assertFalse(player_list.is_empty)

        # Test if head is the added player node
        self.assertEqual(player_list.head.key, "01")

        # After adding 1 player node to an empty list, nothing should be on either side of head
        self.assertIsNone(player_list.head.previous)
        self.assertIsNone(player_list.head.next)

        # And also tail should be the same as head
        self.assertEqual(player_list.tail.key, player_list.head.key)

    def test_insert_head_with_not_empty_list(self):
        player_list = PlayerList()
        self.assertTrue(player_list.is_empty)

        player1 = Player("01", "Alice")
        player2 = Player("02", "Bob")

        node1 = PlayerNode(player1)
        node2 = PlayerNode(player2)

        player_list.insert_head(node1)
        player_list.insert_head(node2)

        self.assertFalse(player_list.is_empty)

        # Node1 was inserted first so head should be Node 2 with key = 02
        self.assertEqual(player_list.head.key, "02")

        # And head's next node should be Node1
        self.assertEqual(player_list.head.next.key,node1.key)

        # And nothing should be in front of head
        self.assertIsNone(player_list.head.previous)

        # Also tail should be Node 1 with key is 01
        self.assertEqual(player_list.tail.key, "01")

    def test_insert_tail_with_empty_list(self):
        player_list= PlayerList()
        self.assertTrue(player_list.is_empty)

        player = Player("01", "Alice")
        node = PlayerNode(player)
        player_list.insert_tail(node)

        self.assertFalse(player_list.is_empty)

        # Head and tail should be the same because list was empty
        self.assertEqual(player_list.head.key, player_list.tail.key)

        # Nothing should be on either side of head/tail
        # Don't need to test for tail here since we already tested that head IS tail
        self.assertIsNone(player_list.head.previous)
        self.assertIsNone(player_list.head.next)


    def test_insert_tail_with_not_empty_list(self):
        player_list= PlayerList()
        self.assertTrue(player_list.is_empty)

        player1 = Player("01", "Bob")
        player2 = Player("02", "Carl")

        node1 = PlayerNode(player1)
        node2 = PlayerNode(player2)

        player_list.insert_tail(node1)
        player_list.insert_tail(node2)

        # Node1 is now head and node2 is now tail
        self.assertEqual(player_list.head.key, "01")
        self.assertEqual(player_list.tail.key, "02")

        # Head's next should be tail and tail's previous should be head
        self.assertEqual(player_list.head.next.key, player_list.tail.key)
        self.assertEqual(player_list.tail.previous.key, player_list.head.key)

        # nothing should be in front of head and nothing should behind tail
        self.assertIsNone(player_list.head.previous)
        self.assertIsNone(player_list.tail.next)

    def test_delete_at_head_with_empty_list(self):
        player_list = PlayerList()
        self.assertTrue(player_list.is_empty)

        with self.assertRaises(IndexError) as error:
            player_list.delete_at_head()
        self.assertEqual(type(error.exception), IndexError)

    def test_delete_at_head_with_not_empty_list(self):
        player_list = PlayerList()

        player1 = Player("01", "Alice")
        player2 = Player("02", "Bob")

        node1 = PlayerNode(player1)
        node2 = PlayerNode(player2)

        player_list.insert_head(node1)
        player_list.insert_head(node2)

        player_list.delete_at_head()

        self.assertEqual(player_list.head.key, "01")
        self.assertIsNone(player_list.head.previous)
        self.assertIsNone(player_list.head.next)

    def test_delete_at_tail_with_empty_list(self):
        player_list = PlayerList()
        self.assertTrue(player_list.is_empty)

        with self.assertRaises(IndexError) as error:
            player_list.delete_at_tail()
        self.assertEqual(type(error.exception), IndexError)

    def test_delete_at_tail_with_not_empty_list(self):
        player_list = PlayerList()

        player1 = Player("01", "Alice")
        player2 = Player("02", "Bob")

        node1 = PlayerNode(player1)
        node2 = PlayerNode(player2)

        player_list.insert_head(node1)
        player_list.insert_head(node2)

        player_list.delete_at_tail()

        self.assertEqual(player_list.tail.player.uid, "02")
        self.assertIsNone(player_list.tail.previous)
        self.assertIsNone(player_list.tail.next)

    def test_delete_at_key_with_empty_list(self):
        player_list = PlayerList()
        self.assertTrue(player_list.is_empty)

        with self.assertRaises(IndexError) as error:
            player_list.delete_at_key("01")
        self.assertEqual(type(error.exception), IndexError)

    def test_delete_at_key_with_key_is_head_or_tail(self):
        player_list = PlayerList()

        player1 = Player("01", "Alice")
        player2 = Player("02", "Bob")
        player3 = Player("03", "Carl")
        player4 = Player("04", "Dean")

        node1 = PlayerNode(player1)
        node2 = PlayerNode(player2)
        node3 = PlayerNode(player3)
        node4 = PlayerNode(player4)

        player_list.insert_head(node1)
        player_list.insert_head(node2)
        player_list.insert_head(node3)
        player_list.insert_head(node4)

        player_list.delete_at_key("01")
        player_list.delete_at_key("04")

        # Check if head and tail updated correctly - The list key's order is 4 3 2 1
        self.assertEqual(player_list.head.key, "03")
        self.assertEqual(player_list.tail.key, "02")

    def test_delete_at_key_with_1_node(self):
        player_list = PlayerList()
        player1 = Player("01", "Alice")
        node1 = PlayerNode(player1)
        player_list.insert_head(node1)

        player_list.delete_at_key("01")
        self.assertTrue(player_list.is_empty)

    def test_delete_at_key_with_not_empty_list(self):
        player_list = PlayerList()

        player1 = Player("01", "Alice")
        player2 = Player("02", "Bob")
        player3 = Player("03", "Carl")
        player4 = Player("04", "Dean")

        node1 = PlayerNode(player1)
        node2 = PlayerNode(player2)
        node3 = PlayerNode(player3)
        node4 = PlayerNode(player4)

        player_list.insert_head(node1)
        player_list.insert_head(node2)
        player_list.insert_head(node3)
        player_list.insert_head(node4)

        # Test delete with an invalid key
        with self.assertRaises(IndexError) as error:
            player_list.delete_at_key("05")
        self.assertEqual(type(error.exception), IndexError)

        # Test delete with a valid key - The list key's order is 4 3 2 1
        player_list.delete_at_key("03")
        self.assertEqual(player_list.head.next.key, "02")

if __name__ == "__main__":
    unittest.main()