print("Hello World!")

from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    textnode = TextNode("This is a text node", "italic")
    print(textnode_to_htmlnode(textnode))


def textnode_to_htmlnode(textnode):
    valid_types = ["text", "bold", "italic", "code", "link", "image"]
    if textnode.text_type not in valid_types:
        raise Exception("Invalid Type")
    valid_tags = [None, "b", "i", "code", "a", "img"]
    valid_props = [None, None, None, None, {"href": textnode.url}, {}]
    type_index = valid_types.index(textnode.text_type)
    return LeafNode(valid_tags[type_index], textnode.text, None, 


main()
