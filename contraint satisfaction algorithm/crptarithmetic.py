from itertools import permutations

def solve_cryptarithmetic(words, result):
    """
    Solve the cryptarithmetic puzzle where sum(words) = result.
    words: list of strings (addends)
    result: string (sum)
    """
    unique_letters = set(''.join(words) + result)
    if len(unique_letters) > 10:
        print("Too many unique letters for digits 0-9.")
        return None

    letters = list(unique_letters)
    first_letters = set(word[0] for word in words + [result])

    for perm in permutations(range(10), len(letters)):
        assignment = dict(zip(letters, perm))

        # Leading letters cannot be zero
        if any(assignment[fl] == 0 for fl in first_letters):
            continue

        def word_value(word):
            val = 0
            for ch in word:
                val = val * 10 + assignment[ch]
            return val

        sum_words = sum(word_value(word) for word in words)
        result_value = word_value(result)

        if sum_words == result_value:
            return assignment

    return None

if __name__ == "__main__":
    print("Enter the addend words separated by spaces :")
    words_input = input().strip()
    words = words_input.split()

    print("Enter the result word :")
    result = input().strip()

    solution = solve_cryptarithmetic(words, result)
    if solution:
        print("Solution found:")
        for letter in sorted(solution.keys()):
            print(f"{letter} = {solution[letter]}")
    else:
        print("No solution found.")
