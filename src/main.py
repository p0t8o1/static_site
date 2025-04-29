from inline_markdown import split_nodes_delimiter
from textnode import *

def main():
    print(TextNode("ha ha ha", TextType.BOLD).__repr__())
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)

main()