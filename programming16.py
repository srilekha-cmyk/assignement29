s="hello"
r=""
for i in s:
    if 'a'<=i<='z':
        r=r+chr((ord(i)-97+13)%26+97)
    else:
        r=r+i
print(r)

# Output:
# uryyb
