def markdown_to_blocks(md_string):
    block_list = md_string.split("\n\n")
    new_list = []
    for block in block_list:
        if block != "":
            new_list.append(block.strip())
    return new_list


def block_to_block_type(block):
    # Check if Heading Block
    if block.startswith("#"):
        for i in range(1, 7):
            pound = "#" * i
            if block.startswith(f"{pound} "):
                return "heading"
        raise ValueError("invalid syntax, too many headers")
    # Check if Code Block
    if block.startswith("```"):
        if block.endswith("```"):
            return "code"
        raise ValueError("invalid syntax, close code block")
    # Entering the lines section
    lines = block.split("\n")
    # Check if Quote Block
    if block.startswith(">"):
        if all(map(lambda line: line.startswith(">"), lines)):
            return "quote"
        raise ValueError("invalid syntax, reformat quote block")
    # Check if Unordered List
    if block.startswith("* ") or block.startswith("- "):
        if all(map(lambda line: line.startswith("* ") or line.startswith("- "), lines)):
            return "unordered_list"
        raise ValueError("invalid syntax, reformat unordered list block")
    # Check if Ordered List
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                raise ValueError("invalid syntax, reformat ordered list block")
            i += 1
        return "ordered_list"
    return "paragraph"


# md_string = """# This is a heading
"""
This is a paragraph of text. It has some **bold** and *italic* words inside of it.

- This is a list item
* This is another list item

```
Code Block
```

> Quote 1
>Quote 2
> Quote 3

1. This is an ordered list item
2. This is another ordered list item
3. list item
4. list item
5. list item

. Another paragraph block, this one strange


block_list = markdown_to_blocks(md_string)


for block in block_list:
    print(block_to_block_type(block))

print(block_list)
"""
