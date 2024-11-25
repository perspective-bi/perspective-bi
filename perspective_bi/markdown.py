import markdown

class MarkdownContent:
    def __init__(self, content):
        self.content = content
        self._html = markdown.markdown(content)
    
    def _repr_html_(self):
        return self._html

def markdown_text(content):
    """Create markdown content that can be displayed in the report"""
    return MarkdownContent(content)