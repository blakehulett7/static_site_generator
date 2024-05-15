from htmlnode import LeafNode


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            (self.text == other.text)
            and (self.text_type == other.text_type)
            and (self.url == other.url)
        )

    def __repr__(self):
        return f"TextNode('{self.text}', '{self.text_type}', {self.url})"


def textnode_to_htmlnode(textnode):
    valid_types = ["text", "bold", "italic", "code", "link", "image"]
    if textnode.text_type not in valid_types:
        raise Exception("Invalid Type")
    valid_tags = [None, "b", "i", "code", "a", "img"]
    valid_props = [
        None,
        None,
        None,
        None,
        {"href": textnode.url},
        {"src": textnode.url, "alt": textnode.text},
    ]
    type_index = valid_types.index(textnode.text_type)
    if textnode.text_type == "image":
        textnode.text = ""
    return LeafNode(
        valid_tags[type_index], textnode.text, None, valid_props[type_index]
    )

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
        elif node.text.count(delimiter) % 2:
            raise Exception("invalid markdown syntax")        
        else: 
            node_list = node.text.split(delimiter)
            text_list = node_list[::2]
            special_list = node_list[1::2]
            result_list = []
            specialnode_list = []
            for text in text_list:
                result_list.append(TextNode(text, "text"))
            for special in special_list:
                specialnode_list.append(TextNode(special, text_type))
            for special_node in specialnode_list:
                result_list.insert(specialnode_list.index(special_node) * 2 + 1, special_node)
            new_nodes.extend(result_list)
            
            
    return new_nodes
            
