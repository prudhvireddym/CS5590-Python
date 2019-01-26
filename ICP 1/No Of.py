string = input("Input a string")
d=l=0
for c in string:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Number of Letters", l)
print("Number Of Digits", d)