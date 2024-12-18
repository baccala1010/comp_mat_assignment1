#   here we define function, it can differ from the one in the task
def f(x):
    return x**3 - 2*x**2 + 4

#   implementing false position method
def falsePosition(x0, x1, e):
    step = 1
    print('\n\nfalse position method implementation')
    condition = True
    while condition:
        x2 = x0 - (x1 - x0) * f(x0)/( f(x1) - f(x0) )
        print('iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(x2)) > e

    print('\nrequired root is: %0.8f' % x2)

#   taking inputs
x0 = float(input('first guess: '))
x1 = float(input('second guess: '))
e = float(input('allowed error: '))

#   checking if the guesses are correct
if f(x0) * f(x1) > 0.0:
    print('given guesses do not bracket the root.')
    print('try again with different guesses.')
else:
    falsePosition(x0, x1, e)
