global list_of_popularity
global list_of_filesID
list_of_popularity = []
list_of_filesID = []
list_of_size = []
list_of_k_value = []
k_parameter = 0.002
total_hit_cost = [0] * 100

number_of_miss_better_files = 0


verbose = False  # Set it to True to print which files are in the cache.
verbose_time = False


def cache_decision_sample(my_cache, file, file_size):
    if file not in my_cache.stored_files:
        # If the cache capacity is full,
        # remove the last accessed files from the cache until there is enough space for the new file.
        if my_cache.cache_size + file_size < my_cache.cache_capacity:
            my_cache.store_in_cache(file)
        else:
            while my_cache.cache_size + file_size > my_cache.cache_capacity:
                my_cache.remove_from_cache(min(my_cache.timestamp, key=my_cache.timestamp.get))
            my_cache.store_in_cache(file)


# You will fill inside this function for part 1. You can only use the information given in the arguments.
def cache_decision_part1(my_cache, file, file_popularities, file_sizes):
    global list_of_popularity
    global number_of_miss_better_files
    global list_of_size
    global list_of_k_value
    global list_of_filesID

    file_size = file_sizes[file]
    file_popularity = file_popularities[file]

    if file not in my_cache.stored_files:
        if (len(my_cache.stored_files) != len(list_of_popularity)):
            list_of_popularity.clear()
            list_of_filesID.clear()
            list_of_size.clear()
            list_of_k_value.clear()

        total_hit_cost[file] += file_size

        if (file_popularity * file_size > 0.00005):

            if my_cache.cache_size + file_size < my_cache.cache_capacity:
                my_cache.store_in_cache(file)
                list_of_popularity.append(file_popularity)
                list_of_filesID.append(file)
                list_of_size.append(file_size)
                list_of_k_value.append(file_size / file_popularity)
            else:
                if (my_cache.cache_size > 0.05):

                    current_total_pop = 0
                    for x in range(len(list_of_popularity)):
                        current_total_pop += list_of_popularity[x]
                    length = len(list_of_popularity)
                    if (len(list_of_popularity) == 0):
                        length = 1
                    if (file_popularity > (current_total_pop / length) + 0.038):
                        number_of_miss_better_files = number_of_miss_better_files + 1
                        print("better file missed", number_of_miss_better_files)
                        while my_cache.cache_size + file_size > my_cache.cache_capacity:
                            index_min = min(range(len(list_of_popularity)), key=list_of_popularity.__getitem__)
                            delete_item = list_of_filesID[index_min]
                            my_cache.remove_from_cache(delete_item)
                            list_of_popularity.pop(index_min)
                            list_of_filesID.pop(index_min)
                            list_of_size.pop(index_min)
                            list_of_k_value.pop(index_min)
                            print("New Cache_size1:%.20f" % my_cache.cache_size)
                        my_cache.store_in_cache(file)
                        list_of_popularity.append(file_popularity)
                        list_of_filesID.append(file)
                        list_of_size.append(file_size)
                        list_of_k_value.append(file_size / file_popularity)

                else:

                    current_total_pop = 0
                    for x in range(len(list_of_popularity)):
                        current_total_pop += list_of_popularity[x]
                    print("current_pop:", current_total_pop)
                    length = len(list_of_popularity)
                    if (len(list_of_popularity) == 0):
                        length = 1
                    if (file_popularity > (current_total_pop / length) + 0.015):
                        print("you shouldn't miss this file", "current:", current_total_pop / length, "this file:",
                              file_popularity)
                        while my_cache.cache_size + file_size > my_cache.cache_capacity:
                            index_min = min(range(len(list_of_popularity)), key=list_of_popularity.__getitem__)
                            delete_item = list_of_filesID[index_min]
                            my_cache.remove_from_cache(delete_item)
                            list_of_popularity.pop(index_min)
                            list_of_filesID.pop(index_min)
                            list_of_size.pop(index_min)
                            list_of_k_value.pop(index_min)
                            print("New Cache_size2:%.20f" % my_cache.cache_size)

                        my_cache.store_in_cache(file)
                        list_of_popularity.append(file_popularity)
                        list_of_filesID.append(file)
                        list_of_size.append(file_size)
                        list_of_k_value.append(file_size / file_popularity)

# You will fill inside this function for part 2. You can only use the information given in the arguments.
def cache_decision_part2(my_cache, file, file_size):
    pass
