s = input()
alnum =False
alpha =False
digit=False
lower =False
upper=False
for i in range (len(s)):
	if s[i].isalnum() == True:
		alnum = True
	if s[i].isalpha() == True:
		alpha = True
	if s[i].isdigit() == True:
		digit = True
	if s[i].islower() == True:
		lower = True
	if s[i].isupper() == True:
		upper = True

print(alnum)
print(alpha)
print(digit)
print(lower)
print(upper)