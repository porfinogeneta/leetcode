
import math


def evaluateReversePN(tokens):
    stack = []
    for token in tokens:
        if token == '+':
            x,y = stack.pop(),stack.pop()
            stack.append(x+y)
        elif token == '-':
            x, y = stack.pop(), stack.pop()
            stack.append(y-x)
        elif token == '*':
            x, y = stack.pop(), stack.pop()
            stack.append(y*x)
        elif token == '/':
            x, y = stack.pop(), stack.pop()
            stack.append(int(y/x))
        else:
            stack.append(int(token))
    return stack.pop()



if __name__ == '__main__':
    print(evaluateReversePN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    print(evaluateReversePN(["4","13","5","/","+"]))