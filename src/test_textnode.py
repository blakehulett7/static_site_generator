import unittest

from textnode import TextNode, textnode_to_htmlnode, split_nodes_delimiter


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
        self.assertEqual(
            "TextNode('This is a text node', 'bold', ChristisKing.com)", repr(node)
        )
        
    def test_split_function_bold(self):
        old_nodes = [
                TextNode("this is a **test** string.", "text"),
                TextNode("**this is a weird test string**", "bold"),
                TextNode("**this** is a test **string.**", "text")
        ]
        self.assertEqual(split_nodes_delimiter(old_nodes, "**", "bold"), [TextNode("this is a ", "text", None), TextNode("test", "bold", None), TextNode(" string.", "text", None), TextNode("**this is a weird test string**", "bold", None), TextNode("", "text", None), TextNode("this", "bold", None), TextNode(" is a test ", "text", None), TextNode("string.", "bold", None), TextNode("", "text", None)])
        
    def test_split_function_italic(self):
        old_nodes = [
            TextNode("this *is* a test string.", "text"),
            TextNode("*this is a weird test string*", "italic"),
            TextNode("*this* is a test *string.*", "text")
        ]
        self.assertEqual(split_nodes_delimiter(old_nodes, "*", "italic"), [TextNode('this ', 'text', None), TextNode('is', 'italic', None), TextNode(' a test string.', 'text', None), TextNode('*this is a weird test string*', 'italic', None), TextNode('', 'text', None), TextNode('this', 'italic', None), TextNode(' is a test ', 'text', None), TextNode('string.', 'italic', None), TextNode('', 'text', None)])

    def test_split_function_code(self):
        old_nodes = [
            TextNode("this is `a` test string.", "text"),
            TextNode("`this is a weird test string`", "code"),
            TextNode("`this` is a test `string.`", "text")
        ]
        self.assertEqual(split_nodes_delimiter(old_nodes, "`", "code"), [TextNode('this is ', 'text', None), TextNode('a', 'code', None), TextNode(' test string.', 'text', None), TextNode('`this is a weird test string`', 'code', None), TextNode('', 'text', None), TextNode('this', 'code', None), TextNode(' is a test ', 'text', None), TextNode('string.', 'code', None), TextNode('', 'text', None)])

if __name__ == "__main__":
    unittest.main()
