import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_1(self):
        node = HTMLNode(None, None, None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        result = node.props_to_html()
        self.assertEqual(' href="https://www.google.com" target="_blank"', result)

if __name__ == "__main__":
    unittest.main()