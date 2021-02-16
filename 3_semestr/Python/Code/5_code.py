
import stdio
import sys


class Stack:

    def __init__(self):
        self._first = None  

    def isEmpty(self):
        return self._first is None

    def push(self, item):
        self._first = _Node(item, self._first)


    def pop(self):
        item = self._first.item
        self._first = self._first.next
        return item

    def __str__(self):
        s = ''
        cur = self._first
        while cur is not None:
            s += str(cur.item) + ' '
            cur = cur.next
        return s


class _Node:
    def __init__(self, item, next):
        self.item = item  
        self.next = next 

def tracer(frame, event, arg):
    print(event, frame.f_lineno, frame.f_locals)
    return tracer
    
def tracerNull(frame, event, arg):
    return tracerNull
    
def main():
    stack = Stack()
    while  not stdio.isEmpty():
        item = stdio.readString()
        sys.settrace(tracer)
        if item != '-':
            stack.push(item)
        else:
            stdio.write(stack.pop() + ' ')
        sys.settrace(tracerNull)   
    stdio.writeln()

if __name__ == '__main__':
    main()
