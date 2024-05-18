from textnode import TextNode, split_nodes_delimiter
import re


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


# List flattener function from the internet
def flatten(xss):
    return [x for xs in xss for x in xs]


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        re_output = extract_markdown_images(node.text)
        text = node.text
        if len(re_output) == 0:
            new_nodes.append(node)
            continue
        for i in range(len(re_output)):
            image = re_output[i]
            split_text = text.split(f"![{image[0]}]({image[1]})", 1)
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], "text"))
            new_nodes.append(TextNode(image[0], "image", image[1]))
            text = split_text[1]
        if text != "":
            new_nodes.append(TextNode(text, "text"))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        re_output = extract_markdown_links(node.text)
        text = node.text
        if len(re_output) == 0:
            new_nodes.append(node)
            continue
        for i in range(len(re_output)):
            link = re_output[i]
            split_text = text.split(f"[{link[0]}]({link[1]})", 1)
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], "text"))
            new_nodes.append(TextNode(link[0], "link", link[1]))
            text = split_text[1]
        if text != "":
            new_nodes.append(TextNode(text, "text"))
    return new_nodes

def text_to_textnodes(text):
    node_list = split_nodes_delimiter([TextNode(text, "text")], "**", "bold")
    node_list = split_nodes_delimiter(node_list, "*", "italic")
    node_list = split_nodes_delimiter(node_list, "`", "code")
    node_list = split_nodes_image(node_list)
    node_list = split_nodes_link(node_list)
    return node_list
    


'''
node = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev), then more text!"


print(text_to_textnodes(node))
'''
