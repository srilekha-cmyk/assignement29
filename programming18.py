n="21"
if n.endswith("1") and n!="11":
    print(n+"st")
elif n.endswith("2") and n!="12":
    print(n+"nd")
elif n.endswith("3") and n!="13":
    print(n+"rd")
else:
    print(n+"th")

# Output:
# 21st
