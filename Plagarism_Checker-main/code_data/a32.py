def convert_markdown_to_html(markdown_text):
    html_output = ""
    lines = markdown_text.split('\n')
    
    for line in lines:
        if line.startswith('# '):
            html_output += f"<h1>{line[2:]}</h1>\n"
        elif line.startswith('## '):
            html_output += f"<h2>{line[3:]}</h2>\n"
        elif line.startswith('### '):
            html_output += f"<h3>{line[4:]}</h3>\n"
        else:
            html_output += f"<p>{line}</p>\n"
    
    return html_output

def main():
    markdown_text = """# Sample Title
## Subtitle
This is a sample paragraph in markdown.
### Sub-subtitle
Another paragraph here."""
    
    print("Converting Markdown to HTML...")
    html_result = convert_markdown_to_html(markdown_text)
    print("Converted HTML:\n")
    print(html_result)

if __name__ == "__main__":
    main()
