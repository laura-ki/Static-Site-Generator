from markdown_blocks import markdown_to_html_node, extract_title
from htmlnode import ParentNode
import os

def generate_page(from_path, template_path, dest_path):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as md_file:
        md_file_text = md_file.read()
    

    with open(template_path) as html_file:
        html_file_text = html_file.read()
    

    md_node = markdown_to_html_node(md_file_text)
    md_to_html = md_node.to_html()
    title = extract_title(md_file_text)
    replaced_title = html_file_text.replace("{{ Title }}", title)
    replaced_content = replaced_title.replace("{{ Content }}", md_to_html)
    new_content = replaced_content

    dirpath = os.path.dirname(dest_path)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(new_content)



