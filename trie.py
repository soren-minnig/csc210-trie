class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.count = 0 # Not necessary but useful for debugging

    def add(self, word):
        node = self.root # Set initial node to root

        for char in word: # For each character
            if char not in node.children:
                node.children[char] = TrieNode() # Add to trie if doesn't already exist
            node = node.children[char] # Move to next node
        node.is_word = True # Mark as the end of a word

    def search(self, word):
        node = self.root # Set initial node to root

        for char in word: # For each character
            if char not in node.children:
                return False # The word does not exist
            node = node.children[char] # Move to next node
        return node.is_word # If marked as is_word will return true
    
# Testing
trie = Trie()
running = True
found = False
command = ""
word = ""

while running:
    command = input("Choose a command (add or search or end): ")
    if (command == "add"):
        word = input("Enter a word to add: ")
        trie.add(word)
        print(f"{word} added")
    elif (command == "search"):
        word = input("Enter a word to search: ")
        found = trie.search(word)
        if found:
            print(f"{word} exists")
        else:
            print(f"{word} does not exist")
    elif (command == "end"):
        running = False
    else:
        continue