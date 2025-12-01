import unittest
from trie import Trie

class TestTrie(unittest.TestCase):

    def test_insert_and_search(self):
        t = Trie()
        t.insert("hello")
        self.assertTrue(t.search("hello"))
        self.assertFalse(t.search("hell"))
        self.assertFalse(t.search("world"))

    def test_startswith(self):
        t = Trie()
        t.insert("car")
        t.insert("cat")
        self.assertTrue(t.startswith("ca"))
        self.assertFalse(t.startswith("dog"))

    def test_delete(self):
        t = Trie()
        t.insert("test")
        t.insert("team")

        t.delete("test")

        self.assertFalse(t.search("test"))
        self.assertTrue(t.search("team"))  # Ensure other words unaffected

    def test_delete_nonexistent(self):
        t = Trie()
        t.insert("abc")
        t.delete("xyz")  # Should not break
        self.assertTrue(t.search("abc"))

    def test_multiple_words(self):
        t = Trie()
        words = ["apple", "app", "application", "apply"]

        for w in words:
            t.insert(w)

        for w in words:
            self.assertTrue(t.search(w))

        self.assertTrue(t.startswith("app"))
        self.assertFalse(t.startswith("banana"))

if __name__ == "__main__":
    unittest.main()