import pytest

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

class TestDivideNumbers:
    @pytest.mark.parametrize("a, b, expected", [
        (10, 2, 5.0),
        (5, 2, 2.5),
        (-10, 2, -5.0),
        (10, -2, -5.0),
        (-10, -2, 5.0),
        (0, 5, 0.0),
        (7, 3, 7/3),
        (0.5, 0.2, 2.5),
        (1000000, 2, 500000.0),
        (1, 100, 0.01),
    ])
    def test_divide_numbers_happy_path_and_edge_cases(self, a, b, expected):
        assert divide_numbers(a, b) == expected

    def test_divide_numbers_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero."):
            divide_numbers(10, 0)
        with pytest.raises(ValueError, match="Cannot divide by zero."):
            divide_numbers(0, 0)

    @pytest.mark.parametrize("a, b", [
        ("a", 2),
        (10, "b"),
        ("a", "b"),
        (None, 5),
        (5, None),
        ([1, 2], 2),
        (10, [1, 2]),
    ])
    def test_divide_numbers_invalid_types(self, a, b):
        with pytest.raises(TypeError):
            divide_numbers(a, b)

class TestIsPrime:
    @pytest.mark.parametrize("n, expected", [
        (2, True),
        (3, True),
        (5, True),
        (7, True),
        (11, True),
        (13, True),
        (17, True),
        (23, True),
        (97, True),
        (101, True),
    ])
    def test_is_prime_happy_path_primes(self, n, expected):
        assert is_prime(n) == expected

    @pytest.mark.parametrize("n, expected", [
        (1, False),
        (0, False),
        (-1, False),
        (-10, False),
        (4, False),
        (6, False),
        (9, False),
        (10, False),
        (15, False),
        (25, False),
        (100, False),
        (99, False),
    ])
    def test_is_prime_happy_path_non_primes_and_edge_cases(self, n, expected):
        assert is_prime(n) == expected

    @pytest.mark.parametrize("n", [
        2.5,
        3.0,
        -5.1,
        "abc",
        None,
        [1, 2],
        {"key": "value"},
    ])
    def test_is_prime_invalid_type(self, n):
        with pytest.raises(TypeError, match="Input must be an integer."):
            is_prime(n)