import multiprocessing

def worker_function(number):
    print(f"Number {number} processed by Process id: {multiprocessing.current_process().pid}")

if __name__ == "__main__":
    # Numbers to be processed
    numbers = range(0,100)

    # Create a multiprocessing Pool
    pool = multiprocessing.Pool(processes=4)

    # Map numbers to the worker_function
    pool.map(worker_function, numbers)

    # Close the pool
    pool.close()

    # Wait for all processes to finish
    pool.join()