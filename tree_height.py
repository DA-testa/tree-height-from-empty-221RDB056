import sys
import threading
import numpy


def compute_height(n, parents):
    max_height = 0
    store_height = numpy.zeros(n)

    for i in range(n):
        current = i
        height = 0
        while current != -1:
            if store_height[current] != 0:
                height += store_height[current]
                break
            height += 1
            current = parents[current]
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


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()