def even_fibonacci_numbers():
    solution = 0
    prev, current = 1, 1
    while current < 4000000:
        if current % 2 == 0: 
            solution += current
        next_val = prev + current
        prev, current = current, next_val
    return solution

if __name__ == "__main__":
    print(even_fibonacci_numbers())