s="pythonProgrammingLanguage"
r=""
for i in s:
    if i.isupper():
        r=r+"_"+i.lower()
    else:
        r=r+i
print(r)

# Output:
# python_programming_language
