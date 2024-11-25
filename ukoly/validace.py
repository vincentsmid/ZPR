def xml(input_string):
    all_tags = []
    tag_count = 0
    stack = []
    current_tag = ""
    inside_tag = False

    for char in input_string:
        if char == '<':
            inside_tag = True
            current_tag = '<'
        elif char == '>' and inside_tag:
            current_tag = current_tag + '>'
            inside_tag = False

            tag_count = tag_count + 1

            tag_name = current_tag.replace('<', '').replace('>', '').replace('/', '')

            if tag_name not in all_tags:
                all_tags.append(tag_name)

            if current_tag.endswith('/>'):
                pass
            elif not current_tag.startswith('</'):
                stack.append(tag_name)
            else:
                if len(stack) == 0:
                    return False, None, []
                if stack[-1] != tag_name:
                    return False, None, []
                stack.pop()

            current_tag = ""
        elif inside_tag:
            current_tag = current_tag + char

    if len(stack) > 0 or len(all_tags) == 0:
        return False, None, []

    all_tags.sort()

    return True, tag_count, all_tags

# print(xml('<a><b></a></b>'))
# print(xml('<a><b>10</b><c>ahoj svete</c><d/><d/></a>'))
# print(xml('<table><tr><td>10</td><td>20</td></tr><tr><td><img/></td></tr></table>'))