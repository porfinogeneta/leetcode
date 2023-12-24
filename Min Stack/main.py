

class MinStack:
    def __init__(self):
        # główny stos
        self.stack = []
        # stos na wartości minimalne
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        # dodajemy do stosu wartości minimalnych, robimy to na każdej pozycji stosu
        # każda pozycja ma swoją 'korespondującą' wartość minimalną
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)


    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

if __name__ == '__main__':
    obj = MinStack()
    obj.push(4)
    obj.push(3)
    obj.push(6)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()