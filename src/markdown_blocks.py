from textnode import TextNode, TextType

def markdown_to_blocks(markdown):
    blocks = []

    split_blocks = markdown.split("\n\n")

    for block in split_blocks:
        strip_blocks = block.strip()
        blocks.append(strip_blocks)

    for block in blocks:
        if block == "":
            blocks.remove(block)

    return blocks