import time
start = time.time()

def Square_root_convergents(numerator,denominator,count):
    for x in range(1, 1001):
        numerator += 2 * denominator
        denominator = numerator - denominator
        if len(str(denominator)) < len(str(numerator)):
            count += 1
    print(count)
    end = time.time()
    print(end - start)

Square_root_convergents(3,2,0)

