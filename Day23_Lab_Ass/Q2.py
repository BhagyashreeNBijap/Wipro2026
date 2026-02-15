import math
import time
from multiprocessing import Pool, cpu_count

numbers = [50000, 60000, 55000, 45000, 70000]

def compute_factorial(n):
    return math.factorial(n)

if __name__ == "__main__":

    # Sequential Execution
    start_seq = time.time()

    seq_results = []
    for num in numbers:
        result = compute_factorial(num)
        seq_results.append(result)
        print(f"Sequential: Factorial of {num} calculated")

    seq_time = time.time() - start_seq
    print(f"\nSequential Time: {seq_time:.4f} seconds")


    #  Multiprocessing Execution
    start_parallel = time.time()

    with Pool(cpu_count()) as pool:
        parallel_results = pool.map(compute_factorial, numbers)

    for num in numbers:
        print(f"Multiprocessing: Factorial of {num} calculated")

    parallel_time = time.time() - start_parallel
    print(f"\nMultiprocessing Time: {parallel_time:.4f} seconds")


    # Comparison
    print("\nTime Comparison:")
    print(f"Sequential      : {seq_time:.4f} seconds")
    print(f"Multiprocessing : {parallel_time:.4f} seconds")
