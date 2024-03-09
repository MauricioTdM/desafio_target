USER_INPUT = 56

def verify_number_in_fibonacci(user_number):
    fibonacci_sequence = [0, 1]
    sum_numbers = 0
    i = 0

    while user_number > sum_numbers:
        sum_numbers = fibonacci_sequence[0 + i] + fibonacci_sequence[1 + i]
        fibonacci_sequence.append(sum_numbers)
        i += 1
    
    if (user_number in fibonacci_sequence) == True:
        print(f'O número: {user_number}, pertence a sequência de Fibonacci: {fibonacci_sequence}')
    else:
        print(f'O número: {user_number}, não pertence a sequência de Fibonacci: {fibonacci_sequence}')

verify_number_in_fibonacci(USER_INPUT)