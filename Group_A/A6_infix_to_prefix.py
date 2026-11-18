class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.isEmpty():
            return None
        return self.top.data


def prec(op):
    if op == '^':
        return 3
    if op == '*' or op == '/':
        return 2
    if op == '+' or op == '-':
        return 1
    return 0


def infixToPrefix(exp):
    exp = exp.replace(' ', '')
    rev = ""
    for ch in exp[::-1]:
        if ch == '(':
            rev += ')'
        elif ch == ')':
            rev += '('
        else:
            rev += ch

    st = Stack()
    post = ""

    for ch in rev:
        if ch.isalnum():
            post += ch
        elif ch == '(':
            st.push(ch)
        elif ch == ')':
            while not st.isEmpty() and st.peek() != '(':
                post += st.pop()
            st.pop()
        else:
            while not st.isEmpty() and st.peek() != '(' and (prec(st.peek()) > prec(ch) or (prec(st.peek()) == prec(ch) and ch == '^')):
                post += st.pop()
            st.push(ch)

    while not st.isEmpty():
        post += st.pop()

    return post[::-1]


exp = input("Enter infix expression: ")
print("Prefix expression:", infixToPrefix(exp))
