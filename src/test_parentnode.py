import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        print("test 1 parentnode")
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        print("test 2 parentnode")
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_no_children(self):
        node = ParentNode("div", None)
        print("test 3 parentnode")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_tag(self):
        child_node = LeafNode("span", "child")
        node = ParentNode(None, [child_node])
        print("test 4 parentnode")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_props(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        child_node = LeafNode("span", "child", props)
        node = ParentNode("p", [child_node])
        print("test 5 parentnode")
        self.assertEqual(node.to_html(), '<p><span href="https://www.google.com" target="_blank">child</span></p>')