s="Python programming language"
w=s.split()
m=w[0]
for i in w:
    if len(i)>len(m):
        m=i
print("Longest Word:",m)

# Output:
# Longest Word: programming
