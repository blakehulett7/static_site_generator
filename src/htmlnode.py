class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        string = ""
        for key, value in self.props.items():
            string += f' {key}="{value}"'
        return string


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag, value, children, props)
        self.children = None
        if self.value is None:
            raise ValueError("value is required")

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag, value, children, props)
        self.value = None
        if self.children is None:
            raise ValueError("children required")

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag required")
        child_texts = []
        for child in self.children:
            child_texts.append(child.to_html())
        children_string = "".join(child_texts)
        return f"<{self.tag}>{children_string}</{self.tag}>"


node = ParentNode(
    "p",
    children=[
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

node2 = ParentNode("p", children=node)

print(node2.to_html())
