
#Write a Python function to check whether a number is perfect or not

def is_perfect(num):
    if num < 2:
        return False
    divisors_sum = 1  # 1 is always a divisor
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num

# Example
print(is_perfect(6))    # True
print(is_perfect(28))   # True
print(is_perfect(12))   # False
