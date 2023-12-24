
def isValid(s):
    parentheses = {'(': ')', '[': ']', '{':'}'}

    stack = []

    for p in s:
        if p in parentheses.keys():
            stack.append(p)
        if p in parentheses.values():
            if stack == []:
                return False
            else:
                popped = stack.pop()
                if parentheses[popped] != p:
                    return False

    if stack == []: return True
    else: return False



if __name__ == '__main__':
    print(isValid("()[]{]"))