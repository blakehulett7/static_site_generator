import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
    def test_eq_withurl(self):
        node = TextNode("This is a text node", "bold", "ChristisKing.com")
        node2 = TextNode("This is a text node", "bold", "ChristisKing.com")
        self.assertEqual(node, node2)
        
    def test_not_eq_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a mismatched text node", "bold")
        self.assertNotEqual(node, node2)
        
    def test_not_eq_property(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)
        
    def test_not_eq_url(self):
        node = TextNode("This is a text node", "bold", "JesusisLord.com")
        node2 = TextNode("This is a text node", "italic", "ChristisKing.com")
        self.assertNotEqual(node, node2)
        
    def test_repr(self):
        node = TextNode("This is a text node", "bold", "ChristisKing.com")
        self.assertEqual("TextNode(This is a text node, bold, ChristisKing.com)", repr(node))


if __name__ == "__main__":
    unittest.main()
