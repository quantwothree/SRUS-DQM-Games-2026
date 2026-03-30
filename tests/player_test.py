import unittest, random
from app.player import Player

class PlayerTest(unittest.TestCase):
    def test_uid(self):
        player = Player("01", "Alice")
        self.assertEqual(player.uid, "01")

    def test_name(self):
        player = Player("02", "Bob")
        self.assertEqual(player.name, "Bob")

    def test_sort_players(self):
        players = [Player('01',"Alice", 10), Player('02',"Bob",5),
                   Player('03', "Charlie", 15)]
        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player('02',"Bob", 5), Player('01', "Alice", 10),
                                   Player('03', "Charlie", 15)]
        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player('01', "Alice", 10)
        bob = Player('02', "Bob", 5)

        self.assertLess(bob, alice)

    def test_custom_sort(self):
        players = [Player('01', "Alice", 10), Player('02', "Bob", 5), Player('03', "Charlie", 15)]
        players_manually_sorted = [Player('03', "Charlie", 15), Player('01', "Alice", 10), Player('02', "Bob", 5)]
        players_sorted = Player.custom_sort(players)

        self.assertListEqual(players_sorted, players_manually_sorted)

    def test_custom_sort_with_1000_players(self):
        players = [Player(f"{i:03}", f"Player {i}", random.randint(0, 1000)) for i in range(1000)]
        players_manually_sorted = sorted(players, reverse=True)
        players_sorted = Player.custom_sort(players)

        self.assertListEqual(players_manually_sorted, players_sorted)

    def test_custom_sort_with_sorted_list(self):
        players_unsorted = [Player(f"{i:03}", f"Player {i}", random.randint(0, 1000)) for i in range(1000)]
        players_sorted = sorted(players_unsorted, reverse=True)

        # Use custom sort on the unsorted list
        players_custom_sorted_unsorted_list = Player.custom_sort(players_unsorted)

        # Use custom sort on the sorted list
        players_custom_sorted_sorted_list = Player.custom_sort(players_sorted)

        self.assertListEqual(players_custom_sorted_unsorted_list, players_custom_sorted_sorted_list)


if __name__ == "__main__":
    unittest.main()


