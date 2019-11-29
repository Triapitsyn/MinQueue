class MinStack():
    def __init__(self, data=None):
        if data is None:
            data = []
        self.stack = list(data)
        self.prevmin = []
        if data:
            self.prevmin.append(self.stack[0])
            for elem in self.stack[1:]:
                self.prevmin.append(min(self.prevmin[-1],
                                        elem))

    def push(self, elem):
        self.stack.append(elem)
        if self.prevmin:
            self.prevmin.append(min(self.prevmin[-1],
                                    elem))
        else:
            self.prevmin = [elem]

    def pop(self):
        self.prevmin.pop()
        return self.stack.pop()

    def getmin(self):
        return self.prevmin[-1]

    def __len__(self):
        return len(self.stack)

    def __getitem__(self, item):
        return self.stack[item]

    def __bool__(self):
        return bool(self.stack)


class MinQueue():
    def __init__(self):
        self.s1, self.s2 = MinStack(), MinStack()

    def enq(self, elem):
        self.s2.push(elem)

    def deq(self):
        if not self.s1:
            self.s1, self.s2 = MinStack(data = self.s2[::-1]), MinStack()
        return self.s1.pop()

    def getmin(self):
        if self.s1:
            ans = self.s1.getmin()
        else:
            ans = self.s2.getmin()
        if self.s2:
            ans = min(ans, self.s2.getmin())
        return ans

    def __len__(self):
        return len(self.s1) + len(self.s2)
