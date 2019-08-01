def capitalize_word(str):
    str=str.strip()
    while (str.find('  ')!=-1):
        str=str.replace('  ',' ')
    str=str.title()
    return str
def uppercase_lowercase_words(str):
    str=capitalize_word(str)
    str=str.split(' ')
    for i in range(0,len(str)):
        if i%2!=0:
            str[i]=str[i].lower()
        else:
            str[i]=str[i].upper()
    return str
