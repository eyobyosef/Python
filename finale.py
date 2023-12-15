import time

# ... (previous code)

if __name__ == '__main__':
    input_folder = "/home/eyob/Desktop/images"

    # Measure time before parallel processing
    start_time_sequential = time.time()

    for input_path, output_path in zip(input_paths, output_paths):
        apply_gaussian_blur(input_path, output_path)

    end_time_sequential = time.time()
    sequential_time = end_time_sequential - start_time_sequential

    # Measure time after parallel processing
    start_time_parallel = time.time()

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.starmap(apply_gaussian_blur, zip(input_paths, output_paths))

    end_time_parallel = time.time()
    parallel_time = end_time_parallel - start_time_parallel

    # Calculate speedup, efficiency, and average
    speedup = sequential_time / parallel_time
    efficiency = speedup / multiprocessing.cpu_count()
    average_time = (sequential_time + parallel_time) / 2

    # Print the results
    print("Time taken (sequential processing):", sequential_time, "seconds")
    print("Time taken (parallel processing):", parallel_time, "seconds")
    print("Speed up (sequential processing):", speedup)
    print("Speed up (parallel processing):", 1.0)  # Speedup is always 1 for sequential
    print("Efficiency (sequential processing):", efficiency)
    print("Efficiency (parallel processing):", efficiency)
    print("Average time:", average_time, "seconds")
