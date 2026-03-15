# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?

> They are all hash functions because they have the same properties as follows:

- Each function takes an input to generate an output, for the same input, the functions would generate the same output.
- They have a chance of having collisions, it happens when the different inputs are mapped into the same index in the hash table, the hash table must then handle it. 
- They take data in and convert it into a number 
- They are used to distribute key-value pairs accross a table by taking the generated number mentioned above and perform a modulo by the size of the hash table
( the number of indexes/ slots available in the table)


2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

> SSH: 
This hash function doesn't have any uniformity, collistion resistance and sesitivity to input changes because it always return a 1 regardless of the outputs. For every different input, it would use the same index in the hash map which means no evenly distributed outputs, collision happens every single time and doesn't matter how much the inputs change the output always stay the same, number 1. However, it does have determinism due to the same reason - always return a 1. It should be really fast though (for storing values into the table) since no internal computing required for it to run. It is not secure because output can be predicted easily, making it prone to attacks, when it's used to look up values though, it would be slow because all values would be jammed in the same index - leaving the collision handling decides how fast looking up values can be. 

ASCII: 
According to OpenDSA's Data Structures and Algorithms (https://chalmersgu-data-structure-courses.github.io/OpenDSA/Published/ChalmersGU-DSABook/html/HashFuncExamp.html):

with this ASCII hash function "If the table size is large compared to the possible sums, the distribution becomes poor" and "The order of characters does not matter, so different permutations of the same letters, produce the same hash value, causing collisions." 

This hash function doesn't have decent uniformity since it takes the sum of ASCII values of the key's characters, and the sum would not change if the order of the character in the key changes. 

For example: abc, acb, bca, bac,.. would have the same ASCII sum of 294, resulting in the same index 

However, it does have excellent determinism because ASCII values of the same string would always be the same value, making the output stay the same. 
With that in mind, it does suffer from poor collision resistance, many different strings would be put into the same index in the table. 

For example: 'stop' and 'pots' would be in the same index (collision) 

So we could say that this function itself is efficient in performing the hash because it requires only the iteration through the characters of string and performing additions but has poor key distribution and many collisions, efficiency can be reduced significantly. 

Security wise, it's not very secure because the sum of ASCII values can be easily deciphered with reverse engineering and it is not secure because it's not very sensitive to input changes. If 1 character changes in the string, the difference would only be a ASCII value of 1 character, the sum of the rest of string stays the same. 

For example: abc has ASCII sum of 294 and abd has ASCII sum of 295 

Pearson:

According to Pearson Hashing on Wikipedia (https://en.wikipedia.org/wiki/Pearson_hashing): this function is designed to be fast and "executes quickly" since "it requires only a few instructions, plus a 256-byte lookup table containing a permutation of the values 0 through 255"

Accoding to Daniel Lemire at ScienceDirect (https://www.sciencedirect.com/science/article/pii/S0166218X11004276?): 







3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> 1. Hash function quality 
This is the most important because uniformity and collision frequency depend directly on the function. Take the SSH as an example, it is a bad function for hashmaps and comepletely defeats the purpose of removing the need to iterate through a double linked list to find a key-value pair (at least in this task that's what we aiming for) 

Collision Resistance
Since we cannot avoid collision in hashmap, a good hashmap should avoid collision as much as possible. Because when collision occurs we bascially have to resolve the initial problem we were trying to solve in the first place one more time, so the less likely the collisions are the better the hasmap

Collision Handling
When collision happens though, we want to handle it the best we can (reason mentioned above). With modern, secured function like SHA 256, collision are less likely but inherently we still need to optimize collision handling for our hashmaps to maximize performance and effciency

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> I would choose the Pearson hash function because it's not too simple that it defeats the purpose of the task but also not over-engineered. However I did use a different hash function in my implementation because I have aleady used Pearson in my last attempt for this task 

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> import random
-> import the random module, used to perform a shuffle of the table 

random.seed(42) 
this is the settings for the random operation, to make sure that for every sessions the Pearson table will be randomized in the same way
this makes the hash map deterministic since it ensures that the same input would generate the same output, without this the table could be randomized differently making the hash values different. 


pearson_table = list(range(256)) 
make a list consist of numbers from 0 to 255 and name it pearson_table 
the 'secret' of Pearson function is the table, if attackers can get access to this table, they can reverse engineer and find out the input, which is why it is not very secure for real world use

random.shuffle(pearson_table) 
this is where the table get randomized or shuffled, so now the table contains numbers from 0 to 255 but in random order 

def pearson_hash(key: str, size: int) -> int: 
declare the function, it takes 2 arguments: key (expects a string) and a size (expects an int) and returns an integer 

hash_ = 0 
sets the hash_ variable to 0 

for char in key:
perform a for loop for every character in the key string

hash_ = pearson_table[hash_ ^ ord(char)]
for each of the character, do this: get the ASCII values of the character then do a bitwise comparison with the previous value of hash_, use the result as the index in the pearson table, then update the hash_ value with its associated value. Because each character in the string affects the next character's hash value, Pearson hash function has moderate sensitivity to input changes. The earlier the change happens in the string, the greater the changes in the final hash value

return hash_ % size 
after finishing the for loop, the final hash value will be put through a modulo with the size of the hash map to decide which index the final hash value belongs to


6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

> Create a hashmap with a fixed size
For each of the index of the hashamp, create a empty PlayerList 
When inserting a player into the hashmap using __setitem__:
Check whether if the key is of type Player or string
    If its a Player, then use the uid of the player as the key
    If its a string, then use that string as the key 

Hash the key to get a value 
Use the value as the index, to know which PlayerList the player belongs to 
Find the player in that list 
    If the player exists in the list 
        update their name 
    If not 
        create a new player 
        create a playernode with that player 
        insert the node to the playerlist 


## Reflection

1. What was the most challenging aspect of this task?

> The most challenging aspect of this task was the implementation of the conceptual idea into code. Meaning I would understand conceptually how it works but only by actually writting the code, I found myself having some hiccups translating the idea into working code. 

And I also struggling with deciding what and how to test certain functions of a given class. I was not sure if my unit tests actually covered all the edge cases or not. 

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> I could use an external hashmap and handle collision by another internal hashmap. Because hashmap provides faster lookup than a double linked list since it doesn't require a iteration like a linked list would to find a given key-value pair 

## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.
