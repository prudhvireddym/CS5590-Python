from collections import deque
str1 = input("Enter Elements of queue: ")
li = list(str1.split(' '))
queue = deque(li)
con ="yes"
while con[0]=="y":
    ans = input("\nEnter 0 for push\n1 for pop\n2 to print queue\n3 for Top most element : ")
    while ans == "0":
        a = int(input("Enter the element to append"))
        queue.append(a)
        print(queue)
        con =input("Do you want to continue y or n")
        break
    while ans == "1":
        print("Stack element poped is:")
        print(queue.popleft())
        con = input("Do you want to continue y or n")
        break
    while ans == "2":
        print("Stack elements are:")
        print(queue)
        con = input("Do you want to continue y or n")
        break
    while ans == "3":
        print("The stop of the stack is: ")
        print(queue[-1])
        con = input("Do you want to continue y or n")
        break


