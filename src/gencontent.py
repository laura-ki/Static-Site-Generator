from markdown_blocks import markdown_to_html_node, extract_title
from htmlnode import ParentNode
import os

def generate_page(from_path, template_path, dest_path, basepath):

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
    rep_href = replaced_content.replace(f'href="/', f'href="{basepath}')
    rep_src = rep_href.replace(f'src="/', f'src="{basepath}')
    new_content = rep_src

    dirpath = os.path.dirname(dest_path)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(new_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    files = os.listdir(dir_path_content)
    for file in files:
        src_path = os.path.join(dir_path_content, file)
        if os.path.isdir(src_path):
            dest_subdir = os.path.join(dest_dir_path, file)
            os.makedirs(dest_subdir, exist_ok=True)
            generate_pages_recursive(src_path, template_path, dest_subdir, basepath)
        else:
            if file.endswith(".md"):
                src_path = os.path.join(dir_path_content, file)
                html_filename = file.replace("index.md", "index.html")
                dest_path = os.path.join(dest_dir_path, html_filename)
                generate_page(src_path, template_path, dest_path, basepath)


