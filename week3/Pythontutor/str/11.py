s = input()
s = s.replace("h", "H")
A = s.find('H')
B = s.rfind('H')
print(s[:A]+'h'+s[A+1:B]+'h'+s[B+1:])
