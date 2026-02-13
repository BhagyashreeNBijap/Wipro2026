import math
import time
from multiprocessing import Pool,cpu_count

numbers=[50000,60000,55000,45000,70000]

def compute_factoril(n):
    return math.factorial(n)


starttime1=time.time()
seq_results=[]

for num in numbers:
    result=compute_factoril(num)
    seq_results.append(result)
    print(f"sequestial:Factorial{num} calculated")

seqtime=time.time()-starttime1

print(f"\nsequential time{seqtime}")


starttime2=time.time()

with Pool(cpu_count()) as pool:
    parallel_results=pool.map(compute_factoril,numbers)


for num in numbers:
    print(f"multiprocessing:Factorial{num} calculated")

paralleltime=time.time()-starttime2

print(f"\nparallel time{paralleltime}")


