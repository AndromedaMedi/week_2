
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    return f"{num}"

## Better 
   
def fizzbuzz(num):
    divisible_by_3 = num % 3 == 0
    divisible_by_5 = num % 5 == 0

    if divisible_by_3 and divisible_by_5:
        return "FizzBuzz"
    elif divisible_by_3:
        return "Fizz"
    elif divisible_by_5:
        return "Buzz"
    else:
        return f"{num}"

