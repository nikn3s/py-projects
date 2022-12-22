import sys as s
# file.py
def sumup(*n):
    # varible stores all entered values 
    allInt = (num for num in n)
    nums = float()
    # iliteration over allInt tuple 
    for i in allInt:
        # add each value to nums array
        nums += float(i)
    # free up allInt array
    del allInt
    return nums
print(sumup(2.5, 3))
# What went well?  - this mini project taught me how to use * operator. In this example, it allowed me
# to pass pass an infinite number of integers which are added together. This represents the built-in sum() funtion.