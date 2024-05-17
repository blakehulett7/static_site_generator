import unittest

from textnode import TextNode

from inline_markdown import split_nodes_image, split_nodes_link, text_to_textnodes


class TestMarkdown(unittest.TestCase):
    def test_split_md_image(self):
        node = [
            TextNode(
                "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                "text",
            ),
            TextNode(
                "This is text with a second ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                "text",
            ),
            TextNode("This is text with no image", "text"),
        ]
        expected_output = [
            TextNode("This is text with an ", "text", None),
            TextNode(
                "image",
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            TextNode(" and another ", "text", None),
            TextNode(
                "second image",
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
            ),
            TextNode("This is text with a second ", "text", None),
            TextNode(
                "image",
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            TextNode(" and another ", "text", None),
            TextNode(
                "second image",
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
            ),
            TextNode("This is text with no image", "text", None),
        ]

        self.assertEqual(split_nodes_image(node), expected_output)

    def test_split_md_link(self):
        node = [
            TextNode(
                "This is text with a linked [image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                "text",
            ),
            TextNode(
                "This is text with a second [image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                "text",
            ),
            TextNode("This is text with no link", "text"),
        ]
        expected_output = [
            TextNode("This is text with a linked ", "text", None),
            TextNode(
                "image",
                "link",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            TextNode(" and another ", "text", None),
            TextNode(
                "second image",
                "link",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
            ),
            TextNode("This is text with a second ", "text", None),
            TextNode(
                "image",
                "link",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            TextNode(" and another ", "text", None),
            TextNode(
                "second image",
                "link",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
            ),
            TextNode("This is text with no link", "text", None),
        ]
        self.assertEqual(split_nodes_link(node), expected_output)

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        expected_output = [TextNode('This is ', 'text', None), TextNode('text', 'bold', None), TextNode(' with an ', 'text', None), TextNode('italic', 'italic', None), TextNode(' word and a ', 'text', None), TextNode('code block', 'code', None), TextNode(' and an ', 'text', None), TextNode('image', 'image', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png'), TextNode(' and a ', 'text', None), TextNode('link', 'link', 'https://boot.dev')]
        self.assertEqual(text_to_textnodes(text), expected_output)