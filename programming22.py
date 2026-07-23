s="PyThOn"
u=0
l=0
for i in s:
    if i.isupper():
        u=u+1
    elif i.islower():
        l=l+1
print("Uppercase:",u)
print("Lowercase:",l)

# Output:
# Uppercase: 3
# Lowercase: 3
