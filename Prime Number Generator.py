def prime(n):
    # to check if a given number n is a prime number
    if n < 2:
        return False
    # the prime numbers are greater than 1, if n is less than 2 then it's not prime
    for i in range(2, int(n**0.5)+1):
        # for loop from 2 to the square root of n+1
        # if n is divisible by any number beyond √n, it would have already been divisible by a smaller
        # factor before √n
        if n % i == 0:
            # checks for divisibility
            return False
    return True

def get_data():
    # to get user input for the range of numbers to check for primes and returns the start and
    # end of the range
    try:
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))
        # takes user input for start and end of the range and converts them to int

        if start <= 0 or end <= 0 or start > end:
            # both numbers should be positive and start should not be greater than end
            print("Invalid input! Enter positive integers and start <= end.")
            return None, None
        return start, end
    except ValueError:
        # handles exception if user inputs a non-integer value
        print("Please enter valid integers.")
        return None, None

start, end = get_data()
# function call to get the user input
if start is not None:
    # if the input is valid
    prime_no = [str(i) for i in range(start, end + 1) if prime(i)]
    # used for loops through all numbers from start to end+1, calls function is_prime(i) to check if
    # each number is prime, converts each prime number to a string and stores them in the list prime_no

    for i in range(0, len(prime_no), 10):
        print(" ".join(prime_no[i:i+10]))
        # for loop prints 10 prime numbers per line and " ".join() joins the prime numbers into a
        # single space-separated string
