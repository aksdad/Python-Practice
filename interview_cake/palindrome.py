
def is_palindrome(num):
    half = 0

    if num < 0 or (num % 10 == 0 and num != 0):
        return False

    while num > half:
        half = half * 10 + num % 10
        num //= 10
        
    return (num == half) or (num == half // 10)


if __name__ == '__main__':
    print(is_palindrome(12321))
    