s="""Python
Java
C
HTML"""

c=1
for i in s:
    if i=="\n":
        c=c+1

print("Lines:",c)

# Output:
# Lines: 4
