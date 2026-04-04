Knowledge Questions.

Question 1: In your own words, describe what a Binary Search Tree (BST) is.
In addition, describe two important properties of a BST: depth and height. How are they different?

Answer:

    A BST is essentially a binary tree where the nodes have an ordered structure, where for each node:

    - All nodes to its left have values less than the node's value 
    - All nodes to its right have values greater than the node's value 

    Two important properties of a BST:
    
    1. Depth: Depth of a BST refers to the depth of its deepest node. In which the depth of a node is the number of 'edges' from that node to the root node. (The root node is the node with depth of 0 - or the starting node). 

    2. Height: Height of a BST refers to the longest 'edges' from the root node to a leaf node. In which a leaf node is a node that has no children node. 

    The difference between depth and height:

    In BST, both depth and height of a node gives us the position of the node in the BST. But they differs in the direction. 
    While the depth of a node measure how far it is from that node to the root, the height in the other hand measure the longest path for that node to reach a leaf. 

    When we refers to the depth of a node, it's unambiguous because there is only 1 path from the root to that node, wheareas there might be many paths from a node to a leaf, therefore we need to take the longest path to a leaf as its height. 

Question 2: In your own words, describe how an algorithm to find an item in a Binary Search Tree works.

Answer:

    An algorithm finds a node in a BST by doing the following:

    1. We compare the target node's value to the current node's value, with the current node being the root node for the first comparison, the current node gets updated for every recursion moving forward. 
    2. Base on this comparison:

        If the target node's value equals to the current node's value -> Target node found
        If the target nobde's value is less than the current's node value -> Update the current node to the left child node 
        If the the target node's value is greater than the current's node value -> Update the current node to the right child node 

        And we repeat this process until we find the target node unless we reach a node where there is no child node in the direction that we want to go then the target node is not in the BST 

Question 3: In your own words, describe what a balanced BST is. 

Answer: 

    A balanced BST is a BST tree where if we pick any random node, its left and right sub-trees should have a difference in heights of no more than 1. Plus if we pick any random node its left and right sub-trees should also be itself a balanced BST. 


Question 8:

Answer: 

    Because we pick the middle element of the list as root for the sub-trees, we essentially cut down in half the amount of elements for every recursion. 

    If we start with n elements 
    After 1 recursion: we have n/2 elements left in each sub-tree
    After 2 recursion: we have n/4 elements left in each sub-tree
    After 3 recursion: we have n/8 elements left in each sub-tree
    And so on 

    So we need to find out how many times can we devide n elements by 2 before we hit 1 element 

    To do that we solve n / (2 ^ x ) = 1, where x is the number of times we can divide

    <=> n = 2 ^ x 
    => x = log2n 

    Therefore, we need at most log2n steps to find an element in the balanced tree, where n is the number of elements.




    

