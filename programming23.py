s="My email is abc@gmail.com"
for i in s.split():
    if "@" in i:
        print(i)

# Output:
# abc@gmail.com
