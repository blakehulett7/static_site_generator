def markdown_to_blocks(md_string):
    block_list = md_string.split("\n\n")
    new_list = []
    for block in block_list:
        if block != "":
            new_list.append(block.strip())
    return new_list

def block_to_block_type(block):
    # Check if Heading Block
    for i in range(1, 7):
        pound = "#" * i
        if block.startswith(f"{pound} "):
            return "heading"
    # Check if Code Block
    if block.startswith("``` "):
        if block.endswith("```"):
            return "code"
        raise ValueError("invalid syntax, close code block")
    # Check if Quote Block
    if block.startswith(">"):
        if all(map(lambda line: line.startswith(">"), block.split("\n"))):
            return "quote"
        raise ValueError("invalid syntax, reformat quote block")
            
        

md_string = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item

``` Code Block ```

> Quote 1
>Quote 2
> Quote 3
"""


block_list_2 = ["Not a Heading", "# Heading 1", "## Heading 2", "### Heading 3", "#### Heading 4", "##### Heading 5", "###### Heading 6", "####### Also not a heading", "``` Code Block ```", "`` Not a code block"]
quote_list = []

block_list = markdown_to_blocks(md_string)


for block in block_list:
    print(block_to_block_type(block))

