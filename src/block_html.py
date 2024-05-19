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


def block_to_htmlnode_code(block):
    textnodes = text_to_textnodes(block.strip("```"))
    leafnodes = []
    for textnode in textnodes:
        leafnodes.append(textnode_to_htmlnode(textnode))
    for leafnode in leafnodes:
        leafnode.tag = "code"
    return ParentNode("pre", None, leafnodes)


"""
print(block_to_htmlnode_code("```\ncode\n```"))
"""


def block_to_htmlnode_quote(block):
    quote_list = block.split("\n")
    new_quotes = []
    for quote in quote_list:
        if quote != "":
            new_quotes.append(quote.lstrip(">").lstrip())
    textnodes = text_to_textnodes("\n".join(new_quotes))
    leafnodes = []
    for textnode in textnodes:
        leafnodes.append(textnode_to_htmlnode(textnode))
    return ParentNode("blockquote", None, leafnodes)


"""
print(block_to_htmlnode_quote("> quote\n> more > quote"))
"""


def block_to_htmlnode_unordered_list(block):
    list_items = []
    block_list = block.split("\n")
    for line in block_list:
        list_items.append("<li>" + line[2:] + "<li>")
    new_block = "\n".join(list_items)
    textnodes = text_to_textnodes(new_block)
    leafnodes = []
    for textnode in textnodes:
        leafnodes.append(textnode_to_htmlnode(textnode))
    return ParentNode("ul", None, leafnodes)


"""
print(block_to_htmlnode_unordered_list("* *italicized* list\n* **bolded** items"))
"""
