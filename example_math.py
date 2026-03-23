def divide_numbers(a, b):
    """
    Divides number 'a' by number 'b'.
    Raises ValueError if 'b' is 0.
    Returns the quotient.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def is_prime(n):
    """
    Checks if a number is prime.
    Returns True if prime, False otherwise.
    Raises TypeError if n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    
    if n <= 1:
        return False
        
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
            
    return True
