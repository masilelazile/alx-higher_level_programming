#!/usr/bin/python3
def sum_even_numbers(numbers):
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    return even_sum

def main():
    numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
    result = sum_even_numbers(numbers)
    print("Sum of even numbers:", result)

if __name__ == "__main__":
    main()
