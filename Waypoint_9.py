def capitalize_word(str):
    str=str.strip()
    while (str.find('  ')!=-1):
        str=str.replace('  ',' ')
    str=str.title()
    return str
