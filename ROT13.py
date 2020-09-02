import string
lowers = list(string.ascii_lowercase)
uppers = list(string.ascii_uppercase)

s = input()
result =""
for i in s:
    if 'a'<=i<='z':
        idx=lowers.index(i)
        if idx<13:
            result+=lowers[idx+13]
        else:
            result+=lowers[idx-13]
    elif 'A'<=i<='Z':
        idx=uppers.index(i)
        if idx<13:
            result+=uppers[idx+13]
        else:
            result+=uppers[idx-13]

    else:
        result+=i
print(result)