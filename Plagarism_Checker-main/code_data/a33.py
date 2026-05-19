def create_html(title, content):
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    <p>{content}</p>
</body>
</html>
"""
    return html_content

def main():
    title = input("Enter the title of the HTML page: ")
    content = input("Enter the content for the HTML page: ")
    html = create_html(title, content)
    
    with open("output.html", 'w') as file:
        file.write(html)
    print("HTML page created successfully as output.html")

if __name__ == "__main__":
    main()
