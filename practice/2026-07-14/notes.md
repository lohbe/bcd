# Worked example — 2026-07-14

## Goal
<!-- What concept/skill is today's worked example targeting? -->
graph visualisation with pyvis

## Approach
<!-- e.g. graph thinking, functional approach, recursion, data structure -->
getting started with pyvis in marimo notebooks

## Worked example
<!-- The worked example / code goes here or in a sibling file -->
pyvis doesn't work with marimo because of missing javascript libraries (so need to use cdn_resources="remote").
also because DOM conflicts - it will try to inject a full HTML document (so need to escape HTML and wrap in iFrame).

full source is in zeus.lan:~/src/pyvis/test.py

run with uvx marimo edit --sandbox --host zeus.lan test.py


```python
import marimo as mo
import html
from pyvis.network import Network

# 1. Use cdn_resources="remote" so the JavaScript loads properly over the web
net = Network(
    height="500px", 
    width="100%", 
    bgcolor="#222222", 
    font_color="white", 
    cdn_resources="remote"
)

# 2. Add Nodes and Edges
net.add_node(1, label="Node 1", color="#FF5733")
net.add_node(2, label="Node 2", color="#33FF57")
net.add_node(3, label="Node 3", color="#3357FF")
net.add_node(4, label="Node 4", color="#F3FF33")

net.add_edge(1, 2)
net.add_edge(1, 3)
net.add_edge(2, 4)
net.add_edge(3, 4)

net.toggle_physics(True)

# 3. Save the graph to a local HTML file
net.write_html("marimo_graph.html")

# 4. Read the HTML content back in
with open("marimo_graph.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 5. Escape the HTML and wrap it in an IFrame for safe rendering in Marimo
escaped_html = html.escape(html_content)
iframe = f'<iframe srcdoc="{escaped_html}" width="100%" height="520px" style="border:none;"></iframe>'

# Render the isolated iframe
mo.Html(iframe)
```

## Reflection
<!-- What did you learn? What was hard? -->
pyvis seems to be user friendly way of visualising graphs, but it's quite an old python library.
Visualising is difficult because it combines the visual aspect (styles, etc) and code with the actual graph.

