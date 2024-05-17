from textnode import TextNode
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
        for i in range(len(re_output)):
            image = re_output[i]
            split_text = text.split(f"![{image[0]}]({image[1]})", 1)
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], "text"))
            new_nodes.append(TextNode(image[0], "image", image[1]))
            text = split_text[1]
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        re_output = extract_markdown_links(node.text)
        text = node.text
        if len(re_output) == 0:
            new_nodes.append(node)
        for i in range(len(re_output)):
            link = re_output[i]
            split_text = text.split(f"[{link[0]}]({link[1]})", 1)
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], "text"))
            new_nodes.append(TextNode(link[0], "link", link[1]))
            text = split_text[1]
    return new_nodes


"""
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

print(split_nodes_image(node))
"""
