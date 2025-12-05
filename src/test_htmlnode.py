import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",)
        
    def test_missing_tag_raises(self):
        child_node = LeafNode("p", "hello")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_missing_children_raises(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_empty_children_list(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_multiple_children(self):
        child1 = LeafNode("span", "one")
        child2 = LeafNode("span", "two")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>one</span><span>two</span></div>",
        )

    def test_children_must_have_to_html(self):
        class FakeNode:
            pass

        parent_node = ParentNode("div", [FakeNode()])
        with self.assertRaises(AttributeError):
            parent_node.to_html()

    def test_parent_with_props(self):
        child = LeafNode("span", "text")
        parent = ParentNode("div", [child], {"class": "box"})
        self.assertEqual(
            parent.to_html(),
            '<div class="box"><span>text</span></div>'
        )
    
if __name__ == "__main__":
    unittest.main()