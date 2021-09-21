# To use regular expression to find the pattern in the string

import re

if __name__ == '__main__':
    test_string = '''
    This is a test string.
    This is another test string.
    '''
    pattern = re.compile(r'\bis.*\btest\w*\b')
    print(pattern.findall(test_string))