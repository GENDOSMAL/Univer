import sys

def tracer(frame, event, arg):
    print(event, frame.f_lineno, frame.f_locals)
    return tracer

sys.settrace(tracer)

def fun(x):
    x[0] = 0
    x = [4,5,6]
    return x

def main():
    y = [1,2,3]
    z = fun(y)
    print("z =",z)
    print("y =",y)

main()