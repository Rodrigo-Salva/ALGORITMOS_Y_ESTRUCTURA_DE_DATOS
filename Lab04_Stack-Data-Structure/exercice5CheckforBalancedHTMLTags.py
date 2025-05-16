def is_balanced_html(html):
    import re
    stack = []
    
    tags = re.findall(r'</?[^<>]+>', html)

    for tag in tags:
        if not tag.startswith('</'):
            tag_name = tag[1:-1]
            stack.append(tag_name)
        else:
            if not stack:
                return False
            tag_name = tag[2:-1]
            if stack[-1] == tag_name:
                stack.pop()
            else:
                return False
    
    return len(stack) == 0

if __name__ == "__main__":
    html_text = "<div><p>Hello, world!</p></div>"
    
    result = is_balanced_html(html_text)
    print("Tags are balanced:", result)
