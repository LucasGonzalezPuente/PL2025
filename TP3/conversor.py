def markdown_to_html(markdown: str) -> str:
    lines = markdown.split('\n')
    html_lines = []
    
    in_list = False
    
    for line in lines:
        if line.startswith('# '):
            html_lines.append(f'<h1>{line[2:]}</h1>')
        elif line.startswith('## '):
            html_lines.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('### '):
            html_lines.append(f'<h3>{line[4:]}</h3>')
        elif line.startswith(('1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ')):
            if not in_list:
                html_lines.append('<ol>')
                in_list = True
            html_lines.append(f'<li>{line[3:]}</li>')
        elif in_list:
            html_lines.append('</ol>')
            in_list = False
        else:
            line = line.replace('**', '<b>', 1).replace('**', '</b>', 1)
            line = line.replace('*', '<i>', 1).replace('*', '</i>', 1)
            
            while '[' in line and ']' in line and '(' in line and ')' in line:
                start_text = line.find('[')
                end_text = line.find(']')
                start_url = line.find('(', end_text)
                end_url = line.find(')', start_url)
                
                text = line[start_text + 1:end_text]
                url = line[start_url + 1:end_url]
                
                line = line[:start_text] + f'<a href="{url}">{text}</a>' + line[end_url + 1:]
            
            while '![' in line and ']' in line and '(' in line and ')' in line:
                start_alt = line.find('![')
                end_alt = line.find(']', start_alt)
                start_src = line.find('(', end_alt)
                end_src = line.find(')', start_src)
                
                alt_text = line[start_alt + 2:end_alt]
                src = line[start_src + 1:end_src]
                
                line = line[:start_alt] + f'<img src="{src}" alt="{alt_text}"/>' + line[end_src + 1:]
            
            html_lines.append(line)
    
    if in_list:
        html_lines.append('</ol>')
    
    return '\n'.join(html_lines)

# Entrada de usuario
markdown_text = input("Escriba el texto Markdown:\n")
html_output = markdown_to_html(markdown_text)
print("\nHTML generado:\n", html_output)
