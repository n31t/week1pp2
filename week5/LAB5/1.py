import re
txt = '''
a
aaa
llllaob
red_mad_robot
'''
# task 1
x = re.findall('.*a+b?.*', txt)
print(x)
