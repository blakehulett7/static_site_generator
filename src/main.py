print("Hello World!")

from textnode import TextNode, textnode_to_htmlnode
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    textnode = TextNode("This is a text node", "link", "boot.dev")
    print(textnode_to_htmlnode(textnode))


main()
