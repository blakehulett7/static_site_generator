def markdown_to_blocks(md_string):
    block_list = md_string.split("\n\n")
    new_list = []
    for block in block_list:
        if block != "":
            new_list.append(block.strip())
    return new_list

md_string = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item"""

print(markdown_to_blocks(md_string)) 

