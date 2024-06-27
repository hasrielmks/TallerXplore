import sys

def submit_query(query):
    print(f"Q {' '.join(map(str, query))}")
    sys.stdout.flush()
    return int(input().strip())

def solve(N):
    # Start with initial queries
    zeros = [0] * N
    ones = [1] * N

    # Query with all zeros
    correct_zeros = submit_query(zeros)
    
    if correct_zeros == N:
        # All zeros is the correct answer
        print(f"A {' '.join(map(str, zeros))}")
        return

    # Query with all ones
    correct_ones = submit_query(ones)
    
    if correct_ones == N:
        # All ones is the correct answer
        print(f"A {' '.join(map(str, ones))}")
        return

    # We now know that the correct sequence is neither all zeros nor all ones
    # Initialize the result array with -1 to indicate unknown bits
    result = [-1] * N

    # Use the information from the initial queries to refine our guess
    for i in range(N):
        if result[i] == -1:
            test_query = result[:]
            test_query[i] = 1
            if test_query.count(1) < correct_ones:
                result[i] = 0
            else:
                result[i] = 1

    # Print the final answer
    print(f"A {' '.join(map(str, result))}")

def main():
    # Read the length of the sequence
    N = int(input().strip())
    solve(N)

if __name__ == "__main__":
    main()
