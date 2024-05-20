from block_html import (
    block_to_htmlnode_code,
    block_to_htmlnode_heading,
    block_to_htmlnode_ordered_list,
    block_to_htmlnode_paragraph,
    block_to_htmlnode_quote,
    block_to_htmlnode_unordered_list,
)
from block_markdown import markdown_to_blocks, block_to_block_type
from htmlnode import ParentNode, LeafNode


def md_to_htmlnode(markdown_document):
    blocks = markdown_to_blocks(markdown_document)
    block_types = []
    for block in blocks:
        block_types.append(block_to_block_type(block))
    nodes = []
    for block in blocks:
        block_type = block_types[blocks.index(block)]
        func = f"block_to_htmlnode_{block_type}(block)"
        node = eval(func)
        nodes.append(node)
    return ParentNode("div", None, nodes)


md_string = """# This is a **bold** heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

- This is a list item
* This is another *italicized* list item

```
Code Block
```

> Quote 1
>Quote 2
> Quote 3

1. This is an ordered list item
2. This is another ordered list item
3. `coded` list item
4. list item with **bold** and *italics*
5. list item

. Another paragraph block, this one strange
"""

# print(md_to_htmlnode(md_string))
