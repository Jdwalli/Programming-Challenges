def names_scores(data):
    sorted_names = sorted(data)
    return sum(sum(ord(char) - 64 for char in name) * (index + 1) for index, name in enumerate(sorted_names))

if __name__ == "__main__":
    with open ("./assets/Problem22.txt", "r") as names:
        unsorted_names = names.readline().split(",")
    print(names_scores(unsorted_names))
