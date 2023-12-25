


def generateParenthesis(n):
    result = []
    stack = []
    # kończymy jak skończą się nawiasy
    # dodajemy zawsze jak się da otwierający nawias
    # zamykamy tylko jak zamykający jest mniejszy od otwierający
    def generateParenthesisHelper(opening, closing):
        if opening == n and closing == n:
            result.append("".join(stack))
            return
        if opening < n:
            # możemy otworzyć jeśli mamy otwierające
            stack.append('(')
            generateParenthesisHelper(opening+1, closing)
            stack.pop()
        if closing < opening:
            # zamknąć możemy tylko w takim przypadku
            stack.append(')')
            generateParenthesisHelper(opening, closing+1)
            stack.pop()

    generateParenthesisHelper(0, 0)

    return result




if __name__ == '__main__':
    generateParenthesis(3)