import time
def is_prime(number):
    for divider in range(2,number):
        if (number % divider == 0):
            return False
    return True

def find_largest_prime(limit):
    start_time = time.time()

    for n in range(1,limit):
        if is_prime(n):
            largest_prime = n

    print("The largest prime number smaller than {} is {}".format(limit,largest_prime))
    elapsed_time = time.time() - start_time
    print("Program took {:.3f} sec".format(elapsed_time))

if (__name__ == "__main__"):
    find_largest_prime(1000000)