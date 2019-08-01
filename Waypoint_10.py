str = '1 one two 2 3 three four 4 five six'
def capitalize_words(str):
    str=str.strip()
    while (str.find('  ')!=-1):
        str=str.replace('  ',' ')
    str=str.title()
    return str
# def uppercase_lowercase_words(str):
#     str=capitalize_word(str)
#     str=str.split(' ')
#     for i in range(0,len(str)):
#         if i%2!=0:
#             str[i]=str[i].lower()
#         else:
#             str[i]=str[i].upper()
#     return str
str = capitalize_words(str)
str = str.split(' ')
for i in range(0, len(str)):
    if i % 2 != 0:
        str[i] = str[i].lower()
    else:
        str[i] = str[i].upper()
cc = ' '.join(str)
print(cc)