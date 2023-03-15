import rrt
import rrt_star
import time
import numpy as np
import pandas as pd
from tqdm import tqdm
import multiprocessing as mp
from multiprocessing import Process

print("Number of processors: ", mp.cpu_count())

number_of_iteration = 10


####################
#####    RRT   #####
####################


print("--- Exécution de RRT ---")

def RRT_Benchmark():

    #On compte les itérations et le temps d'execution
    start_time = time.time()
    iterations = rrt.main()
    end_time = time.time()
    temps_exec = end_time - start_time

    return [iterations,temps_exec]

#Multiprocessing
result = []
pool = mp.Pool()
for i in range(100):
    pool.apply_async(RRT_Benchmark, args=(), callback=result.append)
pool.close()
pool.join()

RRT_Benchmark_to_print = pd.DataFrame(result)
RRT_Benchmark_to_print.to_csv("RRT_Parallel_Benchmark.csv")


####################
##### RRT_STAR #####
####################


print("--- Exécution de RRT_Star ---")

def RRTStar_Benchmark():

    #On compte les itérations et le temps d'execution
    start_time = time.time()
    iterations = rrt_star.main()
    end_time = time.time()
    temps_exec = end_time - start_time

    return [iterations,temps_exec]


#Multiprocessing
result = []
pool = mp.Pool()
for i in range(100):
    pool.apply_async(RRTStar_Benchmark, args=(), callback=result.append)
pool.close()
pool.join()

RRTStar_Benchmark_to_print = pd.DataFrame(result)

RRTStar_Benchmark_to_print.to_csv("RRTStar_Parallel_Benchmark.csv")


