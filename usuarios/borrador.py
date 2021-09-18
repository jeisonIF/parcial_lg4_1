import re

def valip(contra):
   

    regex = re.compile('^(?=\S{0,8}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')
    return bool(regex.search(contra))


print(valip('J$eison1'))