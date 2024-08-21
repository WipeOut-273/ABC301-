s=input()
up = 0
lo = 0
for i in range(len(s)):
    if s[i].isupper():
        up+=1
    elif s[i].islower():
        lo+=1

if up>lo:
    print(s.upper())
elif up<lo:
    print(s.lower())
