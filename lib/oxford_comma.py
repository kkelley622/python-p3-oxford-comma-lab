def oxford_comma(items):
    if not items:
        return ''
    
    string_end = items.pop()
    if not items:
        return string_end
    
    and_display = ' and ' if len(items) == 1 else ', and '
    new_string = ', '.join(items) + and_display + string_end

    return new_string

