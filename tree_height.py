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
    # implement input form keyboard and from files
    input = input("From keyboard (I) or from files (F): ")
    if input == "I":
        nodes = input()
    # let user input file name to use, don't allow file names with letter a
    elif input == "'F":
        file_name = input("File name: ")
        file = open(file_name, "r")
        if file_name.__contains__("a"):
            return
        nodes = file.read()
        print(nodes)



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
main()
# print(numpy.array([1,2,3]))