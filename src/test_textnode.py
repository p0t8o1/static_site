import unittest
from textnode import TextType, TextNode

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
        node6 = TextNode("url test", TextType.NORMAL, "https://github.com/p0t8o1/static_site")
        node7 = TextNode("url test", TextType.NORMAL, "https://github.com/p0t8o1/static_site")
        node8 = TextNode("url test", TextType.NORMAL)
        print("test 3 textnode")
        self.assertEqual(node6, node7)
        self.assertNotEqual(node7,node8)

if __name__ == "__main__":
    unittest.main()