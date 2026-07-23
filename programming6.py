s="banana"
sub="a"
for i in range(len(s)):
    if s[i:i+len(sub)]==sub:
        print(i)

# Output:
# 1
# 3
# 5
