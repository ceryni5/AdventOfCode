import re


string1 = '#53abcde'
string2 = '76in'
print(bool(re.search('^#[a-f0-9]{6}$', string1)))
print(bool(re.search('^(1[6-8][0-9]|19[0-3])cm$|^(59|6[0-9]|7[0-6])in$', string2)))
print(bool(re.search('', string2)))

string3 = 'abcaba'
print(len(set(string3)))
