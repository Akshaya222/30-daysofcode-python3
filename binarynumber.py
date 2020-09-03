import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary=bin(n)
    binary=binary[2:]
    print(max(map(len,binary.split('0'))))
    

