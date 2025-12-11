import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHama

marynazelenska.com

321-555-4321
123.555.1234
123*555*1234
800*555*1234
900-555-1234

Mr. Test
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

mat
cat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

# function finditer() <re.Match object; span=(2, 3), match='a'>

# pattern = re.compile(r'start', flags=re.IGNORECASE) # case is important flag I
# matches = pattern.finditer(sentence)
#
# for el in matches:
#     print(el)


# explain about . \d

# pattern = re.compile(r'\W', flags=re.IGNORECASE)
# # pattern = re.compile(r'marynazelenska\.com', flags=re.IGNORECASE) # need to use \.
# matches = pattern.finditer(text_to_search)
#
# for el in matches:
#     print(el)


# explain about \b

# pattern = re.compile(r'\bma', re.I)
# matches = pattern.finditer(text_to_search)
#
# for el in matches:
#     print(el)


# explain about ^ $

# pattern = re.compile(r'^t', re.I)
# pattern = re.compile(r'end$', re.I)
# matches = pattern.finditer(sentence)
#
# for el in matches:
#     print(el)


# try to found
"""
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
"""


# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d', re.I)
# pattern = re.compile(r'\d\d\d[.-]\d\d\d[-.]\d\d\d\d', re.I)
# pattern = re.compile(r'\d{3}[.-]\d{3}[-.]\d{3,4}', re.I)
# # matches = pattern.finditer(text_to_search)
# matches = pattern.findall(text_to_search)
# print(matches)


"""
try to find
800-555-1234
900*555*1234
"""

pattern = re.compile(r'[89]00[.*-]\d\d\d[*-.]\d\d\d\d', re.I)
matches = pattern.findall(text_to_search)
print(matches)


"""
find 
mat
cat
but not bat
"""
#
# pattern = re.compile(r'[^b]at')
# matches = pattern.findall(text_to_search)
# print(matches)


"""
Mr. Test
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""
#
# pattern = re.compile(r'M(?:r|rs|s)\.?\s[A-Z]\w*')
# matches = pattern.findall(text_to_search)
# print(matches)


"""
find emails
emails = '''
MarynaZelenska@gmail.com
maryna.zelenska@test.edu
maryna-321-zelenska@hillel.ua
'''
"""

emails = '''
MarynaZelenska@gmail.com
maryna.zelenska@test.edu
maryna-321-zelenska@hillel.ua
'''

# pattern = re.compile(r'[A-Za-z0-9.-]+@[A-Za-z]+\.(?:com|edu|ua)')
# pattern = re.compile(r'[\w.-]+@[A-Za-z]+\.(?:com|edu|ua)')
# matches = pattern.findall(emails)
# print(matches)

"""
work with groups
urls = '''
https://www.google.com
http://zelenska.com
https://youtube.com
https://www.nasa.gov
'''
"""

urls = '''
https://www.google.com
http://zelenska.com
https://youtube.com
https://www.nasa.gov
'''

# pattern = re.compile(r'https?://(www\.)?(\w+\.)(com|gov)')
#
# subbed_urls = pattern.sub(r'\2\3', urls)
# print(subbed_urls.strip().split('\n'))

# matches = re.findall(pattern, urls)
# print(matches)
# matches = pattern.finditer(urls)
# for match in matches:
#     print(match.group(3))


