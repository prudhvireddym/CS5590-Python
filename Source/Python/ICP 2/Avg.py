
plan = int(input("Insert number of plants: "))
print("Enter heights of the plants: ")
a = [int(x) for x in input().split()]
sum = 0.000
for y in a:
    sum = sum + y
tmp= sum/plan
avg=round(tmp,3)
print ("the avg of given numbers is:",avg)
