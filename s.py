def superStack(operations, operations_cnt):
    stack = [0] * operations_cnt
    lst_idx = -1  # idx of last element

    for opr in operations:
        opr_lst = opr.split(" ")
        if opr_lst[0] == "push":
            elem = int(opr_lst[1])
            stack[lst_idx + 1] = elem
            lst_idx += 1
            print(stack[-1])
        elif opr_lst[0] == "inc":
            elms_i = int(opr_lst[1])
            elms_v = int(opr_lst[2])
            for i in range(0, elms_i):
                if i < len(stack):
                    stack[i] += elms_v
            if stack != []:
                print(stack[-1])
            else:
                print("EMPTY")
        elif opr_lst[0] == "pop":
            if stack != []:
                stack.pop()
                lst_idx -= 1
                if stack == []:
                    print("EMPTY")
                else:
                    print(stack[-1])

            else:
                print("EMPTY")


if __name__ == "__main__":
    superStack(["push 4", "pop", "push 3"], 3)