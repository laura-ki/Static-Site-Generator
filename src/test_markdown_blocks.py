import unittest
from markdown_blocks import markdown_to_blocks, BlockType, block_to_block_type, extract_title

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
        def test_extract_title_with_spaces(self):
            md = """#   My Title With Spaces

    Some content here.
    """
            self.assertEqual(extract_title(md), "My Title With Spaces")

        def test_extract_title_with_multiple_headings(self):
            md = """# First Title

    Some content.

    ## Second Title

    More content.
    """
            self.assertEqual(extract_title(md), "First Title")

        def test_extract_title_with_no_title(self):
            md = """
    Some content without a heading.
    """
            with self.assertRaises(Exception):
                extract_title(md)

        def test_extract_title_with_heading_and_text(self):
            md = """#TitleWithNoSpace
    Some content.
    """
            self.assertEqual(extract_title(md), "TitleWithNoSpace")

        def test_extract_title_with_leading_newlines(self):
            md = """



    # Leading Newlines Title

    Content.
    """
            self.assertEqual(extract_title(md), "Leading Newlines Title")

        def test_extract_title_with_hashes_in_text(self):
            md = """# Title #1

    Some content.
    """
            self.assertEqual(extract_title(md), "Title #1")