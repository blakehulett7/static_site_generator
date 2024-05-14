import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(props={"tk_1": "tv_1", "tk_2": "tv_2"})
        self.assertEqual(
            "HTMLNode(None, None, None, {'tk_1': 'tv_1', 'tk_2': 'tv_2'})", repr(node)
        )

    def test_props_to_html(self):
        node = HTMLNode(props={"tk_1": "tv_1", "tk_2": "tv_2"})
        self.assertEqual(' tk_1="tv_1" tk_2="tv_2"', node.props_to_html())


class TestLeafNode(unittest.TestCase):
    def test_constructor_defaults(self):
        node = LeafNode(value="test_string")
        self.assertEqual(repr(node), "LeafNode(None, test_string, None, None)")

    def test_constructor_nochildren(self):
        node = LeafNode(
            tag="p",
            value="test_string",
            children="a lot of them",
            props={"href": "https://www.google.com"},
        )
        self.assertEqual(
            repr(node),
            "LeafNode(p, test_string, None, {'href': 'https://www.google.com'})",
        )

    def test_to_html_notag(self):
        node = LeafNode(value="test_string", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "test_string")

    def test_to_html_noprops(self):
        node = LeafNode(tag="p", value="test_string")
        self.assertEqual(node.to_html(), "<p>test_string</p>")

    def test_to_html(self):
        node = LeafNode(
            tag="a",
            value="test_string",
            children="a lot of them",
            props={"href": "https://www.google.com"},
        )
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">test_string</a>'
        )


class TestParentNode(unittest.TestCase):
    def test_constructor(self):
        node = ParentNode(
            "p",
            children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            repr(node),
            "ParentNode(p, None, [LeafNode(b, Bold text, None, None), LeafNode(None, Normal text, None, None), LeafNode(i, italic text, None, None), LeafNode(None, Normal text, None, None)], None)",
        )

    def test_to_html(self):
        node = ParentNode(
            tag="p",
            children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_nested_parents(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        node2 = ParentNode("p", children=node)


if __name__ == "__main__":
    unittest.main()
