import math

# We can use the power rule to take the log of the bases 
# Example: a^b = c can be converted to logˇa(c) = b

def largest_exponential(file):
    solutions = {}
    for index, data in enumerate(open(file)):
        base, exponent = data.split(",")
        solutions[int(exponent) * math.log10(int(base))] = index + 1 
    return solutions[max(list(solutions.keys()))]
        

if __name__ == "__main__":
    print(largest_exponential("./assets/Problem99.txt"))