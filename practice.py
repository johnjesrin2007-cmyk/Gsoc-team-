def is_valid(s):
    stack=[]

    for char in s:
        if char in "abc":
            stack.append(char)

        else:

            if not stack:
                return False

            top=stack.pop()

            if char==")" and top!="(":
                return False
            if char=="]" and top!="[":
                return False
            if char=="}" and top!="{":
                return False
    return len(stack)==0

s="{[()]}"
print(is_valid(s))