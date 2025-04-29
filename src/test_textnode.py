import unittest
from textnode import TextType, TextNode, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        print("test 1 textnode")
        self.assertEqual(node, node2)
        
    def test_not_eq(self):
        node3 = TextNode("This text node is kinda different", TextType.BOLD)
        node4 = TextNode("This text node is more different", TextType.BOLD)
        node5 = TextNode("This text node is more different", TextType.ITALIC)
        print("test 2 textnode")
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node4, node5)

    def test_url(self):
        node6 = TextNode("url test", TextType.TEXT, "https://github.com/p0t8o1/static_site")
        node7 = TextNode("url test", TextType.TEXT, "https://github.com/p0t8o1/static_site")
        node8 = TextNode("url test", TextType.TEXT)
        print("test 3 textnode")
        self.assertEqual(node6, node7)
        self.assertNotEqual(node7,node8)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        print("test 4 textnode")
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        print("test 5 textnode")
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        print("test 6 textnode")
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        print("test 7 textnode")
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://github.com/p0t8o1/static_site")
        html_node = text_node_to_html_node(node)
        print("test 8 textnode")
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href":"https://github.com/p0t8o1/static_site"})

    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://github.com/p0t8o1/static_site")
        html_node = text_node_to_html_node(node)
        print("test 9 textnode")
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": "https://github.com/p0t8o1/static_site", "alt":"This is an image node"})

if __name__ == "__main__":
    unittest.main()