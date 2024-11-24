def testCollatzConjecture(Number):

    i = 1
    while Number != 1:
        if Number % 2 == 0:
            Number = Number // 2
        else:
            Number = 3 * Number + 1
        if i > 1000:
            print(f"Testing iteration {i} for Number: {Number}")
            if i > 10000:
                return False
        i += 1
    return True


if __name__ == '__main__':
    firstNumber = 1
    print("Collatz Conjecture:")
    while True:
        print(f"Testing number: {firstNumber}", end='\r')
        if not testCollatzConjecture(firstNumber):
            print(f"\nFIND!! Not Collatz Conjecture: {firstNumber}")
            break
        firstNumber += 1
