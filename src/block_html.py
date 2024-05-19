from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import textnode_to_htmlnode


def block_to_htmlnode_paragraph(block):
    textnodes = text_to_textnodes(block)
    leafnodes = []
    for textnode in textnodes:
        leafnodes.append(textnode_to_htmlnode(textnode))
    return ParentNode("p", None, leafnodes)


"""
print(
    block_to_html_paragraph(
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
    )
)
"""


def block_to_htmlnode_heading(block):
    textnodes = text_to_textnodes(block.lstrip("#").lstrip(" "))
    leafnodes = []
    for textnode in textnodes:
        leafnodes.append(textnode_to_htmlnode(textnode))
    heading_number = 0
    for char in block:
        if char == "#":
            heading_number += 1
        else:
            break
    return ParentNode(f"h{heading_number}", None, leafnodes)


"""
print(block_to_htmlnode_heading("# Heading 1"))
"""
