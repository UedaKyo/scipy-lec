import numpy as np

is_prime = np.ones((100,), dtype=bool)
is_prime[:2] = 0
N_max = int(np.sqrt(len(is_prime) - 1))

for j in range(2, N_max + 1):
    is_prime[2*j::j] = False

print(np.nonzero(is_prime))