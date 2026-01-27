import unittest
from markdown_blocks import markdown_to_blocks, BlockType, block_to_block_type

class TestMarkdownBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_blocktype(self):
        self.assertEqual(
            block_to_block_type("# Heading 1"),
            BlockType.HEADING
        )
        self.assertEqual(
            block_to_block_type("```\ncode here\n```"),
            BlockType.CODE
        )
        self.assertEqual(
            block_to_block_type("> This is a quote"),
            BlockType.QUOTE
        )
        self.assertEqual(
            block_to_block_type("- item 1\n- item 2"),
            BlockType.UNORDERED_LIST
        )
        self.assertEqual(
            block_to_block_type("1. First item\n2. Second item"),
            BlockType.ORDERED_LIST
        )
        self.assertEqual(
            block_to_block_type("Just a regular paragraph."),
            BlockType.PARAGRAPH
        )