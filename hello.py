
def main():
    import time
    
    start_time = time.time()
    # Your code here
    for i in range(0,10000):
        i=i**2
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    print(f"Elapsed time: {elapsed_time} seconds")

main()
