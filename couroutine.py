def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
        else:
            count += 1
            summ += x
            average = summ / count


def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            break
        else:
            print('.........', message)
    return 'Return'


@coroutine
def delegator(g):
    result = yield from g
    print(result)
