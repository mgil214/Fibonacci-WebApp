def fib(n):
    result = str()
    seq = list()
    number = 0
    count = 0
    while count <= n:
        seq.append(number)
        count += 1
        if count < 2:
            number += 1
        else: #count >= 2 
            number = (seq[count - 1]) + (seq[count - 2])

    for i in seq:
        result = result + " " + str(i)
    return result
