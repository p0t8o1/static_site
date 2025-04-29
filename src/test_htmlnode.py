import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node1 = HTMLNode(None, None, None, props)
        print("test 1 htmlnode")
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_props(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            "className":"avatar", 
            "src":"path/to/image.jpg", 
            "alt":"Avatar", 
            "width":"50", 
            "height":"50"
        }
        node1 = HTMLNode("h1", "value1", None, props)
        print("test 2 htmlnode")
        self.assertEqual(node1.__repr__(),  "HTMLNode(h1, value1, None, " + str(props) + ")")
    
    def test_full_repr(self):
        props_node2 = {
            "href": "https://www.google.com",
            "target": "_blank",
            "className":"avatar",
        }
        node2 = HTMLNode("p", "Hi", None, props_node2)
        node3 = HTMLNode("p", "HIYA")
        nodelist = [node2, node3]
        props_node1 = {
            "alt":"Avatar", 
            "width":"50", 
            "height":"50"
        }
        node1 = HTMLNode("h1", "value1", nodelist, props_node1)
        print("test 3 htmlnode")
        self.assertEqual(node1.__repr__(), "HTMLNode(h1, value1, " + str(nodelist) + ", " + str(props_node1) + ")")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        print("test 1 leafnode")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print("test 2 leafnode")
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_leaf_node_none(self):
        node = LeafNode()
        print("test 3 leafnode")
        with self.assertRaises(ValueError):
            print(node.to_html())
    
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

if __name__ == "__main__":
    unittest.main()