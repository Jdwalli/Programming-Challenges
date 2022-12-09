def power_digit_sum():
    return sum(int(num) for num in str(pow(2, 1000)))

if __name__ == "__main__":
    print(power_digit_sum())