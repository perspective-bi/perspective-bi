import importlib.util
import sys
from flask import Flask, render_template_string
from pathlib import Path
import plotly.graph_objects as go
from .markdown import MarkdownContent

app = Flask(__name__)

def load_module_from_file(file_path):
    """Dynamically load a Python module from file path."""
    spec = importlib.util.spec_from_file_location("dynamic_module", file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["dynamic_module"] = module
    spec.loader.exec_module(module)
    return module

def run_server(file_path, port=3000):
    """Run the perspective-bi server with the given file."""
    module = load_module_from_file(file_path)
    
    @app.route('/')
    def index():
        template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Report</title>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
            <style>
                body { 
                    font-family: Arial, sans-serif; 
                    margin: 20px;
                    line-height: 1.6;
                }
                .chart { margin-bottom: 30px; }
                .markdown-content {
                    margin-bottom: 20px;
                }
            </style>
        </head>
        <body>
            <div id="report">
                {{ content | safe }}
            </div>
        </body>
        </html>
        """
        
        # Get all variables in order of definition
        content = []
        for name, value in module.__dict__.items():
            if not name.startswith('_'):  # Skip private variables
                if isinstance(value, go.Figure):
                    content.append(value.to_html(full_html=False, include_plotlyjs=False))
                elif isinstance(value, MarkdownContent):
                    content.append(f'<div class="markdown-content">{value._repr_html_()}</div>')
        
        return render_template_string(template, content=''.join(content))

    print(f"\nServer running at http://localhost:{port}")
    app.run(host='localhost', port=port, debug=True)