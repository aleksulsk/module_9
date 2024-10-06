
def is_prime(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            for i in range(2, result + 1):
                if result % i == 0 and i != result:
                    print('составное')
                    break
            else:
                print('простое')
        else:
            print('составное')

        return result

    return wrapper
@is_prime
def sum_three(x, y, z):
    return x + y + z

result = sum_three(2, 3, 6)
print(result)