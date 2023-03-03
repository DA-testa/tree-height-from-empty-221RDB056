# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    max_height = 0
    store_height = numpy.zeros(n)
    store_usage = numpy.zeros(n)
    for i in range(n):
        if store_usage[i] == 1:
            continue
        curr = i
        height = 0
        while curr != -1:
            if store_height[curr] != 0:
                height += store_height[curr]
                break
            height += 1
            curr = parents[curr]
        store_height[i] = height
    for i in range(n):
        if max_height < store_height[i]:
            max_height = store_height[i]
    return int(max_height)


def main():
    input_method = input()

    if input_method.__contains__("I"):
        n = int(input())
        parents = numpy.fromstring(input(), dtype = int, sep=" ")
    
    elif input_method.__contains__("F"):
        file_name = input()
        if file_name.__contains__("a"):
            print("Input error")
            return
        try:
            with open("test/" + file_name, "r") as f:
                n = int(f.readline())
                parents = numpy.fromstring(f.readline(), dtype = int, sep = " ")
        except FileNotFoundError:
            print("File not found")
            return

    else:
        print("Input error")
        return
    
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))