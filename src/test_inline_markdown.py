import unittest

from textnode import TextNode

from inline_markdown import split_nodes_image, split_nodes_link


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
