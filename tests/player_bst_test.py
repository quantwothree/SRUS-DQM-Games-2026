import unittest
from app.player import Player
from app.player_bst import PlayerBST

class TestPlayerBST(unittest.TestCase):
    def setUp(self):
        self.bst = PlayerBST(None)
        self.players = [
            Player("8", "Henry", 88),
            Player("4", "David", 102),
            Player("2", "Bob", 42),
            Player("6", "Frank", 31),
            Player("12", "Leo", 56),
            Player("9", "Henry", 99)
        ]

    def test_add_player_to_empty_tree(self):
        self.bst.insert(self.players[0]) #Henry

        self.assertIsNotNone(self.bst.root)
        self.assertEqual(self.bst.root.player.name, "Henry")
        self.assertIsNone(self.bst.root.left_bnode)
        self.assertIsNone(self.bst.root.right_bnode)

    def test_add_players_to_tree_with_root(self):
        self.bst.insert(self.players[0]) #Henry is root
        self.bst.insert(self.players[2]) #Bob is left to Henry
        self.bst.insert(self.players[4]) #Leo is right to Henry

        self.assertEqual(self.bst.root.left_bnode.player.name, "Bob")
        self.assertEqual(self.bst.root.right_bnode.player.name, "Leo")

    def test_deep_recursion(self):
        self.bst.insert(self.players[0]) #Henry is root
        self.bst.insert(self.players[1]) #David is left to Henry
        self.bst.insert(self.players[2]) #Bob is left to David
        self.bst.insert(self.players[3]) #Frank is right to David

        self.assertEqual(self.bst.root.left_bnode.left_bnode.player.name, "Bob")
        self.assertEqual(self.bst.root.left_bnode.right_bnode.player.name, "Frank")

        #Checks right of Henry
        self.assertIsNone(self.bst.root.right_bnode)

        #Checks both side of Bob
        self.assertIsNone(self.bst.root.left_bnode.left_bnode.left_bnode)
        self.assertIsNone(self.bst.root.left_bnode.left_bnode.right_bnode)

        #Checks both side of Frank
        self.assertIsNone(self.bst.root.left_bnode.right_bnode.left_bnode)
        self.assertIsNone(self.bst.root.left_bnode.right_bnode.right_bnode)

    def test_duplication(self):
        self.bst.insert(self.players[0]) #Henry with score of 88
        self.bst.insert(self.players[-1]) #Henry with score of 99

        self.assertIsNone(self.bst.root.left_bnode)
        self.assertIsNone(self.bst.root.right_bnode)
        self.assertEqual(self.bst.root.player.score, 99)

if __name__ == '__main__':
    unittest.main()