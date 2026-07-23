s="Python Programming"
r=""
for i in s:
    if i in "aeiouAEIOU":
        r=r+"*"
    else:
        r=r+i
print(r)

# Output:
# Pyth*n Pr*gr*mm*ng
