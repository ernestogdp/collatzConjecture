def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def test_collatz_conjecture(numbers):
    for number in numbers:
        sequence = collatz_sequence(number)
        print(f"Collatz sequence for {number}: {sequence}")

if __name__ == "__main__":
    # Test the Collatz conjecture for a few numbers (list of numbers or unique number).
    example_numbers = [55]
    test_collatz_conjecture(example_numbers)


