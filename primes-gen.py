import random

def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.

    Parameters:
    - n: int
        The number to be checked.

    Returns:
    - bool:
        True if the number is prime, False otherwise.
    """

    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def generate_prime_numbers(num_primes: int) -> list:
    """
    Generates a list of random prime numbers.

    Parameters:
    - num_primes: int
        The number of prime numbers to generate.

    Returns:
    - list:
        A list of random prime numbers.
    """

    primes = []
    count = 0

    while count < num_primes:
        num = random.randint(2, 1000)  # Generate a random number between 2 and 1000

        if is_prime(num):
            primes.append(num)
            count += 1

    return primes

# Example usage:
num_primes = 5
prime_numbers = generate_prime_numbers(num_primes)
print(f"Generated {num_primes} prime numbers: {prime_numbers}")
