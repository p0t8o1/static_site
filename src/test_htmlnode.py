import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()