import unittest
from app.player import Player
from app.hash_map import HashMap

class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.hashmap = HashMap(5)

    def test_put(self):
        self.hashmap["01"] = "Alice"
        self.hashmap["02"] = "Bob"

        player1 = self.hashmap["01"]
        player2 = self.hashmap["02"]

        self.assertEqual(player1.uid, "01")
        self.assertEqual(player1.name, "Alice")
        self.assertEqual(player2.uid, "02")
        self.assertEqual(player2.name, "Bob")


    def test_get(self):
        self.hashmap["01"] = "Alice"
        self.hashmap["02"] = "Bob"

        player1 = self.hashmap["01"]
        player2 = self.hashmap["02"]

        self.assertEqual(player1.uid, "01")
        self.assertEqual(player1.name, "Alice")
        self.assertEqual(player2.uid, "02")
        self.assertEqual(player2.name, "Bob")

        # Test with invalid key
        with self.assertRaises(IndexError) as error:
            player3 = self.hashmap["03"]
        self.assertEqual(type(error.exception), IndexError)

    def test_get_with_player_object(self):
        self.hashmap["01"] = "Alice"
        player = Player("01", "Placeholder")
        self.assertEqual(self.hashmap[player].name, "Alice")

    def test_put_with_player_object(self):
        player = Player("01", "Alice")
        # This line should update the player's name
        self.hashmap[player] = "New_Name"
        self.assertEqual(self.hashmap[player].name, "New_Name")

    def test_get_index(self):
        index1 = self.hashmap.get_index("01")
        index2 = self.hashmap.get_index("01")

        self.assertIsInstance(index1, int)
        self.assertEqual(index1, index2)

        # Index should be from 0 to 4 because the testing HashMap has a size of 5
        self.assertGreaterEqual(index1, 0)
        self.assertLess(index1, self.hashmap.size)

    def test_get_index_with_player_object(self):
        player1 = Player("01", "Alice")
        player2 = Player("01", "Bob")

        index1 = self.hashmap.get_index(player1)
        index2 = self.hashmap.get_index(player2)

        self.assertIsInstance(index1, int)
        self.assertEqual(index1, index2)
        self.assertGreaterEqual(index1, 0)
        self.assertLess(index1, self.hashmap.size)

    def test_remove(self):
        self.hashmap["01"] = "Alice"
        self.hashmap["02"] = "Bob"

        del self.hashmap["01"]
        del self.hashmap["02"]

        self.assertEqual(len(self.hashmap), 0)

    def test_remove_with_invalid_key(self):
        self.hashmap["01"] = "Alice"
        with self.assertRaises(IndexError) as error:
            del self.hashmap["02"]
        self.assertEqual(type(error.exception), IndexError)

    def test_remove_with_player_object(self):
        player = Player("01", "Alice")
        self.hashmap[player] = "Alice"

        del self.hashmap[player]
        self.assertEqual(len(self.hashmap), 0)

    def test_size(self):
        self.hashmap["01"] = "Alice"
        self.hashmap["02"] = "Bob"
        self.assertEqual(len(self.hashmap), 2)

    def test_display(self):
        self.hashmap["01"] = "Alice"
        self.hashmap["02"] = "Bob"
        self.hashmap["03"] = "Carl"

        print("HashMap: ")
        self.hashmap.display()

if __name__ == "__main__":
    unittest.main()
