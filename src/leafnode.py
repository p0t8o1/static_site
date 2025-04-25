from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag,value,None,props)
    def to_html(self):
        if self.tag == None:
            if self.value == None:
                raise ValueError
            return self.value
        if self.props is not None:
            propsHTML = super().props_to_html()
            return f'<{self.tag}{propsHTML}>{self.value}</{self.tag}>'
        return f'<{self.tag}>{self.value}</{self.tag}>'