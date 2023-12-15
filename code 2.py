import time
import multiprocessing

# Function to apply image processing (you should define your own)
def apply_image_processing(input_path, output_path):
    # Replace this with your actual image processing logic
    pass

if __name__ == '__main__':
    input_folder = "/home/eyob/Desktop/images"
    input_paths = [f"{input_folder}/i1.jpg", f"{input_folder}/i2.jpg", f"{input_folder}/i3.jpg"]
    output_paths = [f"{input_folder}/output{i}.jpg" for i in range(1, 4)]

    # Measure time for 2 processors
    start_time_2_processors = time.time()
    with multiprocessing.Pool(processes=2) as pool:
        pool.starmap(apply_image_processing, zip(input_paths, output_paths))
    end_time_2_processors = time.time()
    time_2_processors = end_time_2_processors - start_time_2_processors

    # Measure time for 4 processors
    start_time_4_processors = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.starmap(apply_image_processing, zip(input_paths, output_paths))
    end_time_4_processors = time.time()
    time_4_processors = end_time_4_processors - start_time_4_processors

    # Calculate speedup, efficiency, and average
    speedup = time_2_processors / time_4_processors
    efficiency = speedup / 4  # Assuming 4 processors
    average_time = (time_2_processors + time_4_processors) / 2

    # Print the results
    print("Time taken (2 processors):", time_2_processors, "seconds")
    print("Time taken (4 processors):", time_4_processors, "seconds")
    print("Speedup:", speedup)
    print("Efficiency:", efficiency)
    print("Average time:", average_time, "seconds")
