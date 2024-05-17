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
        temp_list = node.text.split("!")
        double_list = []
        for str in temp_list:
            double_list.append(str.split(")"))
        final_list = flatten(double_list)
        result_list = []
        for i in range(len(final_list)):
            string = final_list[i]
            if i % 2 == 0:
                if string == "":
                    continue
                result_list.append(TextNode(string, "text"))
            else:
                result_list.append(
                    TextNode(re_output[i // 2][0], "image", re_output[i // 2][1])
                )
        new_nodes.append(result_list)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        re_output = extract_markdown_links(node.text)
        temp_list = node.text.split("[")
        double_list = []
        for str in temp_list:
            double_list.append(str.split(")"))
        final_list = flatten(double_list)
        result_list = []
        for i in range(len(final_list)):
            string = final_list[i]
            if i % 2 == 0:
                if string == "":
                    continue
                result_list.append(TextNode(string, "text"))
            else:
                result_list.append(
                    TextNode(re_output[i // 2][0], "link", re_output[i // 2][1])
                )
        new_nodes.append(result_list)
    return new_nodes


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
new_nodes = split_nodes_link(node)
print(new_nodes)
