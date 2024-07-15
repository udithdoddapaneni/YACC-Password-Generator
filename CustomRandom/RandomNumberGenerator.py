import time
import os

class PCG:
    def __init__(self, seed, seq):
        self.state = seed
        self.inc = (seq << 1) | 1

    def next(self):
        self.state = (self.state * 6364136223846793005 + self.inc) & 0xFFFFFFFFFFFFFFFF
        xorshifted = ((self.state >> 18) ^ self.state) >> 27
        rot = self.state >> 59
        return (xorshifted >> rot) | (xorshifted << ((-rot) & 31))

def Randint(a, b):
    num_instances = 4
    pcgs = []
    for _ in range(num_instances):
        seed = int(time.time() * 1000) ^ int.from_bytes(os.urandom(8), 'big')
        seq = int(time.time() * 1000000) ^ int.from_bytes(os.urandom(8), 'big')
        pcgs.append(PCG(seed, seq))

    result = 0
    for pcg in pcgs:
        result ^= pcg.next()

    return a + result % (b - a + 1)

# def test_pseudo_random_numbers(loops, start, end):
#     test_dict = {}
    
#     for _ in range(loops):
#         random_number = Randint(start, end)
        
#         if random_number in test_dict:
#             test_dict[random_number] += 1
#         else:
#             test_dict[random_number] = 1
    
#     return test_dict


# no_iterations = 1000
# start = 1
# end = 10


# occurrences_dict = test_pseudo_random_numbers(no_iterations, start, end)


# print("Occurrences of random numbers:")
# for number, count in occurrences_dict.items():
#     print(f"Number {number}: {count} times")
