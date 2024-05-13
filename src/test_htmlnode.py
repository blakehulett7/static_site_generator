import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(props={"tk_1": "tv_1", "tk_2": "tv_2"})
        self.assertEqual("HTMLNode(None, None, None, {'tk_1': 'tv_1', 'tk_2': 'tv_2'})", repr(node))
        
    def test_props_to_html(self):
        node = HTMLNode(props={"tk_1": "tv_1", "tk_2": "tv_2"})
        self.assertEqual(' tk_1="tv_1" tk_2="tv_2"', node.props_to_html())
        
if __name__ == "__main__":
    unittest.main()
