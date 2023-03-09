#stack implementation using list
stack = []
def push ():

     element=int(input("enter the element"))
     stack.append(element)
     print(stack)
def pop_element ():
    if not stack :
        print("stack is empty")
    else:
        e=stack.pop()
        print("Removed element:",e)
        print(stack)
while True :
    print("select operation 1.push 2.pop 3.quit")
    choose=int(input())
    if choose==1:
        push()
    elif choose==2:
        pop_element()
    elif choose ==3:
        break
    else:
        print("Select the correct operation")
