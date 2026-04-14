class MinStack:

    def __init__(self):
        self.stack = []
        self.minim = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minim or val <= self.minim[-1]:
            self.minim.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minim[-1]:
            self.minim.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minim:
            return self.minim[-1]
        else:
            print('empty')
            return 0