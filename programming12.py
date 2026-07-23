s="programming"
r=""
for i in s:
    if i not in r:
        print(i,"=",s.count(i))
        r=r+i

# Output:
# p = 1
# r = 2
# o = 1
# g = 2
# a = 1
# m = 2
# i = 1
# n = 1
