s1="python"
s2="typhoon"
r=""
for i in s1:
    if i in s2 and i not in r:
        r=r+i
print(r)

# Output:
# pthon
