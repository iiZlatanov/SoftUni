v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

first_pipe = h * p1
second_pipe = h * p2

if (first_pipe + second_pipe) > v:
    print(f'For {h:.2f} hours the pool overflows with {(first_pipe + second_pipe) - v:.2f} liters.')



!!!