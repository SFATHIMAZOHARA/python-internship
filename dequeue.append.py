n=input()
stack = []
for each_bracket in n:
    if(each_bracket == '[' or each_bracket=='{' or  each_bracket== '('):
        stack.append(each_bracket)
    else:
        top=stack[-1]
        if(top=='(' and each_bracket==')'):
            stack.pop()
        elif(top=='{' and each_bracket=='}'):
            stack.pop()
        elif(top=='[' and each_bracket==']'):
            stack.pop()
        else:
            stack.append(each_bracket)
if(len(stack)==0):
    print("brackets are balance")
else:
    print("barackets are not balance")        
