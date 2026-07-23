s="ab12cd34ef56"
r=""
for i in s:
    if not i.isdigit():
        r=r+i
print(r)

# Output:
# abcdef
