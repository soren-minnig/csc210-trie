class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.end

    def startswith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def delete(self, word):
        def _delete(node, word, depth):
            # If we reached end of the word
            if depth == len(word):
                if not node.end:
                    return False  # Word not found
                node.end = False
                return len(node.children) == 0  # Delete if no children

            ch = word[depth]
            if ch not in node.children:
                return False  # Word not found

            # Recursively delete
            should_delete = _delete(node.children[ch], word, depth + 1)

            if should_delete:
                del node.children[ch]
                return len(node.children) == 0 and not node.end

            return False

        _delete(self.root, word, 0)