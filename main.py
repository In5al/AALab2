import random
import time

import matplotlib.pyplot as plt

from algorithms.MergeSort import *


def createArray(num):
    arr = []
    for _ in range(num):
        arr.append(random.randint(1, 100000))

    return arr

if __name__ == "__main__":
    inputs = []
    results = []
    n = 10000
    for num in range(20):
        n = 10000 + num * 1000
        data = createArray(n)
        inputs.append(n)
        start_time = time.time()
        mergeSort(data)
        results.append(time.time()-start_time)
        print(f"{n} {time.time() - start_time}")
    plt.plot(inputs, results)
    plt.show()