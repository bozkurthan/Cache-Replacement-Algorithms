import time

import numpy as np

from algorithm import cache_decision_sample, cache_decision_part1, cache_decision_part2

np.random.seed(100)

verbose = False  # Set it to True to print which files are in the cache.
verbose_time = False
custom_list = [0] * 100
total_hit_cost = [0] * 100
time2 = 0
replacement_cost = 0
hit_count = 0
cache_size_ut = 0

class Cache:

    def __init__(self, cache_capacity, file_size):
        self.file_size = file_size
        self.cache_capacity = cache_capacity
        self.stored_files = []
        self.cache_size = 0
        self.replacement_amount = 0
        self.timestamp = {}

    def remove_from_cache(self, fileID):
        if fileID in self.stored_files:
            self.stored_files.remove(fileID)
            self.cache_size -= self.file_size[fileID]
            self.replacement_amount += self.file_size[fileID]
            self.timestamp.pop(fileID)
            if verbose:
                print("Remove ", fileID)
                print("Cache:", self.stored_files)
        else:
            print("cannot remove from cache: not in cache")
            print("file:", fileID)
            time.sleep(1)

    def store_in_cache(self, fileID):
        if self.cache_size + self.file_size[fileID] < self.cache_capacity:
            if fileID in self.stored_files:
                print("cannot add to cache: already in cache")
            else:
                self.stored_files.append(fileID)
                self.cache_size += self.file_size[fileID]
                self.replacement_amount += self.file_size[fileID]
                self.timestamp[fileID] = time2
                if verbose:
                    print("Store ", fileID)
                    print("Cache:", self.stored_files)
        else:
            print("cannot add to cache: exceeding capacity. ")



def main():
    global time2
    global hit_count
    global cache_size_ut
    a = 1
    r = 1.1
    no_of_files = 100

    no_of_runs = 100
    hit_penalty = 0
    replacement_penalty = 0.1

    for i in range(no_of_runs):
        # Generate geometric file popularity
        file_popularity = [a * r ** (n - 1) for n in range(1, no_of_files + 1)]
        np.random.shuffle(file_popularity)
        file_popularity = file_popularity / np.sum(file_popularity)  # Normalize the sum to 1.

        # Generate geometric file sizes
        file_sizes = [a * r ** (n - 1) for n in range(1, no_of_files + 1)]
        np.random.shuffle(file_sizes)
        file_sizes = file_sizes / np.sum(file_sizes)  # Normalize the sum to 1.

        # Build an empty cache
        cache_capacity = 0.1
        my_cache = Cache(cache_capacity, file_sizes)

        # Generate demands based on the file popularity
        demands = np.random.choice(100, 100000, p=file_popularity)
        for i in range(len(demands)):
            time2 += 1
            fileID = demands[i]
            cache_size_ut = my_cache.cache_size + cache_size_ut
            if fileID not in my_cache.stored_files:
                hit_penalty += file_sizes[fileID]
                custom_list[fileID] = custom_list[fileID] + 1
                total_hit_cost[fileID] += file_sizes[fileID]
            else:
                hit_count = hit_count + 1


            #cache_decision_sample(my_cache, fileID, file_sizes[fileID])
            cache_decision_part2(my_cache, fileID, file_sizes[fileID])

        replacement_penalty += my_cache.replacement_amount * replacement_cost

    print("Hit Penalty: ", hit_penalty / no_of_runs)
    print("Replacement Penalty: ", replacement_penalty / no_of_runs)
    print("Total Penalty: ", (hit_penalty + replacement_penalty) / no_of_runs)
    print("Hit rate:", hit_count / 10000000)
    print("Cache utilization", cache_size_ut / 1000000)

    print("Hit count: \n")
    for x in range(100):
        print(custom_list[x])
    print("Hit cost: \n")
    for x in range(100):
        print("%.5f" %total_hit_cost[x])


if __name__ == "__main__":
    main()