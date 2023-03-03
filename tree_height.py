# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    return max_height


def main():
    input_method = input("From keyboard (I) or from files (F): ")

    if input_method == "I":
        n = int(input())
        parents = input()
        parents = parents.split()
        print(n, parents)
    
    elif input_method == "F":
        file_name = input("File name: ")
        if file_name.__contains__("a"):
            print("Input error")
            return
        with open("test/"+file_name, "r") as f:
            n = int(f.readline())
            parents = numpy.fromstring(f.readline(), dtype = int, sep = " ")
        print(n, parents)

    else:
        print("Input error")
        return

    # implement input form keyboard and from files
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))